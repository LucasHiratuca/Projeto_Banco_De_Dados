# Services/Relacionamento_Treino_Maquina.py 
 
import sqlite3
 
conexao = sqlite3.connect("Academia.db")
 
cursor = conexao.cursor()
 
cursor.execute(
    '''
        CREATE TABLE IF NOT EXISTS Treino_Maquina(
            ID_Treino INTEGER NOT NULL,
            Nome_Maquina TEXT NOT NULL,
            PRIMARY KEY (ID_Treino, Nome_Maquina),
            FOREIGN KEY (ID_Treino) REFERENCES Treino (ID_Treino),
            FOREIGN KEY (Nome_Maquina) REFERENCES Maquina (Nome_Maquina)
        );
    '''
)
cursor.close()
print("Tabela Treino_Maquina criada com sucesso")