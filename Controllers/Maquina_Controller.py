# Controllers/Maquina_Controller.py
import sqlite3
from Models.Maquina import Maquina

def conectaBD():
    conexao = sqlite3.connect("Academia.db")
    return conexao

def incluirMaquina(maquina): # CORREÇÃO: Recebe o objeto
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
            INSERT INTO Maquina (Nome_Maquina, ID_Maquina, Parte_Trabalhada) # CORREÇÃO: Tabela Maquina e 3 colunas
            VALUES (?, ?, ?) # CORREÇÃO: 3 placeholders
            """, (
                maquina.nome, # CORREÇÃO: Acessa a propriedade
                maquina.id_mqn, 
                maquina.parte_trabalhada
            )) 
        conexao.commit()
        print("Maquina inserida com sucesso!")
        return True
    except sqlite3.Error as e:
        print(f"Erro ao inserir maquina: {e}")
        return False
    finally:
        conexao.close()

def consultarMaquina(): # CORREÇÃO: Renomeado de consultarPlano
    conexao = conectaBD()
    cursor = conexao.cursor()
    
    try:
        cursor.execute('SELECT * FROM Maquina')
        rows = cursor.fetchall()
        
        # Lista para armazenar os dados
        dados = []
        
        for row in rows:
            # CORREÇÃO: Desempacotar 3 colunas
            Nome_Maquina, ID_Maquina, Parte_Trabalhada = row
            
            # Adiciona os dados à lista
            dados.append({
                "Nome da Maquina": Nome_Maquina,
                "ID da Maquina": ID_Maquina,
                "Parte Trabalhada": Parte_Trabalhada # Adicionado campo
            })
        
        return dados
    
    except sqlite3.Error as e:
        print(f"Erro ao consultar as Maquinas: {e}")
        return []
    
    finally:
        conexao.close()
    

def excluirMaquina(Nome_Maquina): # CORREÇÃO: Renomeado de excluirPlano e usa Nome_Maquina (PK)
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()
        # CORREÇÃO: Tabela Maquina e parâmetro em tupla
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

def alterarMaquina(maquina): # CORREÇÃO: Recebe o objeto
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()
        # Nome_Maquina é a chave primária
        cursor.execute('''
            UPDATE Maquina
            SET ID_Maquina = ?, Parte_Trabalhada = ?
            WHERE Nome_Maquina = ?
        ''', (
            maquina.id_mqn, # CORREÇÃO: Acessa a propriedade
            maquina.parte_trabalhada,
            maquina.nome # CORREÇÃO: Usa a PK para o WHERE
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