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
        
            aluno.cpf_aluno = st.number_input("CPF do Aluno: ")
            aluno.rg_aluno = st.number_input("Rg do Aluno: ")
            aluno.telefone_aluno = st.number_input("Informe seu número: ")
            aluno.objetivo_treino = st.text_input_("Nome do Aluno: ")
            aluno.tipo_plano = st.text_input_("Nome do Aluno: ")
            aluno.nome_aluno = st.text_input_("Nome do Aluno: ")
            aluno.cpf_pers = st.number_input("CPF do Personal: ")
            
        
        if st.button("Cadastrar"):
            incluir_produto(produto)
            st.success("Produto cadastrado com sucesso!")

    elif operacao == "Consultar":
        if st.button("Consultar"):
            produtos = consultar_produtos()
            if produtos:
                df = pd.DataFrame(produtos, columns=["Código", "Descrição", "Quantidade", "Valor Unitário", "Valor Total"])
                st.dataframe(df, width=1000)
            else:
                st.info("Nenhum produto cadastrado.")

    elif operacao == "Excluir":
        produtos = consultar_produtos()
        if produtos:
            df = pd.DataFrame(produtos, columns=["Código", "Descrição", "Quantidade", "Valor Unitário", "Valor Total"])
            st.dataframe(df)
            
            codigo = st.number_input("Código do produto a excluir:", min_value=1)
            if st.button("Excluir"):
                excluir_produto(codigo)
                st.success("Produto excluído!")
                st.rerun()
        else:
            st.info("Nenhum produto cadastrado.")

    elif operacao == "Alterar":
        produtos = consultar_produtos()
        if produtos:
            df = pd.DataFrame(produtos, columns=["Código", "Descrição", "Quantidade", "Valor Unitário", "Valor Total"])
            st.dataframe(df)
            
            codigo = st.number_input("Código do produto a alterar:", min_value=1)
            produto_data = next((p for p in produtos if p[0] == codigo), None)
            
            if produto_data:
                produto = Produto(*produto_data[:4])
                
                with st.form(key="altera_produto"):
                    produto.set_descricao(st.text_input("Descrição:", value=produto.get_descricao()))
                    produto.set_qtd(st.number_input("Quantidade:", min_value=0, value=produto.get_qtd()))
                    produto.set_valor_unitario(st.number_input("Valor Unitário (R$):", 
                                                             min_value=0.0, 
                                                             format="%.2f", 
                                                             value=produto.get_valor_unitario()))
                    
                    st.write(f"**Valor Total:** R$ {produto.calcular_valor_total():.2f}")
                    
                    if st.form_submit_button("Salvar Alterações"):
                        alterar_produto(produto)
                        st.success("Produto atualizado!")
                        st.rerun()
            else:
                st.warning("Produto não encontrado!")
        else:
            st.info("Nenhum produto cadastrado.")