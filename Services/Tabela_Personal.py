# Services/Tabela_Personal.py 
 
import sqlite3
 
conexao = sqlite3.connect("Academia.db")
 
cursor = conexao.cursor()
 
cursor.execute(
    '''
        CREATE TABLE Personal(
            CPF_Personal INTEGER (11) UNIQUE NOT NULL PRIMARY KEY,
            RG_Persona INTEGER (11) UNIQUE NOT NULL,
            Nome_Personal VARCHAR (255) NOT NULL,
            Horarios_Professor TIME NOT NULL,
            Telefone_Personal INTEGER (11) UNIQUE NOT NULL
        ) ENGINE=InnoDB;
    '''
)
cursor.close()
print("Tabela Personal criada com sucesso")