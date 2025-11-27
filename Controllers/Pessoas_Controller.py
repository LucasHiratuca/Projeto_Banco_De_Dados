# Controllers/Pessoas_Controller.py
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
            # CORREÇÃO: Usar os métodos getter corretos (get_...)
            cursor.execute("""
                INSERT INTO Professor (CPF_Professor, RG_Prof, Nome_Prof, Horarios_Prof, Telefone_Prof)
                VALUES (?, ?, ?, ?, ?)
            """, (
                pessoa.get_cpf(), # CORREÇÃO: Usar get_cpf()
                pessoa.get_rg_prof(),
                pessoa.get_nome_prof(),
                pessoa.get_horario_prof(),
                pessoa.get_telefone_prof()        
            ))

        elif isinstance(pessoa, Personal):
            # CORREÇÃO: Usar os métodos getter corretos (get_...)
            cursor.execute("""
                INSERT INTO Personal (CPF_Personal, RG_Personal, Nome_Personal, Horarios_Personal, Telefone_Personal)
                VALUES (?, ?, ?, ?, ?)
            """, (
                pessoa.get_cpf(), # CORREÇÃO: Usar get_cpf()
                pessoa.get_rg_pers(),
                pessoa.get_nome_pers(),
                pessoa.get_horario_pers(),
                pessoa.get_telefone_pers()
                
            )) 
        conexao.commit()
        print("Entidade inserida com sucesso!")
        return True
    except sqlite3.Error as e:
        print(f"Erro ao inserir a entidade: {e}")
        return False
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
            
            # CORREÇÃO: Chaves simplificadas para uso no DataFrame
            dados.append({
                "CPF": CPF_Professor,
                "RG": RG,
                "Nome": Nome,
                "Horários": Horario,
                "Telefone": Telefone
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
            # CORREÇÃO: Chaves simplificadas para uso no DataFrame
            dados.append({
                "CPF": CPF_Personal,
                "RG": RG,
                "Nome": Nome,
                "Horários": Horario,
                "Telefone": Telefone
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
        
        # Correção da tupla para o parâmetro
        cursor.execute("DELETE FROM Aluno WHERE CPF_Aluno = ?", (cpf,))
        
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
        linhas_afetadas = cursor.rowcount # Adicionado verificação
        conexao.commit()
        
        if linhas_afetadas > 0:
            print(f"Professor com CPF {cpf} excluído com sucesso!")
            return True
        else:
            print(f"Nenhum Professor encontrado com CPF {cpf}")
            return False
    except sqlite3.Error as e:
        print(f"Erro ao excluir o professor: {e}")
        return False
    finally:
        if conexao:
            conexao.close()

def excluirPersonal(cpf):
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM Personal WHERE CPF_Personal = ?", (cpf,))
        linhas_afetadas = cursor.rowcount # Adicionado verificação
        conexao.commit()
        
        if linhas_afetadas > 0:
            print(f"Personal com CPF {cpf} excluído com sucesso!")
            return True
        else:
            print(f"Nenhum Personal encontrado com CPF {cpf}")
            return False
    except sqlite3.Error as e:
        print(f"Erro ao excluir o personal: {e}")
        return False
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
            aluno.get_rg_aluno(),
            aluno.get_telefone_aluno(),
            aluno.get_nome_aluno(),
            aluno.get_objetivo_treino(),
            aluno.get_tipo_plano(),
            aluno.get_cpf_pers(),
            aluno.get_cpf()
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


def alterarProfessor(professor): # CORREÇÃO: Recebe o objeto e usa getters
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()
        cursor.execute('''
            UPDATE Professor 
            SET RG_Prof = ?, Nome_Prof = ?, Horarios_Prof = ?, Telefone_Prof = ?
            WHERE CPF_Professor = ?
        ''', (
            professor.get_rg_prof(),
            professor.get_nome_prof(),
            professor.get_horario_prof(),
            professor.get_telefone_prof(),
            professor.get_cpf()
        )) 
        conexao.commit()
        print(f"Professor com CPF {professor.get_cpf()} alterado com sucesso!")
        return True
    except sqlite3.Error as e:
        print(f"Erro ao alterar Professor: {e}")
        return False
    finally:
        if conexao:
            conexao.close()

        
def alterarPersonal(personal): # CORREÇÃO: Recebe o objeto e usa getters
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()
        cursor.execute('''
            UPDATE Personal 
            SET RG_Personal = ?, Nome_Personal = ?, Horarios_Personal = ?, Telefone_Personal = ?
            WHERE CPF_Personal = ?
        ''', (
            personal.get_rg_pers(),
            personal.get_nome_pers(),
            personal.get_horario_pers(),
            personal.get_telefone_pers(),
            personal.get_cpf()
        )) 
        conexao.commit()
        print(f"Personal com CPF {personal.get_cpf()} alterado com sucesso!")
        return True
    except sqlite3.Error as e:
        print(f"Erro ao alterar Personal: {e}")
        return False
    finally:
        if conexao:
            conexao.close()