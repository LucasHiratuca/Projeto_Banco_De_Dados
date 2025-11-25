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
            
            # Campos obrigatórios primeiro
                cpf = st.number_input("CPF do Aluno *", min_value=0, step=1, format="%d")
                nome = st.text_input("Nome do Aluno *")
                tipo_plano = st.text_input("Tipo do plano *")
                
            
            # Campos opcionais
                rg = st.number_input("RG do Aluno", min_value=0, step=1, format="%d")
                telefone = st.number_input("Telefone do Aluno", min_value=0, step=1, format="%d")
                objetivo = st.text_input("Objetivo de treino")
                cpf_personal = st.number_input("CPF do Personal *", min_value=0, step=1, format="%d")
            
                submitted = st.form_submit_button("Cadastrar Aluno")
            
                if submitted:
                # Validação
                    if not cpf or not nome or not tipo_plano:
                        st.error("Preencha todos os campos obrigatórios (*)")
                    else:
                        try:
                        # Converte para None se for 0
                            rg_val = int(rg) if rg and rg > 0 else None
                            tel_val = int(telefone) if telefone and telefone > 0 else None
                            obj_val = objetivo if objetivo else None
                        
                            aluno = Aluno(
                            cpf=int(cpf),
                            rg_aluno=rg_val,
                            telefone_aluno=tel_val,
                            nome_aluno=nome,
                            objetivo_treino=obj_val,
                            tipo_plano=tipo_plano,
                            cpf_pers=int(cpf_personal)
                            )
                        
                            incluirPessoa(aluno)
                            st.success("Aluno cadastrado com sucesso!")
                            st.rerun()  # Limpa o formulário
                        
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
        
        # Seleciona CPF do aluno
                cpf = st.number_input("CPF do ALuno a alterar: ", min_value=0, step=1, format="%d")
        
        # Encontra o aluno (agora usando chave do dicionário)
                aluno_check = next((a for a in alunos if a["CPF"] == cpf), None)
        
                if aluno_check:
            # Cria objeto Aluno com os dados corretos (na ordem do construtor)
                    aluno_att = Aluno(
                    aluno_check["CPF"],           # cpf
                    aluno_check["RG"],            # rg_aluno  
                    aluno_check["Número"],        # telefone_aluno
                    aluno_check["Nome"],          # nome_aluno
                    aluno_check["Objetivo de treino"],  # objetivo_treino
                    aluno_check["Tipo do Plano"], # tipo_plano
                    aluno_check["CPF do Personal"] # cpf_pers
                    )
            
                    with st.form(key="alterarAluno"):
                # Use os GETTERS para obter os valores atuais
                        rg_value = aluno_att.get_rg_aluno() or 0
                        telefone_value = aluno_att.get_telefone_aluno() or 0
                        cpf_personal_value = aluno_att.get_cpf_pers() or 0
                        objetivo_value = aluno_att.get_objetivo_treino() or ""
                
                # Campos de edição
                        novo_rg = st.number_input("RG do Aluno:", value=rg_value, min_value=0, format="%d")
                        novo_telefone = st.number_input("Informe seu número:", value=telefone_value, min_value=0, format="%d")
                        novo_nome = st.text_input("Nome do Aluno:", value=aluno_att.get_nome_aluno() or "")
                        novo_objetivo = st.text_input("Objetivo de treino:", value=objetivo_value)
                        novo_plano = st.text_input("Tipo do plano:", value=aluno_att.get_tipo_plano() or "")
                        novo_cpf_personal = st.number_input("CPF do Personal:", value=cpf_personal_value, min_value=0, format="%d")
                
                        if st.form_submit_button("Salvar Alterações"):
                    # Use os SETTERS corretamente
                            aluno_att.set_rg_aluno(novo_rg if novo_rg != 0 else None)
                            aluno_att.set_telefone_aluno(novo_telefone if novo_telefone != 0 else None)
                            aluno_att.set_nome_aluno(novo_nome)
                            aluno_att.set_objetivo_treino(novo_objetivo if novo_objetivo else None)
                            aluno_att.set_tipo_plano(novo_plano)
                            aluno_att.set_cpf_pers(novo_cpf_personal if novo_cpf_personal != 0 else None)
                    
                    # Chama a função de alteração
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
            professor = Professor(0, 0, "", "", 0)
        
            professor.get_cpf = st.number_input("CPF do Professor: ")
            professor.get_rg_prof = st.number_input("Rg do Professor: ") or None
            professor.get_nome_prof = st.text_input("Nome do Professor: ")
            professor.get_horario_prof = st.text_input("Horários: ") 
            professor.get_telefone_prof = st.number_input("Telefone: ") or None
            
        
        if st.button("Cadastrar"):
            incluirPessoa(professor)
            st.success("Professor cadastrado com sucesso!")


        elif operacao == "Consultar":
            if st.button("Consultar"):
                profs = consultarProfessor()
                if profs:
                    df = pd.DataFrame(profs, columns=["CPF", "RG", "Nome", "Horários", "Telefone"])
                    st.dataframe(df, width=1000)
                else:
                    st.info("Nenhum professor cadastrado.")

        elif operacao == "Excluir":
            profs = consultarProfessor()
            if profs:
                df = pd.DataFrame(profs, columns=["CPF", "RG", "Nome", "Horários", "Telefone"])
                st.dataframe(df, width=1000)
            
                cpf = st.number_input("CPF do professor a excluir:", min_value=1)
                if st.button("Excluir"):
                    excluirProfessor(cpf)
                    st.success("Professor excluído!")
                    st.rerun()
                else: 
                    st.info("Não foi possível achar o professor")
            else:
                st.info("Nenhum professor cadastrado.")


        elif operacao == "Alterar":
            profs = consultarProfessor()
            if profs:
                df = pd.DataFrame(profs, columns=["CPF", "RG", "Nome", "Horários", "Telefone"])
                st.dataframe(df, width=1000)
    
                cpf = st.number_input("CPF do professor a alterar:", min_value=1, key="cpf_personal_alterar")
                prof_check = next((p for p in profs if p[0] == cpf), None)
    
                if prof_check:
                    prof_att = Professor(*prof_check[:5])
        
                    with st.form(key="alterarProfessor"):
                
                        rg_value = prof_att.get_rg_prof or 0
                        telefone_value = prof_att.get_telefone_prof or 0
                
                        novo_rg = st.number_input("RG do Professor:", value=rg_value, min_value=0)
                        novo_nome = st.text_input("Informe seu nome:", value=prof_att.get_nome_prof or "")
                        novo_horario = st.text_input("Horário do Professor:", value=prof_att.get_horario_prof or "")
                        novo_telefone = st.number_input("Telefone:", value=telefone_value, min_value=0)
                
                    if st.form_submit_button("Salvar Alterações"):
                    
                        prof_att.set_rg_prof(novo_rg if novo_rg != 0 else None)
                        prof_att.set_nome_prof(novo_nome or None)
                        prof_att.set_horario_prof(novo_horario or None)
                        prof_att.set_telefone_prof(novo_telefone if novo_telefone != 0 else None)
                    
                        alterarProfessor(prof_att)
                        st.success("Professor atualizado!")
                        st.rerun()
                else:
                    st.warning("Professor não encontrado!")
            else:
                st.info("Nenhum professor cadastrado.")

    if entidade == "Personal":

        operacao = st.sidebar.selectbox("Operações", ["Incluir", "Consultar", "Excluir", "Alterar"])

        if operacao == "Incluir":
            personal = Personal(0, 0, "", "", 0)
        
            personal.set_cpf = st.number_input("CPF do Personal: ")
            personal.set_rg_pers = st.number_input("Rg do Personal: ") or None
            personal.set_nome_pers = st.text_input("Nome do Personal: ") 
            personal.set_horario_pers = st.text_input("Horario: ")
            personal.set_telefone_pers = st.number_input("Telefone: ") or None
            
            if st.button("Cadastrar"):
                incluirPessoa(personal)
                st.success("Personal cadastrado com sucesso!")

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
            if alunos:
                df = pd.DataFrame(pers, columns=["CPF", "RG", "Nome", "Horários", "Telefone"])
                st.dataframe(df, width=1000)
            
                cpf = st.number_input("CPF do personal a excluir:", min_value=1)
                if st.button("Excluir"):
                    excluirPersonal(cpf)
                    st.success("Personal excluído!")
                    st.rerun()
                else:
                    st.info("Personal não encontrado.")
            else:
                st.info("Nenhum personal cadastrado.")


        elif operacao == "Alterar":
            pers = consultarPersonal()
            if personal:
                df = pd.DataFrame(pers, columns=["CPF", "RG", "Nome", "Horários", "Telefone"])
                st.dataframe(df, width=1000)
    
                cpf = st.number_input("CPF do personal a alterar:", min_value=1, key="cpf_personal_alterar")
                pers_check = next((p for p in pers if p[0] == cpf), None)
    
                if pers_check:
                    pers_att = Personal(*pers_check[:5])
        
                    with st.form(key="alterarPersonal"):
                
                        rg_value = pers_att.get_rg_pers or 0
                        telefone_value = pers_att.get_telefone_pers or 0
                
                        novo_rg = st.number_input("RG do Personal:", value=rg_value, min_value=0)
                        novo_nome = st.text_input("Informe seu nome:", value=pers_att.get_nome_pers or "")
                        novo_horario = st.text_input("Horário do Personal:", value=pers_att.get_horario_pers or "")
                        novo_telefone = st.number_input("Telefone:", value=telefone_value, min_value=0)
                
                        if st.form_submit_button("Salvar Alterações"):
                    
                            pers_att.set_rg_pers(novo_rg if novo_rg != 0 else None)
                            pers_att.set_nome_pers(novo_nome or None)
                            pers_att.set_horario_pers(novo_horario or None)
                            pers_att.set_telefone_pers(novo_telefone if novo_telefone != 0 else None)
                    
                            alterarPersonal(pers_att)
                            st.success("Personal atualizado!")
                            st.rerun()
                else:
                    st.warning("Personal não encontrado!")
            else:
                st.info("Nenhum personal cadastrado.")       