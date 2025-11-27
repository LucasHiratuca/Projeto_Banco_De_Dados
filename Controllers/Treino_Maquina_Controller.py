# Controllers/Treino_Maquina_Controller.py
import sqlite3
from Models.Treino_Maquina import Treino_Maquina

def conectaBD():
    conexao = sqlite3.connect("Academia.db")
    return conexao

def incluirTreinoMaquina(treino_maquina): # CORREÇÃO: Recebe o objeto
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
            INSERT INTO Treino_Maquina (ID_Treino, Nome_Maquina)
            VALUES (?, ?)
            """, (
                treino_maquina.id_tr, # CORREÇÃO: Acessa a propriedade
                treino_maquina.nome_mqn
            )) 
        conexao.commit()
        print("Dados inseridos com sucesso!")
        return True
    except sqlite3.Error as e:
        print(f"Erro ao inserir dados: {e}")
        return False
    finally:
        conexao.close()

def consultarTreinoMaquina():
    conexao = conectaBD()
    cursor = conexao.cursor()
    
    try:
        cursor.execute('SELECT * FROM Treino_Maquina') # CORREÇÃO: Tabela Treino_Maquina
        rows = cursor.fetchall()
        
        # Lista para armazenar os dados
        dados = []
        
        for row in rows:
            # CORREÇÃO: Desempacotar (ID_Treino, Nome_Maquina)
            ID_Treino, Nome_Maquina = row
            
            # Adiciona os dados à lista
            dados.append({
                "ID do Treino": ID_Treino,
                "Nome da Maquina": Nome_Maquina
            })
        
        return dados
    
    except sqlite3.Error as e:
        print(f"Erro ao consultar o relacionamento: {e}")
        return []
    
    finally:
        conexao.close()
    

def excluirTreinoMaquina(ID_Treino):
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM Treino_Maquina WHERE ID_Treino = ?", (ID_Treino,)) # CORREÇÃO: Tupla
        linhas_afetadas = cursor.rowcount
        conexao.commit()
        if linhas_afetadas > 0:
            print(f"Relacionamento(s) com ID_Treino {ID_Treino} excluído com sucesso!")
            return True
        else:
            print(f"Nenhum relacionamento encontrado com ID_Treino {ID_Treino}.")
            return False
    except sqlite3.Error as e:
        print(f"Erro ao excluir relacionamento: {e}")
        return False
    finally:
        if conexao:
            conexao.close()

def excluirTreinoMaquinaEsp(ID_Treino, Nome_Maquina): # CORREÇÃO: Nome_Maquina como parâmetro
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()
        # CORREÇÃO: Tabela Treino_Maquina e Nome_Maquina
        cursor.execute("DELETE FROM Treino_Maquina WHERE ID_Treino = ? AND Nome_Maquina = ?", (ID_Treino, Nome_Maquina))
        linhas_afetadas = cursor.rowcount
        conexao.commit()
        if linhas_afetadas > 0:
            print(f"Relacionamento com ID_Treino {ID_Treino} e Nome da Maquina {Nome_Maquina} excluído com sucesso!")
            return True
        else:
            print(f"Relacionamento com ID_Treino {ID_Treino} e Nome da Maquina {Nome_Maquina} não encontrado.")
            return False
    except sqlite3.Error as e:
        print(f"Erro ao excluir relacionamento: {e}")
        return False
    finally:
        if conexao:
            conexao.close()

def alterarTreinoMaquina(treino_maquina, old_nome_maquina): # CORREÇÃO: Recebe o objeto e o nome antigo para WHERE
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()
        # Atualizar a máquina com base no ID_Treino e no Nome_Maquina antigo
        cursor.execute('''
            UPDATE Treino_Maquina
            SET ID_Treino = ?, Nome_Maquina = ?
            WHERE ID_Treino = ? AND Nome_Maquina = ?
        ''', (
            treino_maquina.id_tr,
            treino_maquina.nome_mqn,
            treino_maquina.id_tr, # Chave 1
            old_nome_maquina # Chave 2 (Nome antigo)
        ))
        conexao.commit()
        print(f"Relacionamento com ID_Treino {treino_maquina.id_tr} alterado com sucesso!")
        return True
    except sqlite3.Error as e:
        print(f"Erro ao alterar relacionamento: {e}")
        return False
    finally:
        if conexao:
            conexao.close()