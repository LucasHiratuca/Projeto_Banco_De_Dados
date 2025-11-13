# Services/Tabela_Aluno.py 
 
import sqlite3
 
conexao = sqlite3.connect("Academia.db")
 
cursor = conexao.cursor()
 
cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS Aluno (
        CPF_Aluno INTEGER PRIMARY KEY,
        RG INTEGER UNIQUE,
        Telefone INTEGER,
        Nome TEXT NOT NULL,
        Objetivo_Treino TEXT,
        Tipo_Plano TEXT,
        CPF_Personal INTEGER NOT NULL,
        FOREIGN KEY (Tipo_Plano) REFERENCES Plano (Tipo_Plano),
        FOREIGN KEY (CPF_Personal) REFERENCES Personal (CPF_Personal)
    );
    '''
)
cursor.close()
print("Tabela Aluno criada com sucesso")