# Controllers/PessoasController.py
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
                pessoa.get_cpf_aluno(),
                pessoa.get_rg_aluno(),
                pessoa.get_telefone(),
                pessoa.get_nome(),
                pessoa.get_objetivo_treino(),
                pessoa.get_tipo_plano(),
                pessoa.get_cpf_personal(),
            )) 

        elif isinstance(pessoa, Professor):
            cursor.execute("""
                INSERT INTO Professor (CPF_Professor, RG_Professor, Nome_Professor, Horario_Professor, Telefone_Professor)
                VALUES (?, ?, ?, ?, ?)
            """, (
                pessoa.get_cpf_professor(),
                pessoa.get_rg_professor(),
                pessoa.get_nome_professor(),
                pessoa.get_telefone_professor(),
                pessoa.get_horario_professor()
            ))

        elif isinstance(pessoa, Personal):
            cursor.execute("""
                INSERT INTO Personal (CPF_Personal, RG_Personal, Nome_Personal, Horario_Personal, Telefone_Personal)
                VALUES (?, ?, ?, ?, ?)
            """, (
                pessoa.get_cpf_personal(),
                pessoa.get_rg_personal(),
                pessoa.get_nome_personal(),
                pessoa.get_telefone_personal(),
                pessoa.get_horario_personal()
            )) 

        conexao.commit()
        print("Dados inseridos com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao inserir uma novo usuário: {e}")
    finally:
        conexao.close()

def consultarFuncionario():
    conexao = conectaBD()
    cursor = conexao.cursor()
    
    try:
        cursor.execute('SELECT * FROM funcionario')
        rows = cursor.fetchall()
        
        # Lista para armazenar os dados dos funcionários
        dados = []
        
        for row in rows:
            codigo, nome, tipo, diasTrabalhados, valorDia, salarioBase, comissao = row
            
            if tipo == 'FreeLancer':
                funcionario = FreeLancer(codigo, nome, diasTrabalhados, valorDia)
                salario = funcionario.calcularSalario()
            elif tipo == 'Vendedor':
                funcionario = Vendedor(codigo, nome, salarioBase, comissao)
                salario = funcionario.calcularSalario()
            
            # Adiciona os dados do funcionário à lista
            dados.append({
                "Código": codigo,
                "Nome": nome,
                "Tipo": tipo,
                "Dias Trabalhados": diasTrabalhados,
                "Valor Dia": valorDia,
                "Salário Base": salarioBase,
                "Comissão": comissao,
                "Salário Calculado": salario
            })
        
        return dados
    
    except sqlite3.Error as e:
        print(f"Erro ao consultar funcionários: {e}")
        return []
    
    finally:
        conexao.close()
    
    
def excluirFuncionario(codigo):
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM funcionario WHERE codigo = ?", (codigo,))
        conexao.commit()
        print(f"Funcionario com codigo {codigo} excluído com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao excluir funcionario: {e}")
    finally:
        if conexao:
            conexao.close()

def alterarFuncionario(funcionario):
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()
        cursor.execute('''
            UPDATE funcionario 
            SET codigo = ?, nome = ?, tipo = ?, diasTrabalhados = ?, valorDia = ?, salarioBase = ?, comissao = ?
            WHERE codigo = ?
        ''', (
            funcionario["Código"],
            funcionario["Nome"],
            funcionario["Tipo"],
            funcionario["Dias Trabalhados"],
            funcionario["Valor Dia"],
            funcionario["Salário Base"],
            funcionario["Comissão"],
            funcionario["Código"]
        ))
        conexao.commit()
        print(f"Funcionário com código {funcionario['Código']} alterado com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao alterar Funcionário: {e}")
    finally:
        if conexao:
            conexao.close()