# Views/PagePessoas.py
import streamlit as st
import pandas as pd
#Parte do Controller
from Controllers.Pessoas_Controller import *


def show_pessoas_page():
    st.title('Cadastro de Pessoas')

    entidade = st.sidebar.selectbox("Entidades", ["Aluno", "Personal", "Professor"])

    if entidade == "Aluno":
        operacao = st.sidebar.selectbox("Operações", ["Incluir", "Consultar", "Excluir", "Alterar"])

        if operacao == "Incluir":
            with st.form("form_aluno"):
                st.subheader("Cadastrar Aluno")
            

                cpf = st.number_input("CPF do Aluno *", min_value=0, step=1, format="%d")
                nome = st.text_input("Nome do Aluno *")
                tipo_plano = st.text_input("Tipo do plano *")
                
                rg = st.number_input("RG do Aluno", min_value=0, step=1, format="%d")
                telefone = st.number_input("Telefone do Aluno", min_value=0, step=1, format="%d")
                objetivo = st.text_input("Objetivo de treino")
                cpf_personal = st.number_input("CPF do Personal", min_value=0, step=1, format="%d")
            
                submitted = st.form_submit_button("Cadastrar Aluno")
            
                if submitted:
                
                    if not cpf or not nome or not tipo_plano:
                        st.error("Preencha todos os campos obrigatórios (*)")
                    else:
                        try:
                       
                            rg_val = rg if rg > 0 else None
                            tel_val = telefone if telefone > 0 else None
                            obj_val = objetivo if objetivo else None
                        
                            aluno = Aluno(
                            cpf=cpf,
                            rg_aluno=rg_val,
                            telefone_aluno=tel_val,
                            nome_aluno=nome,
                            objetivo_treino=obj_val,
                            tipo_plano=tipo_plano,
                            cpf_pers=cpf_personal
                            )
                        
                            incluirPessoa(aluno)
                            st.success("Aluno cadastrado com sucesso!")
                            st.rerun()  
                        
                        except Exception as e:
                            st.error(f"Erro ao cadastrar: {e}")


        if operacao == "Consultar":
            if st.button("Consultar"):
                alunos = consultarAluno()
                if alunos:
                    df = pd.DataFrame(alunos)
                    st.dataframe(df)
                else:
                    st.info("Nenhum aluno cadastrado.")



        elif operacao == "Excluir":
            alunos = consultarAluno()
            if alunos:
                df = pd.DataFrame(alunos)
                st.dataframe(df, width=1000)
    
                cpf = st.number_input("CPF do aluno a excluir:", min_value=0, step=1, format="%d")
        
                if st.button("Excluir"):
            # Agora a função retorna True/False
                    if excluirAluno(cpf):
                        st.success("Aluno excluído com sucesso!")
                        st.rerun()
                    else:
                        st.error("Aluno não encontrado!")
            else:
                st.info("Nenhum aluno cadastrado.")

        elif operacao == "Alterar":
            alunos = consultarAluno()
    
            if alunos:
                df = pd.DataFrame(alunos)
                st.dataframe(df)
        
       
                cpf = st.number_input("CPF do ALuno a alterar: ", min_value=0, step=1, format="%d")
        
       
                aluno_check = next((a for a in alunos if a["CPF"] == cpf), None)
        
                if aluno_check:
           
                    aluno_att = Aluno(
                    aluno_check["CPF"],           
                    aluno_check["RG"],              
                    aluno_check["Número"],        
                    aluno_check["Nome"],          
                    aluno_check["Objetivo de treino"],  
                    aluno_check["Tipo do Plano"], 
                    aluno_check["CPF do Personal"] 
                    )
            
                    with st.form(key="alterarAluno"):
              
                        rg_value = aluno_att.get_rg_aluno() or 0
                        telefone_value = aluno_att.get_telefone_aluno() or 0
                        cpf_personal_value = aluno_att.get_cpf_pers() or 0
                        objetivo_value = aluno_att.get_objetivo_treino() or ""
                
              
                        novo_rg = st.number_input("RG do Aluno:", value=rg_value, min_value=0, format="%d")
                        novo_telefone = st.number_input("Informe seu número:", value=telefone_value, min_value=0, format="%d")
                        novo_nome = st.text_input("Nome do Aluno:", value=aluno_att.get_nome_aluno() or "")
                        novo_objetivo = st.text_input("Objetivo de treino:", value=objetivo_value)
                        novo_plano = st.text_input("Tipo do plano:", value=aluno_att.get_tipo_plano() or "")
                        novo_cpf_personal = st.number_input("CPF do Personal:", value=cpf_personal_value, min_value=0, format="%d")

                
                        if st.form_submit_button("Salvar Alterações"):
                    
                            aluno_att.set_rg_aluno(novo_rg if novo_rg != 0 else None)
                            aluno_att.set_telefone_aluno(novo_telefone if novo_telefone != 0 else None)
                            aluno_att.set_nome_aluno(novo_nome)
                            aluno_att.set_objetivo_treino(novo_objetivo if novo_objetivo else None)
                            aluno_att.set_tipo_plano(novo_plano)
                            aluno_att.set_cpf_pers(novo_cpf_personal if novo_cpf_personal != 0 else None)
                    
                   
                            if alterarAluno(aluno_att):
                                st.success("Aluno atualizado com sucesso!")
                                st.rerun()
                            else:
                                st.error("Erro ao atualizar aluno!")
                else:
                    st.warning("Aluno não encontrado!")
            else:
                st.info("Nenhum Aluno cadastrado.")
    

    if entidade == "Professor":
        operacao = st.sidebar.selectbox("Operações", ["Incluir", "Consultar", "Excluir", "Alterar"])

        if operacao == "Incluir":
            with st.form("form_professor"):
            
                cpf = st.number_input("CPF do Professor *", min_value=0, step=1, format="%d")
                nome = st.text_input("Nome do Professor *")
                horario = st.text_input("Horário de Trabalho * (Ex: 08:00-12:00)")
                
                rg = st.number_input("RG do Professor", min_value=0, step=1, format="%d")
                telefone = st.number_input("Telefone do Professor", min_value=0, step=1, format="%d")
            
                submitted = st.form_submit_button("Cadastrar Professor")
            
                if submitted:
               
                    if not cpf or not nome or not horario:
                        st.error("Preencha todos os campos obrigatórios (*)")
                    else:
                        try:
                        
                            rg_val = rg if rg > 0 else None
                            tel_val = telefone if telefone > 0 else None
                        
                           
                            professor = Professor(
                                cpf=cpf,
                                rg_prof=rg_val,           
                                nome_prof=nome,             
                                horario_prof=horario,     
                                telefone_prof=tel_val     
                            )
                        
                            incluirPessoa(professor)
                            st.success("Professor cadastrado com sucesso!")
                            st.rerun()
                        
                        except Exception as e:
                            st.error(f"Erro ao cadastrar: {e}")

        if operacao == "Consultar":
            if st.button("Consultar"):
                professores = consultarProfessor()
                if professores:
                    df = pd.DataFrame(professores)
                    st.dataframe(df)
                else:
                    st.info("Nenhum professor cadastrado.")

        elif operacao == "Excluir":
            professores = consultarProfessor()
            if professores:
                df = pd.DataFrame(professores)
                st.dataframe(df, width=1000)

                cpf = st.number_input("CPF do professor a excluir:", min_value=0, step=1, format="%d")
        
                if st.button("Excluir"):
                    if excluirProfessor(cpf):
                        st.success("Professor excluído com sucesso!")
                        st.rerun()
                    else:
                        st.error("Professor não encontrado!")
            else:
                st.info("Nenhum professor cadastrado.")

        elif operacao == "Alterar":
            professores = consultarProfessor()

            if professores:
                df = pd.DataFrame(professores)
                st.dataframe(df)

                cpf = st.number_input("CPF do Professor a alterar: ", min_value=0, step=1, format="%d")

                professor_check = next((p for p in professores if p["CPF"] == cpf), None)

                if professor_check:
            
                    
                    professor_att = Professor(
                        professor_check["CPF"],           
                        professor_check["RG"],              
                        professor_check["Nome"],          
                        professor_check["Horário"],      
                        professor_check["Telefone"]       
                    )
            
                    with st.form(key="alterarProfessor"):
                
                       
                        novo_rg = st.number_input("RG do Professor:", value=professor_att.get_rg_prof() or 0, min_value=0, format="%d")
                        novo_nome = st.text_input("Nome do Professor:", value=professor_att.get_nome_prof() or "")
                        novo_horario = st.text_input("Horário de Trabalho:", value=professor_att.get_horario_prof() or "")
                        novo_telefone = st.number_input("Telefone do Professor:", value=professor_att.get_telefone_prof() or 0, min_value=0, format="%d")
                
                        if st.form_submit_button("Salvar Alterações"):
                    
                            
                            professor_att.set_rg_prof(novo_rg if novo_rg != 0 else None)
                            professor_att.set_nome_prof(novo_nome)
                            professor_att.set_horario_prof(novo_horario)
                            professor_att.set_telefone_prof(novo_telefone if novo_telefone != 0 else None)
                    
                            if alterarProfessor(professor_att):
                                st.success("Professor atualizado com sucesso!")
                                st.rerun()
                            else:
                                st.error("Erro ao atualizar professor!")
                else:
                    st.warning("Professor não encontrado!")
            else:
                st.info("Nenhum Professor cadastrado.")


    if entidade == "Personal":

        operacao = st.sidebar.selectbox("Operações", ["Incluir", "Consultar", "Excluir", "Alterar"])

        if operacao == "Incluir":
            with st.form(key="IncluirPersonal"):

                cpf = st.number_input("CPF do Personal*: ",min_value=0, format="%d")
                rg = st.number_input("Rg do Personal: ",min_value=0, format="%d") or None
                nome = st.text_input("Nome do Personal:* ") 
                horario = st.text_input("Horario*: ")
                telefone = st.number_input("Telefone: ",min_value=0, format="%d") or None
            
                submitted = st.form_submit_button("Cadastrar Personal")
            
                if submitted:
                    if not cpf or not nome or not horario:
                        print("Preencher todos os campos obrigatorios marcados por *")
                    else:
                        try:
                            rg = rg if rg > 0 else None
                            telefone = telefone if telefone > 0 else None

                            personal = Personal(
                                cpf=cpf,
                                rg_pers=rg,
                                nome_pers=nome,
                                horario_pers=horario,
                                telefone_pers=telefone
                            )
                            incluirPessoa(personal)
                            st.success("Personal cadastrado com sucesso!")
                        except Exception as e:
                            st.error(f"Erro ao cadastrar: {e}")

        elif operacao == "Consultar":
            if st.button("Consultar"):
                pers = consultarPersonal()
                if pers:
                    df = pd.DataFrame(pers, columns=["CPF", "RG", "Nome", "Horários", "Telefone"])
                    st.dataframe(df, width=1000)
                else:
                    st.info("Nenhum personal cadastrado.")



        elif operacao == "Excluir":
            pers = consultarPersonal()
            if pers:
                df = pd.DataFrame(pers, columns=["CPF", "RG", "Nome", "Horários", "Telefone"])
                st.dataframe(df, width=1000)
            
                cpf = st.number_input("CPF do personal a excluir:", min_value=1, format="%d")
                if st.button("Excluir"):
                    excluirPersonal(cpf)
                    st.success("Personal excluído!")
                    st.rerun()
                else:
                    st.info("Personal não encontrado.")
            else:
                st.info("Nenhum personal cadastrado.")


        elif operacao == "Alterar":
            personais = consultarPersonal()
    
            if personais:
                df = pd.DataFrame(personais)
                st.dataframe(df)

                cpf = st.number_input("CPF do Personal a alterar: ", min_value=0, step=1, format="%d")
                personal_check = next((p for p in personais if p["CPF"] == cpf), None)

                if personal_check:
    
                    personal_att = Personal(
                    personal_check["CPF"],           
                    personal_check["RG"],             
                    personal_check["Nome"],          
                    personal_check["Horário"],       
                    personal_check["Telefone"]       
                    )
    
                    with st.form(key="alterarPersonal"):
                        novo_rg = st.number_input("RG do Personal:", value=personal_att.get_rg_pers() or 0, min_value=0, format="%d")
                        novo_nome = st.text_input("Nome do Personal:", value=personal_att.get_nome_pers() or "")
                        novo_horario = st.text_input("Horário de Trabalho:", value=personal_att.get_horario_pers() or "")
                        novo_telefone = st.number_input("Telefone do Personal:", value=personal_att.get_telefone_pers() or 0, min_value=0, format="%d")
        
                        if st.form_submit_button("Salvar Alterações"):
            
                            personal_att.set_rg_pers(novo_rg if novo_rg != 0 else None)
                            personal_att.set_nome_pers(novo_nome)
                            personal_att.set_horario_pers(novo_horario)
                            personal_att.set_telefone_pers(novo_telefone if novo_telefone != 0 else None)
            
                            if alterarPersonal(personal_att):
                                st.success("Personal atualizado com sucesso!")
                                st.rerun()
                            else:
                                st.error("Erro ao atualizar personal!")
                else:
                    st.warning("Personal não encontrado!")
            else:
                st.info("Nenhum Personal cadastrado.")
