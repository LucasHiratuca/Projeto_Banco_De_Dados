# Views/Page_Itens.py
import streamlit as st
import pandas as pd
from Controllers.Produto_Controller import *
from Controllers.Maquina_Controller import *
from Models.Produto import Produto
from Models.Maquina import Maquina

def show_itens_page(): # CORREÇÃO: Renomeado de show_relacionamentos_page para show_itens_page
    st.title('Cadastro de Itens e Recursos Físicos')

    relacionamento = st.sidebar.selectbox("Itens", ["Produto", "Maquina"])

    if relacionamento == "Produto":

        operacao = st.sidebar.selectbox("Operações", ["Incluir", "Consultar", "Excluir", "Excluir Específico", "Alterar"])

        if operacao == "Incluir":
            with st.form("form_produto"):
                st.subheader("Cadastrar Produto")
            
                cpf_aluno = st.number_input("CPF do Aluno:", min_value=1, step=1, format="%d")
                id_pr = st.number_input("ID do Produto:", min_value=1, step=1, format="%d") 
                tipo_pr = st.text_input("Tipo do Produto:")
                nome_pr = st.text_input("Nome do Produto:")

                submitted = st.form_submit_button("Cadastrar Produto")
            
                if submitted:
                    if not cpf_aluno or not id_pr or not tipo_pr or not nome_pr:
                        st.error("Preencha todos os campos.")
                    else:
                        try:
                            # CORREÇÃO: Cria o objeto Produto com 4 parâmetros
                            produto = Produto(
                                tipo_pr=tipo_pr,
                                nome_pr=nome_pr,
                                cpf_aluno=int(cpf_aluno),
                                id_pr=int(id_pr)
                            )
                            if incluirProduto(produto):
                                st.success("Produto cadastrado com sucesso!")
                                st.rerun()
                        except Exception as e:
                            st.error(f"Erro ao cadastrar: {e}")


        elif operacao == "Consultar":
            if st.button("Consultar"):
                produtos = consultarProduto()
                if produtos:
                    # CORREÇÃO: Colunas ajustadas
                    df = pd.DataFrame(produtos, columns=["ID do Produto", "Tipo do Produto", "Nome do Produto", "CPF do Aluno"])
                    st.dataframe(df, width=1000)
                else:
                    st.info("Nenhum resultado encontrado. ")

        elif operacao == "Excluir":
            produtos = consultarProduto()
            if produtos:
                df = pd.DataFrame(produtos, columns=["ID do Produto", "Tipo do Produto", "Nome do Produto", "CPF do Aluno"])
                st.dataframe(df, width=1000)
            
                id_pr = st.number_input("ID do produto a excluir:", min_value=1, step=1, format="%d")
                if st.button("Excluir"):
                    if excluirProduto(id_pr): # CORREÇÃO: Excluir por ID_Produto
                        st.success("Produto excluído!")
                        st.rerun()
                    else:
                        st.warning("Produto não encontrado!")
            else:
                st.info("Nenhum relacionamento cadastrado.")


        elif operacao == "Excluir Específico":
            produtos = consultarProduto()
            if produtos:
                df = pd.DataFrame(produtos, columns=["ID do Produto", "Tipo do Produto", "Nome do Produto", "CPF do Aluno"])
                st.dataframe(df, width=1000)
            
                cpf_aluno = st.number_input("CPF do aluno a excluir:", min_value=1, step=1, format="%d")
                id_pr = st.number_input("Id do Produto a excluir:", min_value=1, step=1, format="%d")
                if st.button("Excluir"):
                    if excluirProdutoEsp(id_pr, cpf_aluno): # CORREÇÃO: ID_Produto e CPF_Aluno
                        st.success("Relacionamento excluído!")
                        st.rerun()
                    else:
                        st.warning("Relacionamento não encontrado!")
            else:
                st.info("Nenhum relacionamento cadastrado.")        

        elif operacao == "Alterar":
            produtos = consultarProduto()
            if produtos:
                df = pd.DataFrame(produtos, columns=["ID do Produto", "Tipo do Produto", "Nome do Produto", "CPF do Aluno"])
                st.dataframe(df, width=1000)
    
                old_id = st.number_input("ID do Produto a alterar:", min_value=1, step=1, key="id_produto_alterar")
                
                produto_check = next((p for p in produtos if p["ID do Produto"] == old_id), None)
    
                if produto_check:
                    # Cria objeto Produto
                    produto_att = Produto(
                        tipo_pr=produto_check["Tipo do Produto"],
                        nome_pr=produto_check["Nome do Produto"],
                        cpf_aluno=produto_check["CPF do Aluno"],
                        id_pr=produto_check["ID do Produto"]
                    )
        
                    with st.form(key="alterarProduto"): 
                                    
                        novo_id = st.number_input("Novo ID do Produto:", value=produto_att.get_id_pr(), min_value=1)
                        novo_tipo = st.text_input("Novo Tipo do Produto:", value=produto_att.get_tipo_pr())
                        novo_nome = st.text_input("Novo Nome do Produto:", value=produto_att.get_nome_pr())
                        novo_cpf_aluno = st.number_input("Novo CPF do Aluno:", value=produto_att.get_cpf_aluno(), min_value=1)
                        
                        if st.form_submit_button("Salvar Alterações"):
                    
                            produto_att.set_id_pr(novo_id)
                            produto_att.set_tipo_pr(novo_tipo)
                            produto_att.set_nome_pr(novo_nome)
                            produto_att.set_cpf_aluno(novo_cpf_aluno)
                            
                            # Chama a função de alteração com o ID antigo
                            if alterarProduto(produto_att, old_id):
                                st.success("Produto atualizado!")
                                st.rerun()
                            else:
                                st.error("Erro ao atualizar produto!")
                else:
                    st.warning("Produto não encontrado!")
            else:
                st.info("Nenhum relacionamento cadastrado.")
    

    if relacionamento == "Maquina":

        operacao = st.sidebar.selectbox("Operações", ["Incluir", "Consultar", "Excluir", "Alterar"])

        if operacao == "Incluir":
            with st.form("form_maquina"):
                st.subheader("Cadastrar Máquina")
                # A Maquina precisa de 3 parâmetros: nome, id_mqn, parte_trabalhada
                nome_mqn = st.text_input("Nome da Máquina:") 
                id_mqn = st.number_input("ID da Maquina:", min_value=1, step=1, format="%d")
                parte_trabalhada = st.text_input("Parte do corpo trabalhada:")
            
                submitted = st.form_submit_button("Cadastrar Máquina")
            
                if submitted:
                    if not nome_mqn or not id_mqn or not parte_trabalhada:
                        st.error("Preencha todos os campos.")
                    else:
                        try:
                            # CORREÇÃO: Cria o objeto Maquina com 3 parâmetros
                            maquina = Maquina(
                                nome_mqn=nome_mqn,
                                id_mqn=int(id_mqn),
                                parte_trabalhada=parte_trabalhada
                            )
                            if incluirMaquina(maquina):
                                st.success("Máquina cadastrada com sucesso!")
                                st.rerun()
                        except Exception as e:
                            st.error(f"Erro ao cadastrar: {e}")


        elif operacao == "Consultar":
            if st.button("Consultar"):
                maquinas = consultarMaquina()
                if maquinas:
                    # CORREÇÃO: Colunas ajustadas
                    df = pd.DataFrame(maquinas, columns=["Nome da Maquina", "ID da Maquina", "Parte Trabalhada"])
                    st.dataframe(df, width=1000)
                else:
                    st.info("Nenhum resultado encontrado. ") 

        elif operacao == "Excluir":
            maquinas = consultarMaquina()
            if maquinas:
                df = pd.DataFrame(maquinas, columns=["Nome da Maquina", "ID da Maquina", "Parte Trabalhada"])
                st.dataframe(df, width=1000)
            
                nome_mqn = st.text_input("Nome da Maquina a excluir:")

                if st.button("Excluir"):
                    if excluirMaquina(nome_mqn): # CORREÇÃO: Excluir pelo Nome
                        st.success("Máquina excluída!")
                        st.rerun()
                    else:
                        st.warning("Máquina não encontrada!")
            else:
                st.info("Nenhum relacionamento cadastrado.")


        elif operacao == "Alterar":
            maquinas = consultarMaquina()
            if maquinas:
                df = pd.DataFrame(maquinas, columns=["Nome da Maquina", "ID da Maquina", "Parte Trabalhada"])
                st.dataframe(df, width=1000)
    
                old_nome = st.text_input("Nome da Maquina a alterar:", key="nome_maquina_alterar")
                
                maquina_check = next((m for m in maquinas if m["Nome da Maquina"] == old_nome), None)
    
                if maquina_check:
                    # Cria objeto Maquina
                    maquina_att = Maquina(
                        nome_mqn=maquina_check["Nome da Maquina"],
                        id_mqn=maquina_check["ID da Maquina"],
                        parte_trabalhada=maquina_check["Parte Trabalhada"]
                    )
        
                    with st.form(key="alterarMaquina"):
                                    
                        novo_id = st.number_input("Novo ID da Maquina:", value=maquina_att.id_mqn, min_value=1)
                        nova_parte = st.text_input("Nova Parte Trabalhada:", value=maquina_att.parte_trabalhada)
                        
                        if st.form_submit_button("Salvar Alterações"):
                    
                            maquina_att.id_mqn = novo_id
                            maquina_att.parte_trabalhada = nova_parte
                            
                            # Chama a função de alteração
                            if alterarMaquina(maquina_att):
                                st.success("Máquina atualizada!")
                                st.rerun()
                            else:
                                st.error("Erro ao atualizar máquina!")
                else:
                    st.warning("Máquina não encontrada!")
            else:
                st.info("Nenhuma máquina cadastrada.")