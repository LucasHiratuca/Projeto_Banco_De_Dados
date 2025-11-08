# Services/Tabela_Professor.py 
 
import sqlite3
 
conexao = sqlite3.connect("Academia.db")
 
cursor = conexao.cursor()
 
cursor.execute(
    '''
        CREATE TABLE Professor(
            CPF_Professor INTEGER (11) UNIQUE NOT NULL PRIMARY KEY,
            RG_Professor INTEGER (11) UNIQUE NOT NULL,
            Nome_Professor VARCHAR (255) NOT NULL,
            Horarios_Professor TIME NOT NULL,
            Telefone_Professor INTEGER (11) UNIQUE NOT NULL
        ) ENGINE=InnoDB;
    '''
)
cursor.close()
print("Tabela Professor criada com sucesso")