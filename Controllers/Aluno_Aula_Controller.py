# Controllers/Aluno_Aula_Controller.py
import sqlite3
from Models.Aluno_Aula import Aluno_Aula

def conectaBD():
    conexao = sqlite3.connect("Academia.db")
    return conexao

def incluirAlunoAula(aluno_aula): # CORREÇÃO: Recebe o objeto
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
            INSERT INTO Aluno_Aula (ID_Aula, CPF_Aluno)
            VALUES (?, ?)
            """, (
                aluno_aula.id_aula, # CORREÇÃO: Acessa a propriedade do objeto
                aluno_aula.cpf_aluno
            )) 
        conexao.commit()
        print("Dados inseridos com sucesso!")
        return True
    except sqlite3.Error as e:
        print(f"Erro ao inserir dados: {e}")
        return False
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
    

def excluirAlunoAula(ID_Aula): # CORREÇÃO: Alterado para excluir por ID_Aula
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()
        # CORREÇÃO: Usar ID_Aula com tupla
        cursor.execute("DELETE FROM Aluno_Aula WHERE ID_Aula = ?", (ID_Aula,))
        linhas_afetadas = cursor.rowcount
        conexao.commit()
        if linhas_afetadas > 0:
            print(f"Relacionamento(s) com ID_Aula {ID_Aula} excluído com sucesso!")
            return True
        else:
            print(f"Nenhum relacionamento encontrado com ID_Aula {ID_Aula}.")
            return False
    except sqlite3.Error as e:
        print(f"Erro ao excluir relacionamento: {e}")
        return False
    finally:
        if conexao:
            conexao.close()

def excluirAlunoAulaEsp(ID_Aula, CPF_Aluno):
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()
        # CORREÇÃO: Parâmetros como tupla
        cursor.execute("DELETE FROM Aluno_Aula WHERE ID_Aula = ? AND CPF_Aluno = ?", (ID_Aula, CPF_Aluno))
        linhas_afetadas = cursor.rowcount
        conexao.commit()
        if linhas_afetadas > 0:
            print(f"Relacionamento com CPF {CPF_Aluno} e ID da Aula {ID_Aula} excluído com sucesso!")
            return True
        else:
            print(f"Relacionamento com CPF {CPF_Aluno} e ID da Aula {ID_Aula} não encontrado.")
            return False
    except sqlite3.Error as e:
        print(f"Erro ao excluir relacionamento: {e}")
        return False
    finally:
        if conexao:
            conexao.close()

def alterarAlunoAula(aluno_aula): # CORREÇÃO: Recebe o objeto
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()
        # A chave primária é composta (ID_Aula, CPF_Aluno), por isso o WHERE deve usar ambos se não puder atualizar um.
        cursor.execute('''
            UPDATE Aluno_Aula
            SET ID_Aula = ?, CPF_Aluno = ?
            WHERE ID_Aula = ? AND CPF_Aluno = ? 
        ''', (
            aluno_aula.id_aula,
            aluno_aula.cpf_aluno,
            aluno_aula.id_aula, # Usando o ID_Aula como a chave para WHERE
            aluno_aula.cpf_aluno # Usando o CPF_Aluno como a chave para WHERE
        ))
        conexao.commit()
        print(f"Relacionamento com CPF {aluno_aula.cpf_aluno} alterado com sucesso!")
        return True
    except sqlite3.Error as e:
        print(f"Erro ao alterar relacionamento: {e}")
        return False
    finally:
        if conexao:
            conexao.close()
