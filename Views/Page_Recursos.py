# Views/Page_Recursos.py
import streamlit as st
import pandas as pd
#Parte do Controller
from Controllers.Aula_Controller import *
from Controllers.Treino_Controller import *
from Controllers.Plano_Controller import *
from Models.Aula import Aula
from Models.Treino import Treino
from Models.Plano import Plano

def show_recursos_page(): # CORREÇÃO: Renomeado para show_recursos_page
    st.title('Cadastro de Recursos e Planos')

    recurso = st.sidebar.selectbox("Recurso", ["Aula", "Treino", "Plano"])

    if recurso == "Aula":

        operacao = st.sidebar.selectbox("Operações", ["Incluir", "Consultar", "Excluir", "Excluir Específico", "Alterar"])

        if operacao == "Incluir":
            with st.form("form_aula"):
                st.subheader("Cadastrar Aula")
                
                id_aula = st.number_input("ID da Aula:", min_value=1, step=1, format="%d") 
                tipo_aula = st.text_input("Tipo da aula:") 
                cpf_prof = st.number_input("CPF do Professor:", min_value=1, step=1, format="%d") 

                if st.form_submit_button("Cadastrar Aula"):
                    if not id_aula or not tipo_aula or not cpf_prof:
                        st.error("Preencha todos os campos.")
                    else:
                        try:
                            # Cria o objeto Aula
                            aula = Aula(int(id_aula), tipo_aula, int(cpf_prof))
                            if incluirAula(aula):
                                st.success("Aula cadastrada com sucesso!")
                                st.rerun()
                        except Exception as e:
                            st.error(f"Erro ao cadastrar: {e}")

        elif operacao == "Consultar":
            if st.button("Consultar"):
                aulas = consultarAula()
                if aulas:
                    df = pd.DataFrame(aulas, columns=["ID da Aula", "Tipo da Aula", "CPF do Professor"])
                    st.dataframe(df, width=1000)
                else:
                    st.info("Nenhum resultado encontrado. ")

        elif operacao == "Excluir":
            aulas = consultarAula()
            if aulas:
                df = pd.DataFrame(aulas, columns=["ID da Aula", "Tipo da Aula", "CPF do Professor"])
                st.dataframe(df, width=1000)
            
                id = st.number_input("ID da aula a excluir:", min_value=1, step=1, format="%d")
                if st.button("Excluir"):
                    if excluirAula(id):
                        st.success("Aula excluída!")
                        st.rerun()
                    else:
                        st.warning("Não foi possível achar a aula")
            else:
                st.info("Nenhuma aula cadastrada.")

        elif operacao == "Excluir Específico": # Bloco adicionado
            aulas = consultarAula()
            if aulas:
                df = pd.DataFrame(aulas, columns=["ID da Aula", "Tipo da Aula", "CPF do Professor"])
                st.dataframe(df, width=1000)
            
                id = st.number_input("Id da aula a excluir:", min_value=1, step=1, format="%d")
                cpf_prof = st.number_input("CPF do Professor a excluir:", min_value=1, step=1, format="%d")
                if st.button("Excluir"):
                    if excluirAulaEsp(id, cpf_prof):
                        st.success("Aula excluída!")
                        st.rerun()
                    else:
                        st.warning("Não foi possível achar a aula")
            else:
                st.info("Nenhuma aula cadastrada.")


        elif operacao == "Alterar":
            aulas = consultarAula()
            if aulas:
                df = pd.DataFrame(aulas, columns=["ID da Aula", "Tipo da Aula", "CPF do Professor"])
                st.dataframe(df, width=1000)
    
                id_original = st.number_input("ID da aula a alterar:", min_value=1, step=1, key="aula_alterar")
                
                aula_check = next((a for a in aulas if a["ID da Aula"] == id_original), None)
    
                if aula_check:
                    aula_att = Aula(
                        aula_check["ID da Aula"],
                        aula_check["Tipo da Aula"],
                        aula_check["CPF do Professor"]
                    )
        
                    with st.form(key="alterarAulaForm"):
                                    
                        novo_tipo = st.text_input("Novo tipo da aula", value=aula_att.tipo_aula or "")
                        novo_cpf_prof = st.number_input("Informe o novo cpf do professor:", value=aula_att.cpf_professor, min_value=1, step=1)
                        
                        if st.form_submit_button("Salvar Alterações"):
                    
                            aula_att.tipo_aula = novo_tipo if novo_tipo != "" else None
                            aula_att.cpf_professor = novo_cpf_prof if novo_cpf_prof != 0 else None
                            
                            if alterarAula(aula_att):
                                st.success("Aula atualizada!")
                                st.rerun()
                            else:
                                st.error("Erro ao atualizar aula!")
                else:
                    st.warning("Aula não encontrada!")
            else:
                st.info("Nenhuma Aula cadastrada.")
    

    if recurso == "Treino":

        operacao = st.sidebar.selectbox("Operações", ["Incluir", "Consultar", "Excluir", "Excluir Específico", "Alterar"])

        if operacao == "Incluir":
            with st.form("form_treino"):
                st.subheader("Cadastrar Treino")

                id_tr = st.number_input("ID do Treino:", min_value=1, step=1, format="%d")
                cpf_aluno = st.number_input("CPF do Aluno:", min_value=1, step=1, format="%d")
                alongamento = st.text_input("Alongamento:") 
                exercicios_arbcs = st.text_input("Exercícios Aeróbicos:")
                exercicios_mqn = st.text_input("Exercícios Máquina:")
                carga_mqn = st.number_input("Carga:", min_value=0)

                if st.form_submit_button("Cadastrar Treino"):
                    if not id_tr or not cpf_aluno:
                        st.error("Preencha o ID do Treino e o CPF do Aluno.")
                    else:
                        try:
                            # CORREÇÃO: Cria o objeto Treino com todos os 6 parâmetros
                            treino = Treino(
                                id=int(id_tr), 
                                alongamentos=alongamento, 
                                exercicios_arbcs=exercicios_arbcs, 
                                exercicios_mqn=exercicios_mqn, 
                                carga_mqn=int(carga_mqn), 
                                cpf_aluno=int(cpf_aluno)
                            )
                            if incluirTreino(treino):
                                st.success("Treino cadastrado com sucesso!")
                                st.rerun()
                        except Exception as e:
                            st.error(f"Erro ao cadastrar: {e}")


        elif operacao == "Consultar":
            if st.button("Consultar"):
                treinos = consultarTreino()
                if treinos:
                    df = pd.DataFrame(treinos, columns=["ID do Treino", "Alongamentos", "Ex. Aeróbicos", "Ex. Máquina", "Carga", "CPF Aluno"])
                    st.dataframe(df, width=1000)
                else:
                    st.info("Nenhum resultado encontrado. ")

        elif operacao == "Excluir":
            treinos = consultarTreino()
            if treinos:
                df = pd.DataFrame(treinos, columns=["ID do Treino", "Alongamentos", "Ex. Aeróbicos", "Ex. Máquina", "Carga", "CPF Aluno"])
                st.dataframe(df, width=1000)
            
                id = st.number_input("ID do treino a excluir:", min_value=1, step=1, format="%d")

                if st.button("Excluir"):
                    if excluirTreino(id):
                        st.success("Treino excluído!")
                        st.rerun()
                    else:
                        st.warning("Não foi possível achar o treino")
            else:
                st.info("Nenhum treino cadastrado.")
        
        elif operacao == "Excluir Específico":
            treinos = consultarTreino()
            if treinos:
                df = pd.DataFrame(treinos, columns=["ID do Treino", "Alongamentos", "Ex. Aeróbicos", "Ex. Máquina", "Carga", "CPF Aluno"])
                st.dataframe(df, width=1000)
            
                id = st.number_input("ID do treino a excluir:", min_value=1, step=1, format="%d")
                cpf_aluno = st.number_input("CPF do aluno a excluir:", min_value=1, step=1, format="%d")

                if st.button("Excluir"):
                    if excluirTreinoEsp(id, cpf_aluno):
                        st.success("Relacionamento excluído!")
                        st.rerun()
                    else:
                        st.warning("Não foi possível achar o relacionamento")
            else:
                st.info("Nenhum relacionamento cadastrado.")


        elif operacao == "Alterar":
            treinos = consultarTreino()
            if treinos:
                df = pd.DataFrame(treinos, columns=["ID do Treino", "Alongamentos", "Ex. Aeróbicos", "Ex. Máquina", "Carga", "CPF Aluno"])
                st.dataframe(df, width=1000)
    
                id_original = st.number_input("ID do treino a alterar:", min_value=1, step=1, key="id_treino_alterar")
                treino_check = next((t for t in treinos if t["ID do Treino"] == id_original), None)
    
                if treino_check:
                    treino_att = Treino(
                        treino_check["ID do Treino"], 
                        treino_check["Alongamentos"], 
                        treino_check["Ex. Aeróbicos"], 
                        treino_check["Ex. Máquina"], 
                        treino_check["Carga"], 
                        treino_check["CPF Aluno"]
                    )
        
                    with st.form(key="alterarTreino"):
                                    
                        novo_alongamento = st.text_input("Alongamento:", value=treino_att.alongamentos or "")
                        novo_aerobicos = st.text_input("Exercícios Aeróbicos:", value=treino_att.exercicios_arbcs or "")
                        novo_maquina = st.text_input("Exercícios Máquina:", value=treino_att.exercicios_mqn or "")
                        nova_carga = st.number_input("Carga:", value=treino_att.carga_mqn, min_value=0)
                        novo_cpf_aluno = st.number_input("CPF Aluno:", value=treino_att.cpf_aluno, min_value=1)
                        
                        if st.form_submit_button("Salvar Alterações"):
                    
                            treino_att.alongamentos = novo_alongamento
                            treino_att.exercicios_arbcs = novo_aerobicos
                            treino_att.exercicios_mqn = novo_maquina
                            treino_att.carga_mqn = nova_carga
                            treino_att.cpf_aluno = novo_cpf_aluno
                            
                            if alterarTreino(treino_att):
                                st.success("Treino atualizado!")
                                st.rerun()
                            else:
                                st.error("Erro ao atualizar treino!")
                else:
                    st.warning("Treino não encontrado!")
            else:
                st.info("Nenhum Treino cadastrado.")

    
    if recurso == "Plano":

        operacao = st.sidebar.selectbox("Operações", ["Incluir", "Consultar", "Excluir", "Alterar"])

        if operacao == "Incluir":
            with st.form("form_plano"):
                st.subheader("Cadastrar Plano")
                
                tipo_plano = st.text_input("Tipo do plano:")
                id_plano = st.number_input("ID do plano:", min_value=1, step=1, format="%d")  
            
                if st.form_submit_button("Cadastrar Plano"):
                    if not tipo_plano or not id_plano:
                        st.error("Preencha todos os campos.")
                    else:
                        try:
                            plano = Plano(tipo_plano, int(id_plano))
                            if incluirPlano(plano):
                                st.success("Plano cadastrado com sucesso!")
                                st.rerun()
                        except Exception as e:
                            st.error(f"Erro ao cadastrar: {e}")

        elif operacao == "Consultar":
            if st.button("Consultar"):
                planos = consultarPlano()
                if planos:
                    df = pd.DataFrame(planos, columns=["Tipo do Plano", "Id do Plano"])
                    st.dataframe(df, width=1000)
                else:
                    st.info("Nenhum resultado encontrado. ")

        elif operacao == "Excluir":
            planos = consultarPlano()
            if planos:
                df = pd.DataFrame(planos, columns=["Tipo do Plano", "Id do Plano"])
                st.dataframe(df, width=1000)
            
                tipo = st.text_input("Tipo do plano a excluir:")
                if st.button("Excluir"):
                    if excluirPlano(tipo):
                        st.success("Plano excluído!")
                        st.rerun()
                    else:
                        st.warning("Não foi possível achar o plano")
            else:
                st.info("Nenhum plano cadastrado.")


        elif operacao == "Alterar":
            planos = consultarPlano()
            if planos:
                df = pd.DataFrame(planos, columns=["Tipo do Plano", "Id do Plano"])
                st.dataframe(df, width=1000)
    
                tipo_original = st.text_input("Tipo do plano a alterar:", key="plano_alterar")
                plano_check = next((p for p in planos if p["Tipo do Plano"] == tipo_original), None)
    
                if plano_check:
                    plano_att = Plano(plano_check["Tipo do Plano"], plano_check["Id do Plano"])
        
                    with st.form(key="alterarPlanoForm"):
                                    
                        novo_tipo = st.text_input("Novo tipo do plano", value=plano_att.tipo_plano)
                        novo_id = st.number_input("Id do plano:", value=plano_att.id_plano, min_value=1, step=1)
                        
                        if st.form_submit_button("Salvar Alterações"):
                    
                            plano_att.tipo_plano = novo_tipo if novo_tipo != "" else None
                            plano_att.id_plano = novo_id if novo_id != 0 else None
                            
                            if alterarPlano(plano_att):
                                st.success("Plano atualizado!")
                                st.rerun()
                            else:
                                st.error("Erro ao atualizar Plano!")
                else:
                    st.warning("Plano não encontrado!")
            else:
                st.info("Nenhum Plano cadastrado.")