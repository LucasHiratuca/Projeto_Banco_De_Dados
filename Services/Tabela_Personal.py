# Services/Tabela_Personal.py 
 
import sqlite3
 
conexao = sqlite3.connect("Academia.db")
 
cursor = conexao.cursor()
 
cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS Personal (
        CPF_Personal INTEGER PRIMARY KEY,
        RG INTEGER UNIQUE,
        Nome TEXT NOT NULL,
        Horario TEXT NOT NULL,  -- formato "HH:MM:SS"
        Telefone INTEGER UNIQUE NOT NULL
    );
    '''
)

cursor.close()
print("Tabela Personal criada com sucesso")