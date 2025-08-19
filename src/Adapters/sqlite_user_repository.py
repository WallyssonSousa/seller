import sqlite3
from Domain.service.user_service import User
from Domain.service.user_repository import UserRepository

class UserRepositorySqlite(UserRepository):
    def __init__(self, db_path="users.db"):
        self.conn = sqlite3.connect(db_path)
        self._create_table()
        
    def _create_table(self):
        self.conn.execute(""""
            CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        cnpj TEXT,
        email TEXT UNIQUE,
        celular TEXT,
        senha TEXT,
        status TEXT
    )
    """)
        
    def save(self, user):
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO usuarios (nome, cnpj, email, celular, senha, status)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (user.nome, user.cnpj, user.email, user.celular, user.senha, user.status)
        )
        self.conn.commit()
        return cursor.lastrowid
    
    def search_email(self, email):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE email = ?", (email,))
        linha = cursor.fetchone()
        if linha:
            return User(
                nome=linha[1],
                cnpj=linha[2],
                email=linha[3],
                celular=linha[4],
                senha=linha[5],
                status=linha[6]
            )
        return None
    
    def list_all(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM usuarios")
        linhas = cursor.fetchall()
        usuarios = []
        for linha in linhas:
            usuarios.append(User(
                nome=linha[1],
                cnpj=linha[2],
                email=linha[3],
                celular=linha[4],
                senha=linha[5],
                status=linha[6]
            ))
        return usuarios