# Controllers/Plano.py
import sqlite3
from Models.Plano import Plano

def conectaBD():
    conexao = sqlite3.connect("Academia.db")
    return conexao

def incluirPlano():
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
            INSERT INTO Plano (Tipo_Plano, ID_Plano)
            VALUES (?, ?)
            """, (
                Plano.tipo_plano(),
                Plano.id_plano()
            )) 
        conexao.commit()
        print("Dados inseridos com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao inserir dados: {e}")
    finally:
        conexao.close()

def consultarPlano():
    conexao = conectaBD()
    cursor = conexao.cursor()
    
    try:
        cursor.execute('SELECT * FROM Plano')
        rows = cursor.fetchall()
        
        # Lista para armazenar os dados do relacionamento
        dados = []
        
        for row in rows:
            Tipo_Plano, ID_Plano = row
            
            # Adiciona os dados à lista
            dados.append({
                "Tipo do Plano: ": Tipo_Plano,
                "ID do Plano: ": ID_Plano
            })
        
        return dados
    
    except sqlite3.Error as e:
        print(f"Erro ao consultar os Planos: {e}")
        return []
    
    finally:
        conexao.close()
    

def excluirPlano(Tipo_Plano):
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM Plano WHERE Tipo_Plano = ?", Tipo_Plano)
        conexao.commit()
        print(f"Relacionamento com {Tipo_Plano} excluído com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao excluir plano: {e}")
    finally:
        if conexao:
            conexao.close()

def alterarPlano(Plano):
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()
        cursor.execute('''
            UPDATE Treino_Maquina
            SET ID_Treino = ?, Nome_Maquina = ?
            WHERE ID_Treino = ?
        ''', (
            Plano["Tipo_Plano"],
            Plano["ID_Plano"],
            
        ))
        conexao.commit()
        print(f"Tabela com {Plano['Tipo_Treino']} alterado com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao alterar Plano: {e}")
    finally:
        if conexao:
            conexao.close()