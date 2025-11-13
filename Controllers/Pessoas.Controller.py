# Controllers/PessoasController.py
import sqlite3
from Modelos.Aluno import Aluno
from Modelos.Professor import Professor
from Modelos.Personal import Personal

def conectaBD():
    conexao = sqlite3.connect("Academia.db")
    return conexao

def incluirPessoa(pessoa):
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        if isinstance(pessoa, Aluno):
            cursor.execute("""
                INSERT INTO Aluno (CPF_Aluno, RG_Aluno, Telefone, Nome, Objetivo_Treino, Tipo_Plano, CPF_Personal)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                pessoa.get_cpf_aluno(),
                pessoa.get_rg_aluno(),
                pessoa.get_telefone_al(),
                pessoa.get_nome_al(),
                pessoa.get_objetivo_treino(),
                pessoa.get_tipo_plano(),
                pessoa.get_cpf_pers(),
            )) 
        elif isinstance(pessoa, Professor):
            cursor.execute("""
                INSERT INTO Professor (CPF_Professor, RG_Professor, Nome_Professor, Horario_Professor, Telefone_Professor)
                VALUES (?, ?, ?, ?, ?)
            """, (
                pessoa.get_cpf_professor(),
                pessoa.get_rg_professor(),
                pessoa.get_nome_professor(),
                pessoa.get_horario_professor(),
                pessoa.get_telefone_professor()        
            ))

        elif isinstance(pessoa, Personal):
            cursor.execute("""
                INSERT INTO Personal (CPF_Personal, RG_Personal, Nome_Personal, Horario_Personal, Telefone_Personal)
                VALUES (?, ?, ?, ?, ?)
            """, (
                pessoa.get_cpf_personal(),
                pessoa.get_rg_personal(),
                pessoa.get_nome_personal(),
                pessoa.get_horario_personal(),
                pessoa.get_telefone_personal()
                
            )) 
        conexao.commit()
        print("Funcionário inserido com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao inserir funcionário: {e}")
    finally:
        conexao.close()


def consultarAluno():
    conexao = conectaBD()
    cursor = conexao.cursor()
    
    try:
        cursor.execute('SELECT * FROM Aluno')
        rows = cursor.fetchall()
          # Lista para armazenar os dados dos Alunos
        dados = []
        
        for row in rows:
            CPF_Aluno, RG, Nome, Telefone, Objetivo_Treino, Tipo_Plano, CPF_Personal = row
            
            # Adiciona os dados do funcionário à lista
            dados.append({
                "CPF_Aluno: ": CPF_Aluno,
                "RG: ": RG,
                "Nome: ": Nome,
                "Telefone: ": Telefone,
                "Objetivo de Treino: ": Objetivo_Treino,
                "Tipo de Plano: ": Tipo_Plano,
                "CPF do Personal": CPF_Personal
             })
        
        return dados
    
    except sqlite3.Error as e:
        print(f"Erro ao consultar os alunos: {e}")
        return []
    finally:
        conexao.close()


def consultarProfessor():
    conexao = conectaBD()
    cursor = conexao.cursor()
    
    try:
        cursor.execute('SELECT * FROM Professor')
        rows = cursor.fetchall()
        
        # Lista para armazenar os dados dos professores
        dados = []
        
        for row in rows:
            CPF_Professor, RG, Nome, Horario, Telefone = row
            
            # Adiciona os dados do funcionário à lista
            dados.append({
                "CPF Professor: ": CPF_Professor,
                "RG: ": RG,
                "Nome: ": Nome,
                "Horario: ": Horario,
                "Telefone: ": Telefone
            })
        
        return dados
    
    except sqlite3.Error as e:
        print(f"Erro ao consultar os Professores: {e}")
        return []
    finally:
        conexao.close()


def consultarPersonal():
    conexao = conectaBD()
    cursor = conexao.cursor()
    
    try:
        cursor.execute('SELECT * FROM Personal')
        rows = cursor.fetchall()
        
        # Lista para armazenar os dados dos personais
        dados = []
        
        for row in rows:

            CPF_Personal, RG, Nome, Horario, Telefone = row
            
        # Adiciona os dados do funcionário à lista
            dados.append({
                "CPF Personal: ": CPF_Personal,
                "RG: ": RG,
                "Nome: ": Nome,
                "Horario: ": Horario,
                "Telefone: ": Telefone
                })
        
        return dados
    
    except sqlite3.Error as e:
        print(f"Erro ao consultar os Personais: {e}")
        return []
    finally:
        conexao.close()
    
    
def excluirAluno(cpf):
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM Aluno WHERE CPF_Aluno = ?", (cpf,))
        conexao.commit()
        print(f"Aluno com codigo {cpf,} excluído com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao excluir o aluno: {e}")
    finally:
        if conexao:
            conexao.close()

def excluirProfessor(cpf):
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM Professor WHERE CPF_Professor = ?", (cpf,))
        conexao.commit()
        print(f"Professor com codigo {cpf,} excluído com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao excluir o professor: {e}")
    finally:
        if conexao:
            conexao.close()

def excluirPersonal(cpf):
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM Personal WHERE CPF_Personal = ?", (cpf,))
        conexao.commit()
        print(f"Personal com codigo {cpf,} excluído com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao excluir o personal: {e}")
    finally:
        if conexao:
            conexao.close()

def alterarAluno(aluno):
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()
        cursor.execute('''
            UPDATE Aluno 
            SET CPF_Aluno = ?, RG = ?, Telefone = ?, Nome = ?, Objetivo_Treino = ?, Tipo_Plano = ?, CPF_Personal = ?
            WHERE CPF_Aluno = ?
        ''', (
            aluno["CPF_Aluno"],
            aluno["RG"],
            aluno["Telefone"],
            aluno["Nome"],
            aluno["Objetivo_Treino"],
            aluno["Tipo_Plano"],
            aluno["CPF_Personal"]
        ))
        conexao.commit()
        print(f"Funcionário com código {aluno['CPF_Aluno']} alterado com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao alterar Funcionário: {e}")
    finally:
        if conexao:
            conexao.close()