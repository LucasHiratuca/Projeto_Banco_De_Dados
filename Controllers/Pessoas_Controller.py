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
                INSERT INTO Aluno (CPF_Aluno, RG, Telefone, Nome, Objetivo_Treino, Tipo_Plano, CPF_Personal)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                pessoa.get_cpf(),
                pessoa.get_rg_aluno(),
                pessoa.get_telefone_aluno(),
                pessoa.get_nome_aluno(),
                pessoa.get_objetivo_treino(),
                pessoa.get_tipo_plano(),
                pessoa.get_cpf_pers(),
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
        dados = []
        for row in rows:
            
            CPF_Aluno = row[0]        # CPF_Aluno
            RG = row[1]               # RG
            Telefone = row[2]         # Telefone
            Nome = row[3]             # Nome
            Objetivo_Treino = row[4]  # Objetivo_Treino
            Tipo_Plano = row[5]       # Tipo_Plano
            CPF_Personal = row[6]     # CPF_Personal
            
            dados.append({
                "CPF": CPF_Aluno,
                "RG": RG,
                "Número": Telefone,
                "Nome": Nome,
                "Objetivo de treino": Objetivo_Treino,
                "Tipo do Plano": Tipo_Plano,
                "CPF do Personal": CPF_Personal
            })
        
        return dados
    except Exception as e:
        print(f"Erro na consulta: {e}")
        return []
    finally:
        cursor.close()
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
        
        # CORRETO ✓ - Adicione a vírgula para criar uma tupla
        cursor.execute("DELETE FROM Aluno WHERE CPF_Aluno = ?", (cpf,))
        
        # Verifica se realmente excluiu algum registro
        linhas_afetadas = cursor.rowcount
        conexao.commit()
        
        if linhas_afetadas > 0:
            print(f"Aluno com CPF {cpf} excluído com sucesso!")
            return True
        else:
            print(f"Nenhum aluno encontrado com CPF {cpf}")
            return False
            
    except sqlite3.Error as e:
        print(f"Erro ao excluir o aluno: {e}")
        return False
    finally:
        if conexao:
            conexao.close()

def excluirProfessor(cpf):
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM Professor WHERE CPF_Professor = ?", (cpf,))
        conexao.commit()
        print(f"Professor com codigo {cpf} excluído com sucesso!")
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
        print(f"Personal com codigo {cpf} excluído com sucesso!")
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
            aluno.get_rg_aluno(),           # RG
            aluno.get_telefone_aluno(),     # Telefone
            aluno.get_nome_aluno(),         # Nome
            aluno.get_objetivo_treino(),    # Objetivo_Treino
            aluno.get_tipo_plano(),         # Tipo_Plano
            aluno.get_cpf_pers(),           # CPF_Personal
            aluno.get_cpf()                 # CPF_Aluno (WHERE)
        ))
        conexao.commit()
        print(f"Aluno com CPF {aluno.get_cpf()} alterado com sucesso!")
        return True
    except sqlite3.Error as e:
        print(f"Erro ao alterar Aluno: {e}")
        return False
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