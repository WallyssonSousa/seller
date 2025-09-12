import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
import os

DB_PATH = os.path.join(os.getcwd(), "sellers.db")

class AuthController:
    def get_db(self):
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        return conn

    def login(self, username, password):
        if not username or not password:
            return {"error": "username e password são obrigatórios"}, 400

        conn = self.get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT password, active FROM sellers WHERE username = ?", (username,))
        row = cursor.fetchone()
        conn.close()

        if row is None:
            return {"error": "Usuário não encontrado"}, 404

        stored_password_hash = row["password"]
        try:
            active = int(row["active"])
        except:
            active = 0

        if not check_password_hash(stored_password_hash, password):
            return {"error": "Senha incorreta"}, 401

        if active != 1:
            return {"error": "Conta inativa"}, 403

        return {"message": "Login realizado com sucesso!"}, 200

    def cadastro(self, username, password):
        if not username or not password:
            return {"error": "username e password são obrigatórios"}, 400

        password_hash = generate_password_hash(password)
        conn = self.get_db()
        cursor = conn.cursor()

        try:
            cursor.execute(
                "INSERT INTO sellers (username, password, active) VALUES (?, ?, ?)",
                (username, password_hash, 1)
            )
            conn.commit()
            conn.close()
            return {"message": "Usuário cadastrado com sucesso!"}, 201
        except sqlite3.IntegrityError:
            conn.close()
            return {"error": "Usuário já existe"}, 409
DB_PATH = os.path.join(os.getcwd(), "sellers.db")