# Controllers/Maquina_Controller.py
import sqlite3
from Models.Maquina import Maquina

def conectaBD():
    conexao = sqlite3.connect("Academia.db")
    return conexao

def incluirMaquina(maquina):
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        # Usando Maquina (PascalCase)
        cursor.execute("""
            INSERT INTO Maquina (Nome_Maquina, ID_Maquina, Parte_Trabalhada)
            VALUES (?, ?, ?)
            """, (
                maquina.nome, 
                maquina.id_mqn, 
                maquina.parte_trabalhada
            )) 
        conexao.commit()
        print("Maquina inserida com sucesso!")
        return True
    except sqlite3.IntegrityError as e:
        print(f"ERRO DE INTEGRIDADE ao inserir maquina: O ID ou Nome da Maquina ja existe. Detalhe: {e}")
        return False
    except sqlite3.Error as e:
        print(f"Erro ao inserir maquina: {e}")
        return False
    finally:
        conexao.close()

def consultarMaquina():
    conexao = conectaBD()
    cursor = conexao.cursor()
    
    try:
        cursor.execute('SELECT * FROM Maquina')
        rows = cursor.fetchall()
        
        dados = []
        
        for row in rows:
            Nome_Maquina, ID_Maquina, Parte_Trabalhada = row
            
            dados.append({
                "Nome da Maquina": Nome_Maquina,
                "ID da Maquina": ID_Maquina,
                "Parte Trabalhada": Parte_Trabalhada
            })
        
        return dados
    
    except sqlite3.Error as e:
        print(f"Erro ao consultar as Maquinas: {e}")
        return []
    
    finally:
        conexao.close()
    

def excluirMaquina(Nome_Maquina):
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM Maquina WHERE Nome_Maquina = ?", (Nome_Maquina,))
        linhas_afetadas = cursor.rowcount
        conexao.commit()
        if linhas_afetadas > 0:
            print(f"Maquina com nome {Nome_Maquina} excluída com sucesso!")
            return True
        else:
            print(f"Nenhuma maquina encontrada com nome {Nome_Maquina}.")
            return False
    except sqlite3.Error as e:
        print(f"Erro ao excluir maquina: {e}")
        return False
    finally:
        if conexao:
            conexao.close()
            
def excluirMaquinaEsp(Nome_Maquina, ID_Maquina):
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM Maquina WHERE Nome_Maquina = ? AND ID_Maquina = ?", (Nome_Maquina, ID_Maquina))
        linhas_afetadas = cursor.rowcount
        conexao.commit()
        if linhas_afetadas > 0:
            print(f"Maquina com nome {Nome_Maquina} e ID {ID_Maquina} excluída com sucesso!")
            return True
        else:
            print(f"Maquina com nome {Nome_Maquina} e ID {ID_Maquina} não encontrada.")
            return False
    except sqlite3.Error as e:
        print(f"Erro ao excluir relacionamento: {e}")
        return False
    finally:
        if conexao:
            conexao.close()

def alterarMaquina(maquina, old_nome_maquina):
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()
        cursor.execute('''
            UPDATE Maquina
            SET Nome_Maquina = ?, ID_Maquina = ?, Parte_Trabalhada = ?
            WHERE Nome_Maquina = ?
        ''', (
            maquina.nome, 
            maquina.id_mqn, 
            maquina.parte_trabalhada,
            old_nome_maquina 
        ))
        conexao.commit()
        print(f"Maquina {maquina.nome} alterada com sucesso!")
        return True
    except sqlite3.Error as e:
        print(f"Erro ao alterar Maquina: {e}")
        return False
    finally:
        if conexao:
            conexao.close()