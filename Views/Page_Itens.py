import streamlit as st
import pandas as pd
from Controllers.Produto_Controller import *
from Controllers.Maquina_Controller import *

def show_relacionamentos_page():
    st.title('Cadastro de Relacionamentos')

    relacionamento = st.sidebar.selectbox("Relacionamentos", ["Produto", "Maquina"])

    if relacionamento == "Produto":

        operacao = st.sidebar.selectbox("Operações", ["Incluir", "Consultar", "Excluir", "Excluir Específico", "Alterar"])

        if operacao == "Incluir":
            Produto = Produto(0, 0)
        
            Produto.cpf_aluno = st.number_input("CPF do Aluno: ")
            Produto.id_pr = st.number_input("ID do Produto: ") 
        
        if st.button("Cadastrar"):
            incluirProduto(Produto)
            st.success("Produto cadastrado na aula com sucesso!")

        elif operacao == "Consultar":
            if st.button("Consultar"):
                Produto = consultarProduto()
                if Produto:
                    df = pd.DataFrame(Produto, columns=["CPF", "ID do Produto"])
                    st.dataframe(df, width=1000)
                else:
                    st.info("Nenhum resultado encontrado. ")

        elif operacao == "Excluir":
            Produto = consultarProduto()
            if Produto:
                df = pd.DataFrame(Produto, columns=["CPF", "ID do Produto"])
                st.dataframe(df, width=1000)
            
                cpf = st.number_input("CPF do aluno a excluir:", min_value=1)
                if st.button("Excluir"):
                    excluirProduto(cpf)
                    st.success("Relacionamento excluído!")
                    st.rerun()
                else:
                    st.info("Não foi possível achar o relacionamento")
            else:
                st.info("Nenhum relacionamento cadastrado.")


        elif operacao == "Excluir Específico":
            Produto = consultarProduto()
            if Produto:
                df = pd.DataFrame(Produto, columns=["CPF", "ID do Produto"])
                st.dataframe(df, width=1000)
            
                cpf = st.number_input("CPF do aluno a excluir:", min_value=1)
                id = st.number_input("Id do Produto a excluir:", min_value = 1)
                if st.button("Excluir"):
                    excluirProdutoEsp(id_pr, cpf)
                    st.success("Relacionamento excluído!")
                    st.rerun()
                else:
                    st.info("Não foi possível achar o relacionamento")
            else:
                st.info("Nenhum relacionamento cadastrado.")        

        elif operacao == "Alterar":
            Produto = consultarProduto()
            if Produto:
                df = pd.DataFrame(Produto, columns=["CPF", "ID do Produto"])
                st.dataframe(df, width=1000)
    
                cpf = st.number_input("CPF do aluno com relacionamento a alterar:", min_value=1, key="cpf_aluno_alterar")
                aluno_check = next((a for a in Produto if a[1] == cpf), None)
    
                if aluno_check:
                    Produto_att = Produto(*aluno_check[:2])
        
                    with st.form(key="alterarAluno"):
                                    
                
                        novo_id = st.number_input("ID do Produto:", value=Produto_att.id_pr, min_value=0)
                        novo_cpf = st.number_input("Informe o cpf:", value=Produto_att.cpf_aluno, min_value=0)
                        
                        if st.form_submit_button("Salvar Alterações"):
                    
                            Produto_att.id_aula(novo_id if novo_id != 0 else None)
                            Produto_att.cpf_aluno(novo_cpf if novo_cpf != 0 else None)
                            
                    
                            alterarProduto(Produto_att)
                            st.success("Relacionamento atualizado!")
                            st.rerun()
                else:
                    st.warning("Relacionamento não encontrado!")
            else:
                st.info("Nenhum relacionamento cadastrado.")
    

    if relacionamento == "Maquina":

        operacao = st.sidebar.selectbox("Operações", ["Incluir", "Consultar", "Excluir", "Excluir Específico", "Alterar"])

        if operacao == "Incluir":
            Maquina = Maquina(0, "")
        
            Maquina.id_mqn = st.number_input("ID da Maquina: ")
            Maquina.nome_mqn = st.text_input("Nome da Máquina: ") 
        
        if st.button("Cadastrar"):
            incluirMaquina(Maquina)
            st.success("Relacionamento cadastrado com sucesso!")


        elif operacao == "Consultar":
            if st.button("Consultar"):
                Maquina = consultarMaquina()
                if Maquina:
                    df = pd.DataFrame(Maquina, columns=["ID da Maquina", "Nome da Maquina"])
                    st.dataframe(df, width=1000)
                else:
                    st.info("Nenhum resultado encontrado. ") 

        elif operacao == "Excluir":
            Maquina = consultarMaquina()
            if Maquina:
                df = pd.DataFrame(Maquina, columns=["ID da Maquina", "Nome da Maquina"])
                st.dataframe(df, width=1000)
            
                id = st.number_input("ID da Maquina a excluir:", min_value=1)

                if st.button("Excluir"):
                    excluirMaquina(id)
                    st.success("Relacionamento excluído!")
                    st.rerun()
                else:
                    st.info("Não foi possível achar o relacionamento")
            else:
                st.info("Nenhum relacionamento cadastrado.")


        elif operacao == "Excluir Específico":
            Maquina = consultarMaquina()
            if Maquina:
                df = pd.DataFrame(Maquina, columns=["ID da Maquina", "Nome da Maquina"])
                st.dataframe(df, width=1000)
            
                maquina = st.text_input("Nome da Maquina a excluir:", min_value=1)
                id = st.number_input("ID do Produto a excluir:", min_value = 1)
                if st.button("Excluir"):
                    excluirMaquinaEsp(id, maquina)
                    st.success("Relacionamento excluído!")
                    st.rerun()
                else:
                    st.info("Não foi possível achar o relacionamento")
            else:
                st.info("Nenhum relacionamento cadastrado.")        

        elif operacao == "Alterar":
            Maquina = consultarMaquina()
            if Maquina:
                df = pd.DataFrame(Maquina, columns=["ID da Maquina", "Nome da Maquina"])
                st.dataframe(df, width=1000)
    
                id = st.number_input("ID da Maquina com relacionamento a alterar:", min_value=1, key="id_maquina_alterar")
                Maquina_check = next((t for t in Maquina if t[0] == id), None)
    
                if Maquina_check:
                    Maquina_att = Maquina(*Maquina_check[:2])
        
                    with st.form(key="alterarMaquina"):
                                    
                
                        novo_id = st.number_input("ID da Maquina", value=Maquina_att.id_mqn, min_value=0)
                        nova_maquina = st.text_input("Informe o nome da maquina:", value=Maquina_att.nome_mqn, min_value=0)
                        
                        if st.form_submit_button("Salvar Alterações"):
                    
                            Maquina_att.id_mqn(novo_id if novo_id != 0 else None)
                            Maquina_att.nome_mqn(nova_maquina if novo_cpf != 0 else None)
                            
                    
                            alterarMaquina(Maquina_att)
                            st.success("Relacionamento atualizado!")
                            st.rerun()
                else:
                    st.warning("Relacionamento não encontrado!")
            else:
                st.info("Nenhum relacionamento cadastrado.")