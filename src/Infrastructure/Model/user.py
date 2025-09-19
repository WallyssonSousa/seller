from src.Config.data_base import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    cnpj = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    celular = db.Column(db.String(20), nullable=False)
    _password = db.Column("password", db.String(200), nullable=False)
    status = db.Column(db.String(20), default="Inativo", nullable=False)
    verificacao_code = db.Column(db.String(4), nullable=True)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, plain):
        self._password = generate_password_hash(plain)

    def check_password(self, plain):
        return check_password_hash(self._password, plain)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "cnpj": self.cnpj,
            "email": self.email,
            "celular": self.celular,
            "status": self.status
        }
