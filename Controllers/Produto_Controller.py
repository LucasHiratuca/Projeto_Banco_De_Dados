# Controllers/Produto_Controller.py
import sqlite3
from Models.Produto import Produto

def conectaBD():
    conexao = sqlite3.connect("Academia.db")
    return conexao

def incluirProduto(produto): # CORREÇÃO: Recebe o objeto
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
            INSERT INTO Produto (ID_Produto, Tipo_Produto, Nome_Produto, CPF_Aluno)
            VALUES (?, ?, ?, ?) 
            """, (
                produto.get_id_pr(),
                produto.get_tipo_pr(),
                produto.get_nome_pr(),
                produto.get_cpf_aluno()
            )) 
        conexao.commit()
        print("Produto inserido com sucesso!")
        return True
    except sqlite3.IntegrityError as e: # Trata erros de chave primária/FK
        print(f"ERRO DE INTEGRIDADE ao inserir produto: O ID ou CPF do Aluno ja existe/e invalido. Detalhe: {e}")
        return False
    except sqlite3.Error as e: # Trata outros erros, incluindo o 'unrecognized token'
        print(f"Erro ao inserir produto: {e}")
        return False
    finally:
        conexao.close()

def consultarProduto():
    conexao = conectaBD()
    cursor = conexao.cursor()
    
    try:
        cursor.execute('SELECT * FROM Produto')
        rows = cursor.fetchall()
        
        dados = []
        
        for row in rows:
            # Colunas da tabela Produto: ID_Produto, Tipo_Produto, Nome_Produto, CPF_Aluno
            ID_Produto, Tipo_Produto, Nome_Produto, CPF_Aluno = row
            
            dados.append({
                "ID do Produto": ID_Produto,
                "Tipo do Produto": Tipo_Produto,
                "Nome do Produto": Nome_Produto,
                "CPF do Aluno": CPF_Aluno
            })
        
        return dados
    
    except sqlite3.Error as e:
        print(f"Erro ao consultar o relacionamento: {e}")
        return []
    
    finally:
        conexao.close()
    

def excluirProduto(ID_Produto):
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM Produto WHERE ID_Produto = ?", (ID_Produto,))
        linhas_afetadas = cursor.rowcount
        conexao.commit()
        if linhas_afetadas > 0:
            print(f"Produto com ID {ID_Produto} excluído com sucesso!")
            return True
        else:
            print(f"Nenhum produto encontrado com ID {ID_Produto}.")
            return False
    except sqlite3.Error as e:
        print(f"Erro ao excluir relacionamento: {e}")
        return False
    finally:
        if conexao:
            conexao.close()

def excluirProdutoEsp(ID_Produto, CPF_Aluno):
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM Produto WHERE ID_Produto = ? AND CPF_Aluno = ?", (ID_Produto, CPF_Aluno))
        linhas_afetadas = cursor.rowcount
        conexao.commit()
        if linhas_afetadas > 0:
            print(f"Relacionamento com CPF {CPF_Aluno} e ID do Produto {ID_Produto} excluído com sucesso!")
            return True
        else:
            print(f"Relacionamento com CPF {CPF_Aluno} e ID do Produto {ID_Produto} não encontrado.")
            return False
    except sqlite3.Error as e:
        print(f"Erro ao excluir relacionamento: {e}")
        return False
    finally:
        if conexao:
            conexao.close()

def alterarProduto(produto, old_id_produto):
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()
        cursor.execute('''
            UPDATE Produto
            SET ID_Produto = ?, Tipo_Produto = ?, Nome_Produto = ?, CPF_Aluno = ?
            WHERE ID_Produto = ? 
        ''', (
            produto.get_id_pr(),
            produto.get_tipo_pr(),
            produto.get_nome_pr(),
            produto.get_cpf_aluno(),
            old_id_produto
        ))
        conexao.commit()
        print(f"Produto com ID {produto.get_id_pr()} alterado com sucesso!")
        return True
    except sqlite3.Error as e:
        print(f"Erro ao alterar relacionamento: {e}")
        return False
    finally:
        if conexao:
            conexao.close()