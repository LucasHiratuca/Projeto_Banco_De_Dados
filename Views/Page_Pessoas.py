# Views/Page_Pessoas.py
import streamlit as st
import pandas as pd
#Parte do Controller
from Controllers.Pessoas_Controller import *
from Models.Professor import Professor
from Models.Personal import Personal

def show_pessoas_page():
    st.title('Cadastro de Pessoas')

    entidade = st.sidebar.selectbox("Entidades", ["Aluno", "Personal", "Professor"])

    if entidade == "Aluno":
        operacao = st.sidebar.selectbox("Operações", ["Incluir", "Consultar", "Excluir", "Alterar"])
        # ... (BLOCO ALUNO JÁ CORRETO)
        if operacao == "Incluir":
            with st.form("form_aluno"):
                st.subheader("Cadastrar Aluno")
            
            # Campos obrigatórios primeiro
                cpf = st.number_input("CPF do Aluno *", min_value=1, step=1, format="%d")
                nome = st.text_input("Nome do Aluno *")
                tipo_plano = st.text_input("Tipo do plano *")
                
            
            # Campos opcionais
                rg = st.number_input("RG do Aluno", min_value=0, step=1, format="%d")
                telefone = st.number_input("Telefone do Aluno", min_value=0, step=1, format="%d")
                objetivo = st.text_input("Objetivo de treino")
                cpf_personal = st.number_input("CPF do Personal *", min_value=1, step=1, format="%d")
            
                submitted = st.form_submit_button("Cadastrar Aluno")
            
                if submitted:
                # Validação
                    if not cpf or not nome or not tipo_plano or not cpf_personal:
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
                        
                            if incluirPessoa(aluno):
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
    
                cpf = st.number_input("CPF do aluno a excluir:", min_value=1, step=1, format="%d")
        
                if st.button("Excluir"):
                    if excluirAluno(cpf):
                        st.success("Aluno excluído com sucesso!")
                        st.rerun()
                    else:
                        st.warning("Aluno não encontrado!")
            else:
                st.info("Nenhum aluno cadastrado.")

        elif operacao == "Alterar":
            alunos = consultarAluno()
    
            if alunos:
                df = pd.DataFrame(alunos)
                st.dataframe(df)
        
        # Seleciona CPF do aluno
                cpf = st.number_input("CPF do ALuno a alterar: ", min_value=1, step=1, format="%d")
        
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
                        novo_cpf_personal = st.number_input("CPF do Personal:", value=cpf_personal_value, min_value=1, format="%d")
                
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
            with st.form("form_professor"):
                st.subheader("Cadastrar Professor")

                cpf = st.number_input("CPF do Professor:", min_value=1, step=1, format="%d")
                rg_prof = st.number_input("RG do Professor:", min_value=0, step=1, format="%d") or None
                nome_prof = st.text_input("Nome do Professor:")
                horario_prof = st.text_input("Horários:") 
                telefone_prof = st.number_input("Telefone:", min_value=0, step=1, format="%d") or None
                
                submitted = st.form_submit_button("Cadastrar Professor")
            
                if submitted:
                    if not cpf or not nome_prof or not horario_prof:
                        st.error("Preencha todos os campos obrigatórios (*)")
                    else:
                        try:
                            # CORREÇÃO: Cria o objeto Professor com os dados coletados.
                            professor = Professor(
                                cpf=int(cpf), 
                                rg_prof=rg_prof, 
                                nome_prof=nome_prof, 
                                horario_prof=horario_prof, 
                                telefone_prof=telefone_prof
                            )
                            if incluirPessoa(professor):
                                st.success("Professor cadastrado com sucesso!")
                                st.rerun()
                        except Exception as e:
                            st.error(f"Erro ao cadastrar: {e}")


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
            
                cpf = st.number_input("CPF do professor a excluir:", min_value=1, step=1, format="%d")
                if st.button("Excluir"):
                    if excluirProfessor(cpf):
                        st.success("Professor excluído!")
                        st.rerun()
                    else: 
                        st.warning("Não foi possível achar o professor")
            else:
                st.info("Nenhum professor cadastrado.")


        elif operacao == "Alterar":
            profs = consultarProfessor()
            if profs:
                df = pd.DataFrame(profs, columns=["CPF", "RG", "Nome", "Horários", "Telefone"])
                st.dataframe(df, width=1000)
    
                cpf = st.number_input("CPF do professor a alterar:", min_value=1, step=1, format="%d", key="cpf_professor_alterar")
                prof_check = next((p for p in profs if p["CPF"] == cpf), None)
    
                if prof_check:
                    # Cria objeto Professor
                    prof_att = Professor(
                        prof_check["CPF"], 
                        prof_check["RG"], 
                        prof_check["Nome"], 
                        prof_check["Horários"], 
                        prof_check["Telefone"]
                    )
        
                    with st.form(key="alterarProfessor"):
                
                        rg_value = prof_att.get_rg_prof() or 0
                        telefone_value = prof_att.get_telefone_prof() or 0
                
                        novo_rg = st.number_input("RG do Professor:", value=rg_value, min_value=0, format="%d")
                        novo_nome = st.text_input("Informe seu nome:", value=prof_att.get_nome_prof() or "")
                        novo_horario = st.text_input("Horário do Professor:", value=prof_att.get_horario_prof() or "")
                        novo_telefone = st.number_input("Telefone:", value=telefone_value, min_value=0, format="%d")
                
                        if st.form_submit_button("Salvar Alterações"):
                            
                            prof_att.set_rg_prof(novo_rg if novo_rg != 0 else None)
                            prof_att.set_nome_prof(novo_nome or None)
                            prof_att.set_horario_prof(novo_horario or None)
                            prof_att.set_telefone_prof(novo_telefone if novo_telefone != 0 else None)
                            
                            if alterarProfessor(prof_att):
                                st.success("Professor atualizado!")
                                st.rerun()
                            else:
                                st.error("Erro ao atualizar professor!")
                else:
                    st.warning("Professor não encontrado!")
            else:
                st.info("Nenhum professor cadastrado.")

    if entidade == "Personal":

        operacao = st.sidebar.selectbox("Operações", ["Incluir", "Consultar", "Excluir", "Alterar"])

        if operacao == "Incluir":
            with st.form("form_personal"):
                st.subheader("Cadastrar Personal")
                
                cpf = st.number_input("CPF do Personal:", min_value=1, step=1, format="%d")
                rg_pers = st.number_input("RG do Personal:", min_value=0, step=1, format="%d") or None
                nome_pers = st.text_input("Nome do Personal:") 
                horario_pers = st.text_input("Horario:")
                telefone_pers = st.number_input("Telefone:", min_value=0, step=1, format="%d") or None
                
                if st.form_submit_button("Cadastrar Personal"):
                    if not cpf or not nome_pers or not horario_pers:
                        st.error("Preencha todos os campos obrigatórios (*)")
                    else:
                        try:
                            # CORREÇÃO: Cria o objeto Personal com os dados coletados.
                            personal = Personal(
                                cpf=int(cpf), 
                                rg_pers=rg_pers, 
                                nome_pers=nome_pers, 
                                horario_pers=horario_pers, 
                                telefone_pers=telefone_pers
                            )
                            if incluirPessoa(personal):
                                st.success("Personal cadastrado com sucesso!")
                                st.rerun()
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
            
                cpf = st.number_input("CPF do personal a excluir:", min_value=1, step=1, format="%d")
                if st.button("Excluir"):
                    if excluirPersonal(cpf):
                        st.success("Personal excluído!")
                        st.rerun()
                    else:
                        st.warning("Personal não encontrado.")
            else:
                st.info("Nenhum personal cadastrado.")


        elif operacao == "Alterar":
            pers = consultarPersonal()
            if pers:
                df = pd.DataFrame(pers, columns=["CPF", "RG", "Nome", "Horários", "Telefone"])
                st.dataframe(df, width=1000)
    
                cpf = st.number_input("CPF do personal a alterar:", min_value=1, step=1, format="%d", key="cpf_personal_alterar")
                pers_check = next((p for p in pers if p["CPF"] == cpf), None)
    
                if pers_check:
                    # Cria objeto Personal
                    pers_att = Personal(
                        pers_check["CPF"], 
                        pers_check["RG"], 
                        pers_check["Nome"], 
                        pers_check["Horários"], 
                        pers_check["Telefone"]
                    )
        
                    with st.form(key="alterarPersonal"):
                
                        rg_value = pers_att.get_rg_pers() or 0
                        telefone_value = pers_att.get_telefone_pers() or 0
                
                        novo_rg = st.number_input("RG do Personal:", value=rg_value, min_value=0, format="%d")
                        novo_nome = st.text_input("Informe seu nome:", value=pers_att.get_nome_pers() or "")
                        novo_horario = st.text_input("Horário do Personal:", value=pers_att.get_horario_pers() or "")
                        novo_telefone = st.number_input("Telefone:", value=telefone_value, min_value=0, format="%d")
                
                        if st.form_submit_button("Salvar Alterações"):
                    
                            pers_att.set_rg_pers(novo_rg if novo_rg != 0 else None)
                            pers_att.set_nome_pers(novo_nome or None)
                            pers_att.set_horario_pers(novo_horario or None)
                            pers_att.set_telefone_pers(novo_telefone if novo_telefone != 0 else None)
                            
                            if alterarPersonal(pers_att):
                                st.success("Personal atualizado!")
                                st.rerun()
                            else:
                                st.error("Erro ao atualizar Personal!")
                else:
                    st.warning("Personal não encontrado!")
            else:
                st.info("Nenhum personal cadastrado.")