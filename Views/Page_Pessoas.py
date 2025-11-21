# Views/PageAluno.py
import streamlit as st
import pandas as pd
#Parte do Controller
from Controllers.Pessoas_Controller import *
from Models.Aluno import Aluno
from Models.Professor import Professor
from Models.Personal import Personal

def show_pessoas_page():
    st.title('Cadastro de Pessoas')

    entidade = st.sidebar.selectbox("Entidades", ["Aluno", "Personal", "Professor"])

    if entidade == "Aluno":

        operacao = st.sidebar.selectbox("Operações", ["Incluir", "Consultar", "Excluir", "Alterar"])

        if operacao == "Incluir":
            aluno = Aluno(0, 0, 0, "", "", "", 0)
        
            aluno.cpf = st.number_input("CPF do Aluno: ")
            aluno.rg_aluno = st.number_input("Rg do Aluno: ") or None
            aluno.telefone_aluno = st.number_input("Informe seu número: ") or None
            aluno.nome_aluno = st.text_input_("Nome do Aluno: ")
            aluno.objetivo_treino = st.text_input_("Objetivo de treino: ") or None
            aluno.tipo_plano = st.text_input_("Tipo do plano: ") or None
            aluno.cpf_pers = st.number_input("CPF do Personal: ") or None
            
        
        if st.button("Cadastrar"):
            incluirPessoa(aluno)
            st.success("Aluno cadastrado com sucesso!")

        elif operacao == "Consultar":
            if st.button("Consultar"):
                alunos = consultarAluno()
                if alunos:
                    df = pd.DataFrame(alunos, columns=["CPF", "RG", "Número", "Nome", "Objetivo de treino", "Tipo do Plano", "CPF do Personal"])
                    st.dataframe(df, width=1000)
                else:
                    st.info("Nenhum aluno cadastrado.")

        elif operacao == "Excluir":
            alunos = consultarAluno()
            if alunos:
                df = pd.DataFrame(alunos, columns=["CPF", "RG", "Número", "Nome", "Objetivo de treino", "Tipo do Plano", "CPF do Personal"])
                st.dataframe(df, width=1000)
            
                cpf = st.number_input("CPF do aluno a excluir:", min_value=1)
                if st.button("Excluir"):
                    excluirAluno(cpf)
                    st.success("Aluno excluído!")
                    st.rerun()
            else:
                st.info("Nenhum aluno cadastrado.")

        elif operacao == "Alterar":
            alunos = consultarAluno()
            if alunos:
                df = pd.DataFrame(alunos, columns=["CPF Aluno", "RG", "Número", "Nome", "Objetivo De Treino", "Tipo do Plano", "CPF do Personal"])
                st.dataframe(df, width=1000)
            
                cpf = st.number_input("CPF do aluno a alterar:", min_value=1)
                aluno_check = next((a for a in alunos if a[0] == cpf), None)
            
                if aluno_check:
                    aluno_att = Aluno(*aluno_check[:7])
                
                    with st.form(key="alterarAluno"):
                        aluno_att.rg_aluno        = st.number_input("RG do Aluno:", value=aluno_att.rg_aluno)
                        aluno_att.telefone_aluno  = st.number_input("Informe seu número:", value=aluno_att.telefone_aluno)
                        aluno_att.nome_aluno      = st.text_input("Nome do Aluno:", value=aluno_att.nome_aluno)
                        aluno_att.objetivo_treino = st.text_input("Objetivo de treino:", value=aluno_att.objetivo_treino)
                        aluno_att.tipo_plano      = st.text_input("Tipo do plano:", value=aluno_att.tipo_plano)
                        aluno_att.cpf_pers        = st.number_input("CPF do Personal:", value=aluno_att.cpf_pers)
                    
                        if st.form_submit_button("Salvar Alterações"):
                            alterarAluno(aluno_att)
                            st.success("Aluno atualizado!")
                            st.rerun()
                else:
                    st.warning("Aluno não encontrado!")
            else:
                st.info("Nenhum Aluno cadastrado.")
    

    if entidade == "Professor":

        operacao = st.sidebar.selectbox("Operações", ["Incluir", "Consultar", "Excluir", "Alterar"])

        if operacao == "Incluir":
            aluno = Aluno(0, 0, 0, "", "", "", 0)
        
            aluno.cpf = st.number_input("CPF do Aluno: ")
            aluno.rg_aluno = st.number_input("Rg do Aluno: ") or None
            aluno.telefone_aluno = st.number_input("Informe seu número: ") or None
            aluno.nome_aluno = st.text_input_("Nome do Aluno: ")
            aluno.objetivo_treino = st.text_input_("Objetivo de treino: ") or None
            aluno.tipo_plano = st.text_input_("Tipo do plano: ") or None
            aluno.cpf_pers = st.number_input("CPF do Personal: ") or None
            
        
        if st.button("Cadastrar"):
            incluirPessoa(aluno)
            st.success("Aluno cadastrado com sucesso!")

        elif operacao == "Consultar":
            if st.button("Consultar"):
                alunos = consultarAluno()
                if alunos:
                    df = pd.DataFrame(alunos, columns=["CPF", "RG", "Número", "Nome", "Objetivo de treino", "Tipo do Plano", "CPF do Personal"])
                    st.dataframe(df, width=1000)
                else:
                    st.info("Nenhum aluno cadastrado.")

        elif operacao == "Excluir":
            alunos = consultarAluno()
            if alunos:
                df = pd.DataFrame(alunos, columns=["CPF", "RG", "Número", "Nome", "Objetivo de treino", "Tipo do Plano", "CPF do Personal"])
                st.dataframe(df, width=1000)
            
                cpf = st.number_input("CPF do aluno a excluir:", min_value=1)
                if st.button("Excluir"):
                    excluirAluno(cpf)
                    st.success("Aluno excluído!")
                    st.rerun()
            else:
                st.info("Nenhum aluno cadastrado.")

        elif operacao == "Alterar":
            alunos = consultarAluno()
            if alunos:
                df = pd.DataFrame(alunos, columns=["CPF Aluno", "RG", "Número", "Nome", "Objetivo De Treino", "Tipo do Plano", "CPF do Personal"])
                st.dataframe(df, width=1000)
            
                cpf = st.number_input("CPF do aluno a alterar:", min_value=1)
                aluno_check = next((a for a in alunos if a[0] == cpf), None)
            
                if aluno_check:
                    aluno_att = Aluno(*aluno_check[:7])
                
                    with st.form(key="alterarAluno"):
                        aluno_att.rg_aluno        = st.number_input("RG do Aluno:", value=aluno_att.rg_aluno)
                        aluno_att.telefone_aluno  = st.number_input("Informe seu número:", value=aluno_att.telefone_aluno)
                        aluno_att.nome_aluno      = st.text_input("Nome do Aluno:", value=aluno_att.nome_aluno)
                        aluno_att.objetivo_treino = st.text_input("Objetivo de treino:", value=aluno_att.objetivo_treino)
                        aluno_att.tipo_plano      = st.text_input("Tipo do plano:", value=aluno_att.tipo_plano)
                        aluno_att.cpf_pers        = st.number_input("CPF do Personal:", value=aluno_att.cpf_pers)
                    
                        if st.form_submit_button("Salvar Alterações"):
                            alterarAluno(aluno_att)
                            st.success("Aluno atualizado!")
                            st.rerun()
                else:
                    st.warning("Aluno não encontrado!")
            else:
                st.info("Nenhum Aluno cadastrado.")


    if entidade == "Personal":

        operacao = st.sidebar.selectbox("Operações", ["Incluir", "Consultar", "Excluir", "Alterar"])

        if operacao == "Incluir":
            aluno = Aluno(0, 0, 0, "", "", "", 0)
        
            aluno.cpf = st.number_input("CPF do Aluno: ")
            aluno.rg_aluno = st.number_input("Rg do Aluno: ") or None
            aluno.telefone_aluno = st.number_input("Informe seu número: ") or None
            aluno.nome_aluno = st.text_input_("Nome do Aluno: ")
            aluno.objetivo_treino = st.text_input_("Objetivo de treino: ") or None
            aluno.tipo_plano = st.text_input_("Tipo do plano: ") or None
            aluno.cpf_pers = st.number_input("CPF do Personal: ") or None
            
        
        if st.button("Cadastrar"):
            incluirPessoa(aluno)
            st.success("Aluno cadastrado com sucesso!")

        elif operacao == "Consultar":
            if st.button("Consultar"):
                alunos = consultarAluno()
                if alunos:
                    df = pd.DataFrame(alunos, columns=["CPF", "RG", "Número", "Nome", "Objetivo de treino", "Tipo do Plano", "CPF do Personal"])
                    st.dataframe(df, width=1000)
                else:
                    st.info("Nenhum aluno cadastrado.")

        elif operacao == "Excluir":
            alunos = consultarAluno()
            if alunos:
                df = pd.DataFrame(alunos, columns=["CPF", "RG", "Número", "Nome", "Objetivo de treino", "Tipo do Plano", "CPF do Personal"])
                st.dataframe(df, width=1000)
            
                cpf = st.number_input("CPF do aluno a excluir:", min_value=1)
                if st.button("Excluir"):
                    excluirAluno(cpf)
                    st.success("Aluno excluído!")
                    st.rerun()
            else:
                st.info("Nenhum aluno cadastrado.")

        elif operacao == "Alterar":
            alunos = consultarAluno()
            if alunos:
                df = pd.DataFrame(alunos, columns=["CPF Aluno", "RG", "Número", "Nome", "Objetivo De Treino", "Tipo do Plano", "CPF do Personal"])
                st.dataframe(df, width=1000)
            
                cpf = st.number_input("CPF do aluno a alterar:", min_value=1)
                aluno_check = next((a for a in alunos if a[0] == cpf), None)
            
                if aluno_check:
                    aluno_att = Aluno(*aluno_check[:7])
                
                    with st.form(key="alterarAluno"):
                        aluno_att.rg_aluno        = st.number_input("RG do Aluno:", value=aluno_att.rg_aluno)
                        aluno_att.telefone_aluno  = st.number_input("Informe seu número:", value=aluno_att.telefone_aluno)
                        aluno_att.nome_aluno      = st.text_input("Nome do Aluno:", value=aluno_att.nome_aluno)
                        aluno_att.objetivo_treino = st.text_input("Objetivo de treino:", value=aluno_att.objetivo_treino)
                        aluno_att.tipo_plano      = st.text_input("Tipo do plano:", value=aluno_att.tipo_plano)
                        aluno_att.cpf_pers        = st.number_input("CPF do Personal:", value=aluno_att.cpf_pers)
                    
                        if st.form_submit_button("Salvar Alterações"):
                            alterarAluno(aluno_att)
                            st.success("Aluno atualizado!")
                            st.rerun()
                else:
                    st.warning("Aluno não encontrado!")
            else:
                st.info("Nenhum Aluno cadastrado.")            