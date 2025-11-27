# Controllers/Plano_Controller.py
import sqlite3
from Models.Plano import Plano

def conectaBD():
    conexao = sqlite3.connect("Academia.db")
    return conexao

def incluirPlano(plano): # CORREÇÃO: Recebe o objeto
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
            INSERT INTO Plano (Tipo_Plano, ID_Plano)
            VALUES (?, ?)
            """, (
                plano.tipo_plano, # CORREÇÃO: Acessa a propriedade
                plano.id_plano
            )) 
        conexao.commit()
        print("Dados inseridos com sucesso!")
        return True
    except sqlite3.Error as e:
        print(f"Erro ao inserir dados: {e}")
        return False
    finally:
        conexao.close()

def consultarPlano():
    conexao = conectaBD()
    cursor = conexao.cursor()
    
    try:
        cursor.execute('SELECT * FROM Plano')
        rows = cursor.fetchall()
        
        # Lista para armazenar os dados
        dados = []
        
        for row in rows:
            Tipo_Plano, ID_Plano = row
            
            # CORREÇÃO: Chaves simplificadas
            dados.append({
                "Tipo do Plano": Tipo_Plano,
                "Id do Plano": ID_Plano
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
        cursor.execute("DELETE FROM Plano WHERE Tipo_Plano = ?", (Tipo_Plano,)) # CORREÇÃO: Tupla (Tipo_Plano,)
        linhas_afetadas = cursor.rowcount
        conexao.commit()
        if linhas_afetadas > 0:
            print(f"Plano com tipo {Tipo_Plano} excluído com sucesso!")
            return True
        else:
            print(f"Nenhum plano encontrado com tipo {Tipo_Plano}.")
            return False
    except sqlite3.Error as e:
        print(f"Erro ao excluir plano: {e}")
        return False
    finally:
        if conexao:
            conexao.close()

def alterarPlano(plano): # CORREÇÃO: Recebe o objeto
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()
        cursor.execute('''
            UPDATE Plano # CORREÇÃO: Tabela Plano
            SET ID_Plano = ?
            WHERE Tipo_Plano = ? # CORREÇÃO: Usa Tipo_Plano como PK para WHERE
        ''', (
            plano.id_plano,
            plano.tipo_plano,
        ))
        conexao.commit()
        print(f"Plano com tipo {plano.tipo_plano} alterado com sucesso!") # CORREÇÃO: Mensagem de print
        return True
    except sqlite3.Error as e:
        print(f"Erro ao alterar Plano: {e}")
        return False
    finally:
        if conexao:
            conexao.close()