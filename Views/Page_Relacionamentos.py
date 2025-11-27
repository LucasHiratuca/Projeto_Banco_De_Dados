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
            with st.form("form_aluno_aula"):
                st.subheader("Vincular Aluno à Aula")
                
                id_aula = st.number_input("ID da Aula *", min_value=0, step=1, format="%d")
                cpf_aluno = st.number_input("CPF do Aluno *", min_value=0, step=1, format="%d")
                
                submitted = st.form_submit_button("Vincular Aluno à Aula")
                
                if submitted:
                    if not id_aula or not cpf_aluno:
                        st.error("Preencha todos os campos obrigatórios (*)")
                    else:
                        try:
                            aluno_aula = Aluno_Aula(
                                id_aula=int(id_aula),
                                cpf_aluno=int(cpf_aluno)
                            )
                            
                            if incluirAlunoAula(aluno_aula):
                                st.success("Aluno vinculado à aula com sucesso!")
                                st.rerun()
                            else:
                                st.error("Erro ao vincular aluno à aula!")
                                
                        except Exception as e:
                            st.error(f"Erro ao cadastrar: {e}")

        elif operacao == "Consultar":
            if st.button("Consultar"):
                aluno_aulas = consultarAlunoAula()
                if aluno_aulas:
                    df = pd.DataFrame(aluno_aulas)
                    st.dataframe(df)
                else:
                    st.info("Nenhum vínculo aluno-aula cadastrado.")

        elif operacao == "Excluir":
            aluno_aulas = consultarAlunoAula()
            if aluno_aulas:
                df = pd.DataFrame(aluno_aulas)
                st.dataframe(df, width=1000)
            
                id_aula = st.number_input("ID da aula para excluir TODOS os vínculos:", min_value=0, step=1, format="%d")
                
                if st.button("Excluir"):
                    if excluirAlunoAula(id_aula):
                        st.success("Todos os vínculos desta aula foram excluídos!")
                        st.rerun()
                    else:
                        st.error("Não foi possível excluir os vínculos!")
            else:
                st.info("Nenhum vínculo aluno-aula cadastrado.")

        elif operacao == "Excluir Específico":
            aluno_aulas = consultarAlunoAula()
            if aluno_aulas:
                df = pd.DataFrame(aluno_aulas)
                st.dataframe(df, width=1000)
            
                id_aula = st.number_input("ID da aula:", min_value=0, step=1, format="%d")
                cpf_aluno = st.number_input("CPF do aluno:", min_value=0, step=1, format="%d")
                
                if st.button("Excluir Vínculo Específico"):
                    if excluirAlunoAulaEsp(id_aula, cpf_aluno):
                        st.success("Vínculo específico excluído com sucesso!")
                        st.rerun()
                    else:
                        st.error("Vínculo não encontrado!")
            else:
                st.info("Nenhum vínculo aluno-aula cadastrado.")

        elif operacao == "Alterar":
            aluno_aulas = consultarAlunoAula()
            
            if aluno_aulas:
                df = pd.DataFrame(aluno_aulas)
                st.dataframe(df)

                id_aula = st.number_input("ID da aula do vínculo a alterar:", min_value=0, step=1, format="%d")
                cpf_aluno = st.number_input("CPF do aluno do vínculo a alterar:", min_value=0, step=1, format="%d")

                aluno_aula_check = next((a for a in aluno_aulas if a["ID_Aula"] == id_aula and a["CPF_Aluno"] == cpf_aluno), None)

                if aluno_aula_check:
                    aluno_aula_att = Aluno_Aula(
                        aluno_aula_check["ID_Aula"],
                        aluno_aula_check["CPF_Aluno"]
                    )
        
                    with st.form(key="alterarAlunoAula"):
                        novo_id_aula = st.number_input("Novo ID da Aula:", value=aluno_aula_att.id_aula, min_value=0, format="%d")
                        novo_cpf_aluno = st.number_input("Novo CPF do Aluno:", value=aluno_aula_att.cpf_aluno, min_value=0, format="%d")
                        
                        if st.form_submit_button("Salvar Alterações"):
                            aluno_aula_att.id_aula = novo_id_aula
                            aluno_aula_att.cpf_aluno = novo_cpf_aluno
                    
                            if alterarAlunoAula(aluno_aula_att):
                                st.success("Vínculo atualizado com sucesso!")
                                st.rerun()
                            else:
                                st.error("Erro ao atualizar vínculo!")
                else:
                    st.warning("Vínculo não encontrado!")
            else:
                st.info("Nenhum vínculo aluno-aula cadastrado.")

    if relacionamento == "Treino_Maquina":
        operacao = st.sidebar.selectbox("Operações", ["Incluir", "Consultar", "Excluir", "Excluir Específico", "Alterar"])

        if operacao == "Incluir":
            with st.form("form_treino_maquina"):
                st.subheader("Vincular Treino à Máquina")
                
                id_treino = st.number_input("ID do Treino *", min_value=0, step=1, format="%d")
                nome_maquina = st.text_input("Nome da Máquina *")
                
                submitted = st.form_submit_button("Vincular Treino à Máquina")
                
                if submitted:
                    if not id_treino or not nome_maquina:
                        st.error("Preencha todos os campos obrigatórios (*)")
                    else:
                        try:
                            treino_maquina = Treino_Maquina(
                                id_tr=int(id_treino),
                                nome_mqn=nome_maquina
                            )
                            
                            if incluirTreinoMaquina(treino_maquina):
                                st.success("Treino vinculado à máquina com sucesso!")
                                st.rerun()
                            else:
                                st.error("Erro ao vincular treino à máquina!")
                                
                        except Exception as e:
                            st.error(f"Erro ao cadastrar: {e}")

        elif operacao == "Consultar":
            if st.button("Consultar"):
                treino_maquinas = consultarTreinoMaquina()
                if treino_maquinas:
                    df = pd.DataFrame(treino_maquinas)
                    st.dataframe(df)
                else:
                    st.info("Nenhum vínculo treino-máquina cadastrado.")

        elif operacao == "Excluir":
            treino_maquinas = consultarTreinoMaquina()
            if treino_maquinas:
                df = pd.DataFrame(treino_maquinas)
                st.dataframe(df, width=1000)
            
                id_treino = st.number_input("ID do treino para excluir TODOS os vínculos:", min_value=0, step=1, format="%d")
                
                if st.button("Excluir"):
                    if excluirTreinoMaquina(id_treino):
                        st.success("Todos os vínculos deste treino foram excluídos!")
                        st.rerun()
                    else:
                        st.error("Não foi possível excluir os vínculos!")
            else:
                st.info("Nenhum vínculo treino-máquina cadastrado.")

        elif operacao == "Excluir Específico":
            treino_maquinas = consultarTreinoMaquina()
            if treino_maquinas:
                df = pd.DataFrame(treino_maquinas)
                st.dataframe(df, width=1000)
            
                id_treino = st.number_input("ID do treino:", min_value=0, step=1, format="%d")
                nome_maquina = st.text_input("Nome da máquina:")
                
                if st.button("Excluir Vínculo Específico"):
                    if excluirTreinoMaquinaEsp(id_treino, nome_maquina):
                        st.success("Vínculo específico excluído com sucesso!")
                        st.rerun()
                    else:
                        st.error("Vínculo não encontrado!")
            else:
                st.info("Nenhum vínculo treino-máquina cadastrado.")

        elif operacao == "Alterar":
            treino_maquinas = consultarTreinoMaquina()
            
            if treino_maquinas:
                df = pd.DataFrame(treino_maquinas)
                st.dataframe(df)

                id_treino = st.number_input("ID do treino do vínculo a alterar:", min_value=0, step=1, format="%d")
                nome_maquina = st.text_input("Nome da máquina do vínculo a alterar:")

                treino_maquina_check = next((t for t in treino_maquinas if t["ID_Treino"] == id_treino and t["Nome_Maquina"] == nome_maquina), None)

                if treino_maquina_check:
                    treino_maquina_att = Treino_Maquina(
                        treino_maquina_check["ID_Treino"],
                        treino_maquina_check["Nome_Maquina"]
                    )
        
                    with st.form(key="alterarTreinoMaquina"):
                        novo_id_treino = st.number_input("Novo ID do Treino:", value=treino_maquina_att.id_tr, min_value=0, format="%d")
                        novo_nome_maquina = st.text_input("Novo Nome da Máquina:", value=treino_maquina_att.nome_mqn or "")
                        
                        if st.form_submit_button("Salvar Alterações"):
                            treino_maquina_att.id_tr = novo_id_treino
                            treino_maquina_att.nome_mqn = novo_nome_maquina
                    
                            if alterarTreinoMaquina(treino_maquina_att):
                                st.success("Vínculo atualizado com sucesso!")
                                st.rerun()
                            else:
                                st.error("Erro ao atualizar vínculo!")
                else:
                    st.warning("Vínculo não encontrado!")
            else:
                st.info("Nenhum vínculo treino-máquina cadastrado.")