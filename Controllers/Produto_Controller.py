# Controllers/Treino-Maquina.py
import sqlite3
from Models.Produto import Produto

def conectaBD():
    conexao = sqlite3.connect("Academia.db")
    return conexao

def incluirProduto():
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
            INSERT INTO Produto (ID_Produto,  Tipo_Produto,  Nome_Produto, CPF_Aluno)
            VALUES (?, ?)
            """, (
                Produto.id_pr(),
                Produto.tipo_pr(),
                Produto.nome_pr(),
                Produto.cpf_aluno()
            )) 
        conexao.commit()
        print("Produto inserido com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao inserir produto: {e}")
    finally:
        conexao.close()

def consultarProduto():
    conexao = conectaBD()
    cursor = conexao.cursor()
    
    try:
        cursor.execute('SELECT * FROM Produto')
        rows = cursor.fetchall()
        
        # Lista para armazenar os dados do relacionamento
        dados = []
        
        for row in rows:
            ID_Produto, CPF_Aluno = row
            
            # Adiciona os dados à lista
            dados.append({
                "ID do Produto": ID_Produto,
                "CPF do Aluno": CPF_Aluno
            })
        
        return dados
    
    except sqlite3.Error as e:
        print(f"Erro ao consultar o relacionamento: {e}")
        return []
    
    finally:
        conexao.close()
    

def excluirProduto(CPF_Aluno):
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM Produto WHERE ID_Produto = ?", CPF_Aluno,)
        conexao.commit()
        print(f"Relacionamento com {CPF_Aluno,} excluído com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao excluir relacionamento: {e}")
    finally:
        if conexao:
            conexao.close()

def excluirProdutoEsp(ID_Produto, CPF_Aluno):
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM Produto WHERE ID_Produto = ? AND CPF_Aluno = ?", ID_Produto, CPF_Aluno)
        conexao.commit()
        print(f"Relacionamento com {CPF_Aluno,} e {ID_Produto} excluído com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao excluir relacionamento: {e}")
    finally:
        if conexao:
            conexao.close()

def alterarProduto(Produto):
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()
        cursor.execute('''
            UPDATE Produto
            SET ID_Produto = ?, CPF_Aluno = ?
            WHERE CPF_Aluno = ? 
        ''', (
            Produto["ID_Produto"],
            Produto["CPF_Aluno"],
            Produto("CPF_Aluno")
        ))
        conexao.commit()
        print(f"Relacionamento com {Produto['CPF_Aluno']} alterado com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao alterar relacionamento: {e}")
    finally:
        if conexao:
            conexao.close()