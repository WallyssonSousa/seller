from src.Config.data_base import db 

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    cnpj = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    celular = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), default="Inativo", nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "cnpj": self.cnpj,
            "email": self.email,
            "celular": self.celular,
            "password": self.password,
            "status": self.status
        }