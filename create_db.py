import sqlite3
import os

DB_PATH = os.path.join(os.getcwd(), "sellers.db")

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()
cursor.execute("INSERT INTO sellers (username, password, active) VALUES (?, ?, ?)", ('pedro', '1234', 1))
conn.commit()

conn.commit()
conn.close()
print("Banco criado/atualizado em:", DB_PATH)
#criação do banco de dadas os sellers.db com a tabela sellers para textes
