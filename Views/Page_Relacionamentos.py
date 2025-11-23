# Views/PagePessoas.py
import streamlit as st
import pandas as pd
#Parte do Controller
from Controllers.Aluno_Aula_Controller import *
from Controllers.Treino_Maquina_Controller import *


def show_relacionamentos_page():
    st.title('Cadastro de Relacionamentos')

    relacionamento = st.sidebar.selectbox("Relacionamentos", ["Aluno_Aula", "Treino_Maquina"])

    if relacionamento == "Aluno_Aula":

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


        elif operacao == "Excluir Específico":
            aluno_aula = consultarAlunoAula()
            if aluno_aula:
                df = pd.DataFrame(aluno_aula, columns=["CPF", "ID da Aula"])
                st.dataframe(df, width=1000)
            
                cpf = st.number_input("CPF do aluno a excluir:", min_value=1)
                id = st.number_input("Id da aula a excluir:", min_value = 1)
                if st.button("Excluir"):
                    excluirAlunoAulaEsp(id, cpf)
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
    

    if relacionamento == "Treino_Maquina":

        operacao = st.sidebar.selectbox("Operações", ["Incluir", "Consultar", "Excluir", "Excluir Específico", "Alterar"])

        if operacao == "Incluir":
            treino_maquina = Treino_Maquina(0, "")
        
            treino_maquina.id_tr = st.number_input("ID do Treino: ")
            treino_maquina.nome_mqn = st.text_input("Nome da Máquina: ") 
        
        if st.button("Cadastrar"):
            incluirTreinoMaquina(treino_maquina)
            st.success("Relacionamento cadastrado com sucesso!")


        elif operacao == "Consultar":
            if st.button("Consultar"):
                treino_maquina = consultarTreinoMaquina()
                if treino_maquina:
                    df = pd.DataFrame(treino_maquina, columns=["ID do Treino", "Nome da Maquina"])
                    st.dataframe(df, width=1000)
                else:
                    st.info("Nenhum resultado encontrado. ")

        elif operacao == "Excluir":
            treino_maquina = consultarTreinoMaquina()
            if treino_maquina:
                df = pd.DataFrame(treino_maquina, columns=["ID do Treino", "Nome da Maquina"])
                st.dataframe(df, width=1000)
            
                id = st.number_input("ID do treino a excluir:", min_value=1)

                if st.button("Excluir"):
                    excluirTreinoMaquina(id)
                    st.success("Relacionamento excluído!")
                    st.rerun()
                else:
                    st.info("Não foi possível achar o relacionamento")
            else:
                st.info("Nenhum relacionamento cadastrado.")


        elif operacao == "Excluir Específico":
            treino_maquina = consultarTreinoMaquina()
            if treino_maquina:
                df = pd.DataFrame(treino_maquina, columns=["ID do Treino", "Nome da Maquina"])
                st.dataframe(df, width=1000)
            
                maquina = st.text_input("Nome da Maquina a excluir:", min_value=1)
                id = st.number_input("Id da aula a excluir:", min_value = 1)
                if st.button("Excluir"):
                    excluirTreinoMaquinaEsp(id, maquina)
                    st.success("Relacionamento excluído!")
                    st.rerun()
                else:
                    st.info("Não foi possível achar o relacionamento")
            else:
                st.info("Nenhum relacionamento cadastrado.")        

        elif operacao == "Alterar":
            treino_maquina = consultarTreinoMaquina()
            if treino_maquina:
                df = pd.DataFrame(treino_maquina, columns=["ID do Treino", "Nome da Maquina"])
                st.dataframe(df, width=1000)
    
                id = st.number_input("ID do treino com relacionamento a alterar:", min_value=1, key="id_maquina_alterar")
                treino_maquina_check = next((t for t in treino_maquina if t[0] == id), None)
    
                if treino_maquina_check:
                    treino_maquina_att = Treino_Maquina(*treino_maquina_check[:2])
        
                    with st.form(key="alterarTreinoMaquina"):
                                    
                
                        novo_id = st.number_input("Id do treino", value=treino_maquina_att.id_tr, min_value=0)
                        nova_maquina = st.text_input("Informe o nome da maquina:", value=treino_maquina_att.nome_mqn, min_value=0)
                        
                        if st.form_submit_button("Salvar Alterações"):
                    
                            treino_maquina_att.id_tr(novo_id if novo_id != 0 else None)
                            treino_maquina_att.nome_mqn(nova_maquina if novo_cpf != 0 else None)
                            
                    
                            alterarTreinoMaquina(treino_maquina_att)
                            st.success("Relacionamento atualizado!")
                            st.rerun()
                else:
                    st.warning("Relacionamento não encontrado!")
            else:
                st.info("Nenhum relacionamento cadastrado.")