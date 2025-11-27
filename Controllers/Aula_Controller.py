# Controllers/Aula_Controller.py
import sqlite3
from Models.Aula import Aula # CORREÇÃO: Importar a classe renomeada

def conectaBD():
    conexao = sqlite3.connect("Academia.db")
    return conexao

def incluirAula(aula): # CORREÇÃO: Recebe o objeto
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
            INSERT INTO Aula (ID_Aula, Tipo_Aula, CPF_Professor)
            VALUES (?, ?, ?) # CORREÇÃO: 3 placeholders
            """, (
                aula.id_aula, # CORREÇÃO: Acessa a propriedade do objeto
                aula.tipo_aula,
                aula.cpf_professor
            )) 
        conexao.commit()
        print("Aula inserida com sucesso!")
        return True
    except sqlite3.Error as e:
        print(f"Erro ao inserir Aula: {e}")
        return False
    finally:
        conexao.close()

def consultarAula():
    conexao = conectaBD()
    cursor = conexao.cursor()
    
    try:
        cursor.execute("SELECT * FROM Aula")
        rows = cursor.fetchall()
        
        # Lista para armazenar os dados do relacionamento
        dados = []
        
        for row in rows:
            # CORREÇÃO: Desempacotar 3 colunas
            ID_Aula, Tipo_Aula, CPF_Professor = row
            
            # Adiciona os dados à lista
            dados.append({
                "ID da Aula": ID_Aula,
                "Tipo da Aula": Tipo_Aula, # CORREÇÃO: Campo adicionado
                "CPF do Professor": CPF_Professor
            })
        
        return dados
    
    except sqlite3.Error as e:
        print(f"Erro ao consultar as Aulas: {e}")
        return []
    
    finally:
        conexao.close()
    

def excluirAula(ID_Aula): # CORREÇÃO: Recebe ID_Aula e usa tupla
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM Aula WHERE ID_Aula = ?", (ID_Aula,)) # CORREÇÃO: Tupla (ID_Aula,)
        linhas_afetadas = cursor.rowcount
        conexao.commit()
        if linhas_afetadas > 0:
            print(f"Aula com ID {ID_Aula} excluída com sucesso!")
            return True
        else:
            print(f"Nenhuma aula encontrada com ID {ID_Aula}.")
            return False
    except sqlite3.Error as e:
        print(f"Erro ao excluir aula: {e}")
        return False
    finally:
        if conexao:
            conexao.close()

def excluirAulaEsp(ID_Aula, CPF_Professor):
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()
        # CORREÇÃO: Parâmetros como tupla
        cursor.execute("DELETE FROM Aula WHERE ID_Aula = ? AND CPF_Professor = ?", (ID_Aula, CPF_Professor))
        linhas_afetadas = cursor.rowcount
        conexao.commit()
        if linhas_afetadas > 0:
            print(f"Aula com ID {ID_Aula} e CPF do Professor {CPF_Professor} excluída com sucesso!")
            return True
        else:
            print(f"Aula com ID {ID_Aula} e CPF do Professor {CPF_Professor} não encontrada.")
            return False
    except sqlite3.Error as e:
        print(f"Erro ao excluir relacionamento: {e}")
        return False
    finally:
        if conexao:
            conexao.close()

def alterarAula(aula): # CORREÇÃO: Recebe o objeto
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()
        # ID_Aula é a chave primária, então a atualização deve ser feita com base nela.
        cursor.execute('''
            UPDATE Aula
            SET Tipo_Aula = ?, CPF_Professor = ?
            WHERE ID_Aula = ? 
        ''', (
            aula.tipo_aula, # CORREÇÃO: Acessa a propriedade
            aula.cpf_professor,
            aula.id_aula # CORREÇÃO: Usa a PK para o WHERE
        ))
        conexao.commit()
        print(f"Aula com ID {aula.id_aula} alterada com sucesso!")
        return True
    except sqlite3.Error as e:
        print(f"Erro ao alterar aula: {e}")
        return False
    finally:
        if conexao:
            conexao.close()