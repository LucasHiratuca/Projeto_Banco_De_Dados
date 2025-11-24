# COntrollers/Aluno_Aula_Controller.py

import sqlite3
from Models.Aluno_Aula import Aluno_Aula

def conectaBD():
    conexao = sqlite3.connect("Academia.db")
    return conexao

def incluirAlunoAula():
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
            INSERT INTO Aluno_Aula (ID_Aula, CPF_Aluno)
            VALUES (?, ?)
            """, (
                Aluno_Aula.id_aula(),
                Aluno_Aula.cpf_aluno()
            )) 
        conexao.commit()
        print("Dados inseridos com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao inserir dados: {e}")
    finally:
        conexao.close()

def consultarAlunoAula():
    conexao = conectaBD()
    cursor = conexao.cursor()
    
    try:
        cursor.execute('SELECT * FROM Aluno_Aula')
        rows = cursor.fetchall()
        
        # Lista para armazenar os dados do relacionamento
        dados = []
        
        for row in rows:
            ID_Aula, CPF_Aluno = row
            
            # Adiciona os dados à lista
            dados.append({
                "ID da Aula": ID_Aula,
                "CPF do Aluno": CPF_Aluno
            })
        
        return dados
    
    except sqlite3.Error as e:
        print(f"Erro ao consultar o relacionamento: {e}")
        return []
    
    finally:
        conexao.close()
    

def excluirAlunoAula(CPF_Aluno):
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM Aluno_Aula WHERE ID_Treino = ?", CPF_Aluno)
        conexao.commit()
        print(f"Relacionamento com {CPF_Aluno} excluído com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao excluir relacionamento: {e}")
    finally:
        if conexao:
            conexao.close()

def excluirAlunoAulaEsp(ID_Aula, CPF_Aluno):
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM Aluno_Aula WHERE ID_Aula = ? AND CPF_Aluno = ?", ID_Aula, CPF_Aluno)
        conexao.commit()
        print(f"Relacionamento com {CPF_Aluno} e {ID_Aula} excluído com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao excluir relacionamento: {e}")
    finally:
        if conexao:
            conexao.close()

def alterarAlunoAula(Aluno_Aula):
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()
        cursor.execute('''
            UPDATE Aluno_Aula
            SET ID_Aula = ?, CPF_Aluno = ?
            WHERE CPF_Aluno = ? 
        ''', (
            Aluno-Aula["ID_Aula"],
            Aluno_Aula["CPF_Aluno"]
        ))
        conexao.commit()
        print(f"Relacionamento com {Aluno_Aula['CPF_Aluno']} alterado com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao alterar relacionamento: {e}")
    finally:
        if conexao:
            conexao.close()
