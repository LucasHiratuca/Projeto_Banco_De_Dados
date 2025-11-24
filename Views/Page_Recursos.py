# Views/Pagerecursos.py
import streamlit as st
import pandas as pd
#Parte do Controller
from Controllers.Aula_Controller import *
from Controllers.Treino import *
from Controllers.Plano_Controller import *

def show_relacionamentos_page():
    st.title('Cadastro de Relacionamentos')

    recurso = st.sidebar.selectbox("Recurso", ["Aula", "Treino", "Plano"])

    if recurso == "Aula":

        operacao = st.sidebar.selectbox("Operações", ["Incluir", "Consultar", "Excluir", "Excluir Específico", "Alterar"])

        if operacao == "Incluir":
            aula = Aula(0, "", 0)
        
            aula.id_aula = st.number_input("ID da Aula: ") 
            aula.tipo_aula = st.text_input("Tipo da aula: ") 
            aula.cpf_prof = st.number_input("CPF do Professor: ") 
        
        if st.button("Cadastrar"):
            incluirAula(aula)
            st.success("Aula cadastrada com sucesso!")

        elif operacao == "Consultar":
            if st.button("Consultar"):
                aula = consultarAula()
                if aula:
                    df = pd.DataFrame(aula, columns=["ID da Aula", "Tipo da Aula", "CPF do Professor"])
                    st.dataframe(df, width=1000)
                else:
                    st.info("Nenhum resultado encontrado. ")

        elif operacao == "Excluir":
            aula = consultarAula()
            if aula:
                df = pd.DataFrame(aula, columns=["ID da Aula", "Tipo da Aula", "CPF do Professor"])
                st.dataframe(df, width=1000)
            
                id = st.number_input("ID da aula a excluir:", min_value=1)
                if st.button("Excluir"):
                    excluirAula(id)
                    st.success("Aula excluído!")
                    st.rerun()
                else:
                    st.info("Não foi possível achar a aula")
            else:
                st.info("Nenhuma aula cadastrada.")


        elif operacao == "Alterar":
            aula = consultarAula()
            if aula:
                df = pd.DataFrame(aula, columns=["ID da Aula", "Tipo da Aula", "CPF do Professor"])
                st.dataframe(df, width=1000)
    
                id = st.number_input("ID da aula a alterar:", min_value=1, key="aula_alterar")
                aula_check = next((a for a in aula if a[0] == id), None)
    
                if aula_check:
                    aula_att = Aula(*aula_check[:3])
        
                    with st.form(key="alterarAluno"):
                                    
                
                        novo_id = st.number_input("Id da aula:", value=aula_att.id_aula, min_value=0)
                        novo_tipo = st.text_input("Novo tipo da aula", value=aula_att.tipo_aula,)
                        novo_cpf_prof = st.number_input("Informe o cpf:", value=aula_att.cpf_prof, min_value=0)
                        
                        if st.form_submit_button("Salvar Alterações"):
                    
                            aula_att.id_aula(novo_id if novo_id != 0 else None)
                            aula_att.tipo_aula(novo_tipo if novo_tipo != "" else None)
                            aula_att.cpf_prof(novo_cpf_prof if novo_cpf_prof != 0 else None)
                            
                    
                            Aula(aula_att)
                            st.success("Aula atualizado!")
                            st.rerun()
                else:
                    st.warning("Aula não encontrada!")
            else:
                st.info("Nenhuma AUla cadastrada.")
    

    if recurso == "Treino":

        operacao = st.sidebar.selectbox("Operações", ["Incluir", "Consultar", "Excluir", "Excluir Específico", "Alterar"])

        if operacao == "Incluir":
            treino = Treino(0, "", "", "", 0, 0)
        
            treino.id_tr = st.number_input("ID do Treino: ")
            treino.alongamento = st.text_input("Alongamento: ") 
            treino.
            treino.
            treino.
        
        if st.button("Cadastrar"):
            incluirTreino(treino)
            st.success("Treino cadastrado com sucesso!")


        elif operacao == "Consultar":
            if st.button("Consultar"):
                treino = consultarTreino()
                if treino:
                    df = pd.DataFrame(treino, columns=["ID do Treino", "Alongamento", "Ex. Aeróbicos", "Ex. Máquina", "Carga", "CPF Aluno"])
                    st.dataframe(df, width=1000)
                else:
                    st.info("Nenhum resultado encontrado. ")

        elif operacao == "Excluir":
            treino = consultarTreino()
            if treino:
                df = pd.DataFrame(treino, columns=["ID do Treino", "Alongamento", "Ex. Aeróbicos", "Ex. Máquina", "Carga", "CPF Aluno"])
                st.dataframe(df, width=1000)
            
                id = st.number_input("ID do treino a excluir:", min_value=1)

                if st.button("Excluir"):
                    excluirTreino(id)
                    st.success("Treino excluído!")
                    st.rerun()
                else:
                    st.info("Não foi possível achar o treino")
            else:
                st.info("Nenhum treino cadastrado.")


        elif operacao == "Alterar":
            treino = consultarTreino()
            if treino:
                df = pd.DataFrame(treino, columns=["ID do Treino", "Alongamento", "Ex. Aeróbicos", "Ex. Máquina", "Carga", "CPF Aluno"])
                st.dataframe(df, width=1000)
    
                id = st.number_input("ID do treino com relacionamento a alterar:", min_value=1, key="id_treino_alterar")
                treino_check = next((t for t in treino if t[0] == id), None)
    
                if treino_check:
                    treino_att = Treino(*treino_check[:6])
        
                    with st.form(key="alterarTreino"):
                                    
                
                        novo_id = st.number_input("Id do treino", value=treino_att.id_tr, min_value=0)
                        nova_maquina = st.text_input("Informe o nome da maquina:", value=treino_att.nome_mqn, min_value=0)
                        
                        if st.form_submit_button("Salvar Alterações"):
                    
                            treino_att.id_tr(novo_id if novo_id != 0 else None)
                            treino_att.nome_mqn(nova_maquina if novo_cpf != 0 else None)
                            
                    
                            alterarTreino(treino_att)
                            st.success("Treino atualizado!")
                            st.rerun()
                else:
                    st.warning("Treino não encontrado!")
            else:
                st.info("Nenhum Treino cadastrado.")

    
    if recurso == "Plano":

        operacao = st.sidebar.selectbox("Operações", ["Incluir", "Consultar", "Excluir", "Excluir Específico", "Alterar"])

        if operacao == "Incluir":
            plano = Plano("", 0)

            plano.tipo_plano = st.text_input("Tipo do plano:")
            plano.id_aula = st.number_input("ID do plano: ")  
        
        if st.button("Cadastrar"):
            incluirPlano(plano)
            st.success("Plano cadastrado com sucesso!")

        elif operacao == "Consultar":
            if st.button("Consultar"):
                plano = consultarPlano()
                if plano:
                    df = pd.DataFrame(plano, columns=["Tipo do Plano", "Id do Plano"])
                    st.dataframe(df, width=1000)
                else:
                    st.info("Nenhum resultado encontrado. ")

        elif operacao == "Excluir":
            plano = consultarPlano()
            if plano:
                df = pd.DataFrame(plano, columns=["Tipo do Plano", "Id do Plano"])
                st.dataframe(df, width=1000)
            
                tipo = st.text_input("Tipo do plano a excluir:", min_value=1)
                if st.button("Excluir"):
                    excluirPlano(tipo)
                    st.success("Plano excluído!")
                    st.rerun()
                else:
                    st.info("Não foi possível achar o plano")
            else:
                st.info("Nenhum plano cadastrado.")


        elif operacao == "Alterar":
            plano = consultarPlano()
            if plano:
                df = pd.DataFrame(plano, columns=["Tipo do Plano", "Id do Plano"])
                st.dataframe(df, width=1000)
    
                tipo = st.text_input("Tipo do plano a alterar:", min_value=1, key="plano_alterar")
                plano_check = next((p for p in plano if p[0] == tipo), None)
    
                if plano_check:
                    plano_att = Plano(*plano_check[:2])
        
                    with st.form(key="alterarPlano"):
                                    
                        novo_tipo = st.text_input("Novo tipo do plano", value=aula_att.tipo_aula,)
                        novo_id = st.number_input("Id do plano:", value=aula_att.id_aula, min_value=0)
                        
                        if st.form_submit_button("Salvar Alterações"):
                    
                            plano_att.tipo_plano(novo_tipo if novo_tipo != "" else None)
                            plano_att.id_plano(novo_id if novo_id != 0 else None)
                            
                    
                            Plano(plano_att)
                            st.success("Plano atualizado!")
                            st.rerun()
                else:
                    st.warning("Plano não encontrado!")
            else:
                st.info("Nenhum Plano cadastrado.")