import sqlite3
from Models.Treino import Treino

def conectaBD():
    conexao = sqlite3.connect("Academia.db")
    return conexao

def incluirTreino():
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
            INSERT INTO Treino ( ID_Treino,  Alongamentos,   Exercicios_Aerobicos, Exercicios_Maquina ,Carga , CPF_Aluno)
            VALUES (?, ?)
            """, (
               Treino.id 
               Treino.alongamentos
               Treino.exercicios_mqn 
               Treino.exercicios_arbcs
               Treino.carga_mqn 
               Treino.cpf_aluno 
            )) 
        conexao.commit()
        print("Treino inserido com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao inserir treino: {e}")
    finally:
        conexao.close()

def consultarTreino():
    conexao = conectaBD()
    cursor = conexao.cursor()
    
    try:
        cursor.execute('SELECT * FROM Treino)
        rows = cursor.fetchall()
        
        # Lista para armazenar os dados do relacionamento
        dados = []
        
        for row in rows:
            ID_Aula, CPF_Aluno = row
            
            # Adiciona os dados à lista
            dados.append({
                "ID do Treino": ID_Treino,
                "CPF do Aluno": CPF_Aluno
            })
        
        return dados
    
    except sqlite3.Error as e:
        print(f"Erro ao consultar o relacionamento: {e}")
        return []
    
    finally:
        conexao.close()
    

def excluirTreino(CPF_Aluno):
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM Treino WHERE ID_Treino = ?", CPF_Aluno,)
        conexao.commit()
        print(f"Relacionamento com {CPF_Aluno,} excluído com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao excluir relacionamento: {e}")
    finally:
        if conexao:
            conexao.close()

def excluirTreinoEsp(ID_Treino, CPF_Aluno):
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM Treino WHERE ID_Treino = ? AND CPF_Aluno = ?", ID_Treino, CPF_Aluno)
        conexao.commit()
        print(f"Relacionamento com {CPF_Aluno,} e {ID_Treino} excluído com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao excluir relacionamento: {e}")
    finally:
        if conexao:
            conexao.close()

def alterarTreino(Treino):
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()
        cursor.execute('''
            UPDATE Treino
            SET ID_Treino = ?, CPF_Aluno = ?
            WHERE CPF_Aluno = ? 
        ''', (
            Treino["ID_Treino"],
            Treino["CPF_Aluno"],
            Treino("CPF_Aluno")
        ))
        conexao.commit()
        print(f"Relacionamento com {Treino['CPF_Aluno']} alterado com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao alterar relacionamento: {e}")
    finally:
        if conexao:
            conexao.close()