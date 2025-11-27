# Views/Page_Relacionamentos.py
import streamlit as st
import pandas as pd
#Parte do Controller
from Controllers.Aluno_Aula_Controller import *
from Controllers.Treino_Maquina_Controller import *
from Models.Aluno_Aula import Aluno_Aula
from Models.Treino_Maquina import Treino_Maquina


def show_relacionamentos_page():
    st.title('Cadastro de Relacionamentos')

    relacionamento = st.sidebar.selectbox("Relacionamentos", ["Aluno_Aula", "Treino_Maquina"])

    if relacionamento == "Aluno_Aula":

        operacao = st.sidebar.selectbox("Operações", ["Incluir", "Consultar", "Excluir", "Excluir Específico", "Alterar"])

        if operacao == "Incluir":
            with st.form("form_aluno_aula"):
                st.subheader("Cadastrar Aluno em Aula")
                
                id_aula = st.number_input("ID da Aula:", min_value=1, step=1, format="%d") 
                cpf_aluno = st.number_input("CPF do Aluno:", min_value=1, step=1, format="%d")
                
                if st.form_submit_button("Cadastrar"):
                    if not id_aula or not cpf_aluno:
                        st.error("Preencha todos os campos.")
                    else:
                        try:
                            aluno_aula = Aluno_Aula(int(id_aula), int(cpf_aluno))
                            if incluirAlunoAula(aluno_aula):
                                st.success("Aluno cadastrado na aula com sucesso!")
                                st.rerun()
                        except Exception as e:
                            st.error(f"Erro ao cadastrar: {e}")

        elif operacao == "Consultar":
            if st.button("Consultar"):
                aluno_aula_data = consultarAlunoAula()
                if aluno_aula_data:
                    # CORREÇÃO: Coluna ajustada para "CPF do Aluno"
                    df = pd.DataFrame(aluno_aula_data, columns=["ID da Aula", "CPF do Aluno"])
                    st.dataframe(df, width=1000)
                else:
                    st.info("Nenhum resultado encontrado. ")

        elif operacao == "Excluir":
            aluno_aula_data = consultarAlunoAula()
            if aluno_aula_data:
                df = pd.DataFrame(aluno_aula_data, columns=["ID da Aula", "CPF do Aluno"])
                st.dataframe(df, width=1000)
            
                id = st.number_input("Digite ID da aula a excluir:", min_value=1, step=1, format="%d")
                if st.button("Excluir"):
                    if excluirAlunoAula(id):
                        st.success("Relacionamento excluído!")
                        st.rerun()
                    else:
                        st.warning("Não foi possível achar o relacionamento")
            else:
                st.info("Nenhum relacionamento cadastrado.")


        elif operacao == "Excluir Específico":
            aluno_aula_data = consultarAlunoAula()
            if aluno_aula_data:
                df = pd.DataFrame(aluno_aula_data, columns=["ID da Aula", "CPF do Aluno"])
                st.dataframe(df, width=1000)
            
                cpf = st.number_input("CPF do aluno a excluir:", min_value=1, step=1, format="%d")
                id = st.number_input("Id da aula a excluir:", min_value = 1, step=1, format="%d")
                if st.button("Excluir"):
                    if excluirAlunoAulaEsp(id, cpf):
                        st.success("Relacionamento excluído!")
                        st.rerun()
                    else:
                        st.warning("Não foi possível achar o relacionamento")
            else:
                st.info("Nenhum relacionamento cadastrado.")        

        elif operacao == "Alterar":
            aluno_aula_data = consultarAlunoAula()
            if aluno_aula_data:
                df = pd.DataFrame(aluno_aula_data, columns=["ID da Aula", "CPF do Aluno"])
                st.dataframe(df, width=1000)
    
                id_original = st.number_input("ID da aula com relacionamento a alterar:", min_value=1, step=1, key="id_aula_alterar")
                
                # CORREÇÃO: Busca por chave do dicionário ("ID da Aula")
                aluno_check = next((a for a in aluno_aula_data if a["ID da Aula"] == id_original), None)
    
                if aluno_check:
                    # Cria o objeto para alterar
                    aluno_aula_att = Aluno_Aula(
                        aluno_check["ID da Aula"],
                        aluno_check["CPF do Aluno"]
                    )
        
                    with st.form(key="alterarAlunoAulaForm"):
                                    
                        novo_cpf = st.number_input("Informe o novo CPF do aluno:", value=aluno_aula_att.cpf_aluno, min_value=1)
                        
                        if st.form_submit_button("Salvar Alterações"):
                    
                            aluno_aula_att.cpf_aluno = novo_cpf if novo_cpf != 0 else None
                            
                            # ID da Aula é a chave primária, não pode ser alterado a não ser que você queira excluir e incluir um novo.
                            # Para manter a simplicidade, atualizamos apenas o CPF associado a essa Aula.
                            if alterarAlunoAula(aluno_aula_att):
                                st.success("Relacionamento atualizado!")
                                st.rerun()
                            else:
                                st.error("Erro ao atualizar relacionamento!")
                else:
                    st.warning("Relacionamento não encontrado!")
            else:
                st.info("Nenhum relacionamento cadastrado.")
    

    if relacionamento == "Treino_Maquina":

        operacao = st.sidebar.selectbox("Operações", ["Incluir", "Consultar", "Excluir", "Excluir Específico", "Alterar"])

        if operacao == "Incluir":
            with st.form("form_treino_maquina"):
                st.subheader("Cadastrar Máquina em Treino")
                
                id_tr = st.number_input("ID do Treino:", min_value=1, step=1, format="%d")
                nome_mqn = st.text_input("Nome da Máquina:") 
                
                if st.form_submit_button("Cadastrar"):
                    if not id_tr or not nome_mqn:
                        st.error("Preencha todos os campos.")
                    else:
                        try:
                            treino_maquina = Treino_Maquina(int(id_tr), nome_mqn)
                            if incluirTreinoMaquina(treino_maquina):
                                st.success("Relacionamento cadastrado com sucesso!")
                                st.rerun()
                        except Exception as e:
                            st.error(f"Erro ao cadastrar: {e}")


        elif operacao == "Consultar":
            if st.button("Consultar"):
                treino_maquina_data = consultarTreinoMaquina()
                if treino_maquina_data:
                    df = pd.DataFrame(treino_maquina_data, columns=["ID do Treino", "Nome da Maquina"])
                    st.dataframe(df, width=1000)
                else:
                    st.info("Nenhum resultado encontrado. ")

        elif operacao == "Excluir":
            treino_maquina_data = consultarTreinoMaquina()
            if treino_maquina_data:
                df = pd.DataFrame(treino_maquina_data, columns=["ID do Treino", "Nome da Maquina"])
                st.dataframe(df, width=1000)
            
                id = st.number_input("ID do treino a excluir:", min_value=1, step=1, format="%d")

                if st.button("Excluir"):
                    if excluirTreinoMaquina(id):
                        st.success("Relacionamento excluído!")
                        st.rerun()
                    else:
                        st.warning("Não foi possível achar o relacionamento")
            else:
                st.info("Nenhum relacionamento cadastrado.")


        elif operacao == "Excluir Específico":
            treino_maquina_data = consultarTreinoMaquina()
            if treino_maquina_data:
                df = pd.DataFrame(treino_maquina_data, columns=["ID do Treino", "Nome da Maquina"])
                st.dataframe(df, width=1000)
            
                maquina = st.text_input("Nome da Maquina a excluir:")
                id = st.number_input("ID do treino a excluir:", min_value = 1, step=1, format="%d")
                if st.button("Excluir"):
                    if excluirTreinoMaquinaEsp(id, maquina):
                        st.success("Relacionamento excluído!")
                        st.rerun()
                    else:
                        st.warning("Não foi possível achar o relacionamento")
            else:
                st.info("Nenhum relacionamento cadastrado.")        

        elif operacao == "Alterar":
            treino_maquina_data = consultarTreinoMaquina()
            if treino_maquina_data:
                df = pd.DataFrame(treino_maquina_data, columns=["ID do Treino", "Nome da Maquina"])
                st.dataframe(df, width=1000)
    
                id_original = st.number_input("ID do treino com relacionamento a alterar:", min_value=1, step=1, key="id_treino_alterar")
                nome_maquina_original = st.text_input("Nome da Máquina original:", key="nome_maquina_original")

                # Busca pela chave composta
                treino_maquina_check = next((t for t in treino_maquina_data if t["ID do Treino"] == id_original and t["Nome da Maquina"] == nome_maquina_original), None)
    
                if treino_maquina_check:
                    treino_maquina_att = Treino_Maquina(
                        treino_maquina_check["ID do Treino"],
                        treino_maquina_check["Nome da Maquina"]
                    )
        
                    with st.form(key="alterarTreinoMaquina"):
                                    
                        novo_nome = st.text_input("Informe o novo nome da maquina:", value=treino_maquina_att.nome_mqn or "")
                        
                        if st.form_submit_button("Salvar Alterações"):
                            
                            treino_maquina_att.nome_mqn = novo_nome if novo_nome != "" else None
                            
                            if alterarTreinoMaquina(treino_maquina_att, nome_maquina_original):
                                st.success("Relacionamento atualizado!")
                                st.rerun()
                            else:
                                st.error("Erro ao atualizar relacionamento!")
                else:
                    st.warning("Relacionamento não encontrado!")
            else:
                st.info("Nenhum relacionamento cadastrado.")