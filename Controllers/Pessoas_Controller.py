# Controllers/PessoasController.py

# CRUD de Aluno, Professor e Personal

import sqlite3
from Models.Aluno import Aluno
from Models.Professor import Professor
from Models.Personal import Personal

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
                pessoa.cpf(),
                pessoa.rg_aluno(),
                pessoa.telefone_aluno(),
                pessoa.nome_aluno(),
                pessoa.objetivo_treino(),
                pessoa.tipo_plano(),
                pessoa.cpf_pers(),
            )) 
        elif isinstance(pessoa, Professor):
            cursor.execute("""
                INSERT INTO Professor (CPF_Professor, RG_Professor, Nome_Professor, Horario_Professor, Telefone_Professor)
                VALUES (?, ?, ?, ?, ?)
            """, (
                pessoa.cpf(),
                pessoa.rg_prof(),
                pessoa.nome_prof(),
                pessoa.horario_prof(),
                pessoa.telefone_prof()        
            ))

        elif isinstance(pessoa, Personal):
            cursor.execute("""
                INSERT INTO Personal (CPF_Personal, RG_Personal, Nome_Personal, Horario_Personal, Telefone_Personal)
                VALUES (?, ?, ?, ?, ?)
            """, (
                pessoa.cpf(),
                pessoa.rg_personal(),
                pessoa.nome_pers(),
                pessoa.horario_pers(),
                pessoa.telefone_pers()
                
            )) 
        conexao.commit()
        print("Entidade inserida com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao inserir a entidade: {e}")
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
            SET RG = ?, Telefone = ?, Nome = ?, Objetivo_Treino = ?, Tipo_Plano = ?, CPF_Personal = ?
            WHERE CPF_Aluno = ?
        ''', (
            aluno["RG"],
            aluno["Telefone"],
            aluno["Nome"],
            aluno["Objetivo_Treino"],
            aluno["Tipo_Plano"],
            aluno["CPF_Personal"],
            aluno["CPF_Aluno"]
        ))
        conexao.commit()
        print(f"Aluno com CPF {aluno['CPF_Aluno']} alterado com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao alterar Aluno: {e}")
    finally:
        if conexao:
            conexao.close()


def alterarProfessor(professor):
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()
        cursor.execute('''
            UPDATE Professor 
            SET RG = ?, Nome = ?, Telefone = ?, Horario = ?
            WHERE CPF_Professor = ?
        ''', (
            professor["RG"],
            professor["Nome"],
            professor["Telefone"],
            professor["Horario"],
            professor["CPF_Professor"],
        )) 
        conexao.commit()
        print(f"Professor com CPF {professor['CPF_Professor']} alterado com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao alterar Professor: {e}")
    finally:
        if conexao:
            conexao.close()

        
def alterarPersonal(personal):
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()
        cursor.execute('''
            UPDATE Personal 
            SET RG = ?, Nome = ?, Telefone = ?, Horario = ?
            WHERE CPF_Personal = ?
        ''', (
            personal["RG"],
            personal["Nome"],
            personal["Telefone"],
            personal["Horario"],
            personal["CPF_Personal"],
        )) 
        conexao.commit()
        print(f"Personal com CPF {personal['CPF_Personal']} alterado com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao alterar Personal: {e}")
    finally:
        if conexao:
            conexao.close()