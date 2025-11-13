# Services/Tabela_Aula.py 
 
import sqlite3
 
conexao = sqlite3.connect("Academia.db")
 
cursor = conexao.cursor()
 
cursor.execute(
    '''
        CREATE TABLE IF NOT EXISTS Aula(
            ID_Aula INTEGER PRIMARY KEY,
            Tipo_Aula TEXT UNIQUE NOT NULL,
            CPF_Professor INTEGER UNIQUE NOT NULL,
            FOREIGN KEY (CPF_Professor) REFERENCES Professor(CPF_Professor)
        );
    '''
)
cursor.close()
print("Tabela Aula criada com sucesso")