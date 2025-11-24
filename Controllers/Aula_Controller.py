import sqlite3
from Models.Aula import Aula

def conectaBD():
    conexao = sqlite3.connect("Academia.db")
    return conexao

def incluirAula():
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
            INSERT INTO Aula (ID_Aula,  Tipo_Aula, CPF_Professor)
            VALUES (?, ?)
            """, (
                Aula.id_aula(),
                Aula.tipo_aula(),
                Aula.cpf_professor()
            )) 
        conexao.commit()
        print("Aula inserida com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao inserir Aula: {e}")
    finally:
        conexao.close()

def consultarAula():
    conexao = conectaBD()
    cursor = conexao.cursor()
    
    try:
        cursor.execute('SELECT * FROM Aula)
        rows = cursor.fetchall()
        
        # Lista para armazenar os dados do relacionamento
        dados = []
        
        for row in rows:
            ID_Aula, CPF_Professor = row
            
            # Adiciona os dados à lista
            dados.append({
                "ID da Aula": ID_Aula,
                "CPF do Professor": CPF_Professor
            })
        
        return dados
    
    except sqlite3.Error as e:
        print(f"Erro ao consultar o relacionamento: {e}")
        return []
    
    finally:
        conexao.close()
    

def excluirAula(ID_Aula):
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM Aula WHERE ID_Aula = ?", CPF_Professor,)
        conexao.commit()
        print(f"Relacionamento com {CPF_Professor,} excluído com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao excluir relacionamento: {e}")
    finally:
        if conexao:
            conexao.close()

def excluirAulaEsp(ID_Aula, CPF_Professor):
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM Aula WHERE ID_Aula = ? AND CPF_Professor = ?", ID_Aula, CPF_Professor)
        conexao.commit()
        print(f"Relacionamento com {CPF_Professor,} e {ID_Aula} excluído com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao excluir relacionamento: {e}")
    finally:
        if conexao:
            conexao.close()

def alterarAula(Aula):
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()
        cursor.execute('''
            UPDATE Aula
            SET ID_Aula = ?, CPF_Professor = ?
            WHERE CPF_Professor = ? 
        ''', (
            Aula["ID_Aula"],
            Aula["CPF_Professor"],
            Aula("CPF_Professor")
        ))
        conexao.commit()
        print(f"Relacionamento com {Aula['CPF_Professor']} alterado com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao alterar relacionamento: {e}")
    finally:
        if conexao:
            conexao.close()