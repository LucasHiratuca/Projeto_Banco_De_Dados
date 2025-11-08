# Services/Tabela_Aluno.py 
 
import sqlite3
 
conexao = sqlite3.connect("Academia.db")
 
cursor = conexao.cursor()
 
cursor.execute(
    '''
        CREATE TABLE Aluno(
            CPF_Aluno INTEGER (11) UNIQUE PRIMARY KEY NOT NULL
            RG_Aluno INTEGER (11) UNIQUE NOT NULL,
            Telefone_Aluno INTEGER (255) NOT NULL,
            Nome_Aluno VARCHAR (255) NOT NULL,
            Objetivo_Treino VARCHAR (255),
            Tipo_Plano VARCHAR (255),
            CPF_Personal INTEGER (11) NOT NULL UNIQUE,
            FOREIGN KEY Tipo_Plano REFERENCES Plano(Tipo_Plano),
            FOREIGN KEY CPF_Personal REFERENCES Personal(CPF_Personal)
        ) ENGINE=InnoDB;
    '''
)
cursor.close()
print("Tabela Aluno criada com sucesso")