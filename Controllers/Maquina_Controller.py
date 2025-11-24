import sqlite3
from Models.Maquina import Maquina

def conectaBD():
    conexao = sqlite3.connect("Academia.db")
    return conexao

def incluirMaquina():
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
            INSERT INTO Plano (Nome_Maquina, ID_Maquina, Parte_Trabalhada)
            VALUES (?, ?)
            """, (
                Maquina.nome_mqn_mqn(),
                Maquina.id_mqn(),
                Maquina.parte_trabalhada
            )) 
        conexao.commit()
        print("Maquina inserida com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao inserir maquina: {e}")
    finally:
        conexao.close()

def consultarPlano():
    conexao = conectaBD()
    cursor = conexao.cursor()
    
    try:
        cursor.execute('SELECT * FROM Maquina')
        rows = cursor.fetchall()
        
        # Lista para armazenar os dados do relacionamento
        dados = []
        
        for row in rows:
            Nome_Maquina, ID_Maquina = row
            
            # Adiciona os dados à lista
            dados.append({
                "Nome da Maquina: ": Nome_Maquina,
                "ID do Maquina: ": ID_Maquina
            })
        
        return dados
    
    except sqlite3.Error as e:
        print(f"Erro ao consultar as Maquinas: {e}")
        return []
    
    finally:
        conexao.close()
    

def excluirPlano(Nome_Maquina):
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM Maquinas WHERE Nome_Maquina = ?", Nome_Maquina,)
        conexao.commit()
        print(f"Relacionamento com {Nome_Maquina,} excluído com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao excluir maquina: {e}")
    finally:
        if conexao:
            conexao.close()

def alterarMaquina(Maquina):
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()
        cursor.execute('''
            UPDATE Maquina
            SET ID_Treino = ?, Nome_Maquina = ?
            WHERE ID_Treino = ?
        ''', (
            Maquina["Nome_Maquina"],
            Maquina["ID_Maquina"],
            Maquina[Parte_Trabalhada],

        ))
        conexao.commit()
        print(f"Tabela com {Maquina['Nome_Maquina']} alterado com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao alterar Maquina: {e}")
    finally:
        if conexao:
            conexao.close()