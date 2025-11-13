# Services/Tabela_Professor.py 
 
import sqlite3
 
conexao = sqlite3.connect("Academia.db")
 
cursor = conexao.cursor()
 
cursor.execute(
    '''
        CREATE TABLE IF NOT EXISTS Professor(
            CPF_Professor INTEGER NOT NULL PRIMARY KEY,
            RG INTEGER UNIQUE,
            Nome VARCHAR NOT NULL,
            Horario TIME NOT NULL,
            Telefone INTEGER UNIQUE NOT NULL
        );
    '''
)
cursor.close()
print("Tabela Professor criada com sucesso")