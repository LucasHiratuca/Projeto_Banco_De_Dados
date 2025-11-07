# Services/Tabela_Treino.py 
 
import sqlite3
 
conexao = sqlite3.connect("Academia.db")
 
cursor = conexao.cursor()
 
cursor.execute(
    '''
        CREATE TABLE Treino(
            ID_Treino INTEGER (11) NOT NULL UNIQUE PRIMARY KEY,
            Alongamentos VARCHAR (255),
            Exercicios_Aerobicos VARCHAR (255),
            Exercicios_Maquina VARCHAR (255),
            Carga INTEGER (11)
            CPF_Aluno INTEGER (11) UNIQUE NOT NULL
            FOREIGN KEY CPF_Aluno REFERENCES Aluno(CPF_Aluno)
        ) ENGINE=InnoDB;
    '''
)
cursor.close()
print("Tabela Treino criada com sucesso")