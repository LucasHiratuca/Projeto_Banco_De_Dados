# Controllers/Treino-Maquina.py
import sqlite3
from Models.Treino_Maquina import Treino_Maquina

def conectaBD():
    conexao = sqlite3.connect("Academia.db")
    return conexao

def incluirTreinoMaquina():
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
            INSERT INTO Treino_Maquina (ID_Treino, Nome_Maquina)
            VALUES (?, ?)
            """, (
                Treino_Maquina.id_tr(),
                Treino_Maquina.nome_mqn()
            )) 
        conexao.commit()
        print("Dados inseridos com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao inserir dados: {e}")
    finally:
        conexao.close()

def consultarTreinoMaquina():
    conexao = conectaBD()
    cursor = conexao.cursor()
    
    try:
        cursor.execute('SELECT * FROM Treino_Tabela')
        rows = cursor.fetchall()
        
        # Lista para armazenar os dados do relacionamento
        dados = []
        
        for row in rows:
            ID_Maquina, Nome_Maquina = row
            
            # Adiciona os dados à lista
            dados.append({
                "ID da Maquina": ID_Maquina,
                "Nome da Maquina": Nome_Maquina
            })
        
        return dados
    
    except sqlite3.Error as e:
        print(f"Erro ao consultar funcionários: {e}")
        return []
    
    finally:
        conexao.close()
    

def excluirTreinoMaquina(ID_Treino):
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM Treino_Maquina WHERE ID_Treino = ?", (ID_Treino))
        conexao.commit()
        print(f"Relacionamento com {ID_Treino} excluído com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao excluir relacionamento: {e}")
    finally:
        if conexao:
            conexao.close()

def excluirTreinoMaquinaEsp(ID_Treino, ID_Maquina):
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM Aluno_Aula WHERE ID_Treino = ? AND ID_Maquina = ?", ID_Treino, ID_Maquina)
        conexao.commit()
        print(f"Relacionamento com {ID_Treino} e {ID_Maquina} excluído com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao excluir relacionamento: {e}")
    finally:
        if conexao:
            conexao.close()

def alterarTreinoMaquina(Treino_Maquina):
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()
        cursor.execute('''
            UPDATE Treino_Maquina
            SET ID_Treino = ?, Nome_Maquina = ?
            WHERE ID_Treino = ?
        ''', (
            Treino_Maquina["ID_Treino"],
            Treino_Maquina["Nome-Maquina"],
            Treino_Maquina("ID_Treino")
        ))
        conexao.commit()
        print(f"Relacionamento com {Treino_Maquina['ID_Treino']} alterado com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao alterar relacionamento: {e}")
    finally:
        if conexao:
            conexao.close()