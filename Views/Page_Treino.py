# Views/PagePessoas.py
import streamlit as st
import pandas as pd
#Parte do Controller
from Controllers.Treino import *


def show_relacionamentos_page():
    st.title('Cadastro de Relacionamentos')

    operacao = st.sidebar.selectbox("Operações", ["Incluir", "Consultar", "Excluir", "Excluir Específico", "Alterar"])

    if operacao == "Incluir":
        aluno_aula = Aluno_Aula(0, 0)
        
        aluno_aula.cpf_aluno = st.number_input("CPF do Aluno: ")
        aluno_aula.id_aula = st.number_input("ID da Aula: ") 
        
    if st.button("Cadastrar"):
        incluirAlunoAula(aluno_aula)
        st.success("Aluno cadastrado na aula com sucesso!")

    elif operacao == "Consultar":
        if st.button("Consultar"):
            aluno_aula = consultarAlunoAula()
            if aluno_aula:
                df = pd.DataFrame(aluno_aula, columns=["CPF", "ID da Aula"])
                st.dataframe(df, width=1000)
            else:
                st.info("Nenhum resultado encontrado. ")

    elif operacao == "Excluir":
        aluno_aula = consultarAlunoAula()
        if aluno_aula:
            df = pd.DataFrame(aluno_aula, columns=["CPF", "ID da Aula"])
            st.dataframe(df, width=1000)
            
            cpf = st.number_input("CPF do aluno a excluir:", min_value=1)
            if st.button("Excluir"):
                excluirAlunoAula(cpf)
                st.success("Relacionamento excluído!")
                st.rerun()
            else:
                st.info("Não foi possível achar o relacionamento")
        else:
            st.info("Nenhum relacionamento cadastrado.")
     

    elif operacao == "Alterar":
        aluno_aula = consultarAlunoAula()
        if aluno_aula:
            df = pd.DataFrame(aluno_aula, columns=["CPF", "ID da Aula"])
            st.dataframe(df, width=1000)
    
            cpf = st.number_input("CPF do aluno com relacionamento a alterar:", min_value=1, key="cpf_aluno_alterar")
            aluno_check = next((a for a in aluno_aula if a[1] == cpf), None)
    
            if aluno_check:
                aluno_aula_att = Aluno_Aula(*aluno_check[:2])
        
                with st.form(key="alterarAluno"):
                                    
                    novo_id = st.number_input("Id da aula:", value=aluno_aula_att.id_aula, min_value=0)
                    novo_cpf = st.number_input("Informe o cpf:", value=aluno_aula_att.cpf_aluno, min_value=0)
                        
                    if st.form_submit_button("Salvar Alterações"):
                    
                        aluno_aula_att.id_aula(novo_id if novo_id != 0 else None)
                        aluno_aula_att.cpf_aluno(novo_cpf if novo_cpf != 0 else None)
                            
                    
                        alterarAlunoAula(aluno_aula_att)
                        st.success("Relacionamento atualizado!")
                        st.rerun()
            else:
                st.warning("Relacionamento não encontrado!")
        else:
            st.info("Nenhum relacionamento cadastrado.")