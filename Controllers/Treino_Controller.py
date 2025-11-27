# Controllers/Treino_Controller.py
import sqlite3
from Models.Treino import Treino

def conectaBD():
    conexao = sqlite3.connect("Academia.db")
    return conexao

def incluirTreino(treino): # CORREÇÃO: Recebe o objeto
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
            INSERT INTO Treino (ID_Treino, Alongamentos, Exercicios_Aerobicos, Exercicios_Maquina ,Carga , CPF_Aluno)
            VALUES (?, ?, ?, ?, ?, ?) # CORREÇÃO: 6 placeholders
            """, (
               treino.id, # CORREÇÃO: Acessa a propriedade
               treino.alongamentos,
               treino.exercicios_arbcs, # CORREÇÃO: Acessa a propriedade
               treino.exercicios_mqn, # CORREÇÃO: Acessa a propriedade
               treino.carga_mqn, # CORREÇÃO: Acessa a propriedade
               treino.cpf_aluno # CORREÇÃO: Acessa a propriedade
            )) 
        conexao.commit()
        print("Treino inserido com sucesso!")
        return True
    except sqlite3.Error as e:
        print(f"Erro ao inserir treino: {e}")
        return False
    finally:
        conexao.close()

def consultarTreino():
    conexao = conectaBD()
    cursor = conexao.cursor()
    
    try:
        cursor.execute('SELECT * FROM Treino') # CORREÇÃO: Aspa de fechamento
        rows = cursor.fetchall()
        
        # Lista para armazenar os dados
        dados = []
        
        for row in rows:
            # CORREÇÃO: Desempacotar 6 colunas
            ID_Treino, Alongamentos, Exercicios_Aerobicos, Exercicios_Maquina, Carga, CPF_Aluno = row
            
            # Adiciona os dados à lista
            dados.append({
                "ID do Treino": ID_Treino,
                "Alongamentos": Alongamentos,
                "Ex. Aeróbicos": Exercicios_Aerobicos,
                "Ex. Máquina": Exercicios_Maquina,
                "Carga": Carga,
                "CPF Aluno": CPF_Aluno
            })
        
        return dados
    
    except sqlite3.Error as e:
        print(f"Erro ao consultar o relacionamento: {e}")
        return []
    
    finally:
        conexao.close()
    

def excluirTreino(ID_Treino): # CORREÇÃO: Recebe ID_Treino para exclusão
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM Treino WHERE ID_Treino = ?", (ID_Treino,)) # CORREÇÃO: Usa ID_Treino com tupla
        linhas_afetadas = cursor.rowcount
        conexao.commit()
        if linhas_afetadas > 0:
            print(f"Treino com ID {ID_Treino} excluído com sucesso!")
            return True
        else:
            print(f"Nenhum treino encontrado com ID {ID_Treino}.")
            return False
    except sqlite3.Error as e:
        print(f"Erro ao excluir relacionamento: {e}")
        return False
    finally:
        if conexao:
            conexao.close()

def excluirTreinoEsp(ID_Treino, CPF_Aluno):
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM Treino WHERE ID_Treino = ? AND CPF_Aluno = ?", (ID_Treino, CPF_Aluno)) # CORREÇÃO: Tupla
        linhas_afetadas = cursor.rowcount
        conexao.commit()
        if linhas_afetadas > 0:
            print(f"Relacionamento com CPF {CPF_Aluno} e ID do Treino {ID_Treino} excluído com sucesso!")
            return True
        else:
            print(f"Relacionamento com CPF {CPF_Aluno} e ID do Treino {ID_Treino} não encontrado.")
            return False
    except sqlite3.Error as e:
        print(f"Erro ao excluir relacionamento: {e}")
        return False
    finally:
        if conexao:
            conexao.close()

def alterarTreino(treino): # CORREÇÃO: Recebe o objeto
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()
        # Atualiza os campos do treino com base no ID_Treino
        cursor.execute('''
            UPDATE Treino
            SET Alongamentos = ?, Exercicios_Aerobicos = ?, Exercicios_Maquina = ?, Carga = ?, CPF_Aluno = ?
            WHERE ID_Treino = ? 
        ''', (
            treino.alongamentos,
            treino.exercicios_arbcs,
            treino.exercicios_mqn,
            treino.carga_mqn,
            treino.cpf_aluno,
            treino.id
        ))
        conexao.commit()
        print(f"Treino com ID {treino.id} alterado com sucesso!")
        return True
    except sqlite3.Error as e:
        print(f"Erro ao alterar relacionamento: {e}")
        return False
    finally:
        if conexao:
            conexao.close()