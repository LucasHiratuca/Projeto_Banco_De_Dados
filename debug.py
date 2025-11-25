# debug_alunos.py
import sqlite3

def debug_alunos():
    conexao = sqlite3.connect("Academia.db")
    cursor = conexao.cursor()
    
    # Verifica a estrutura da tabela
    cursor.execute("PRAGMA table_info(Aluno)")
    colunas = cursor.fetchall()
    print("=== ESTRUTURA DA TABELA ===")
    for coluna in colunas:
        print(f"Coluna {coluna[0]}: {coluna[1]} ({coluna[2]})")
    
    # Verifica os dados reais
    cursor.execute("SELECT * FROM Aluno")
    alunos = cursor.fetchall()
    
    print("\n=== DADOS REAIS NA TABELA ===")
    for i, aluno in enumerate(alunos):
        print(f"Registro {i}: {aluno}")
    
    cursor.close()
    conexao.close()

debug_alunos()