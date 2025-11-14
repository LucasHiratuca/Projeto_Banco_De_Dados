# Services/Relacionamento_Aluno_Aula.py 
 
import sqlite3
 
conexao = sqlite3.connect("Academia.db")
 
cursor = conexao.cursor()
 
cursor.execute(
    '''
        CREATE TABLE IF NOT EXISTS Aluno_Aula(
            ID_Aula INTEGER NOT NULL,
            CPF_Aluno INTEGER NOT NULL UNIQUE,
            PRIMARY KEY (ID_Aula, CPF_Aluno),
            FOREIGN KEY (ID_Aula) REFERENCES Aula (ID_Aula),
            FOREIGN KEY (CPF_Aluno) REFERENCES Aluno (CPF_Aluno)
        );
    '''
)
cursor.close()
print("Tabela Aluno_Aula criada com sucesso")