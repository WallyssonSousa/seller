from src.Config.data_base import db

class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(50), nullable=False, default="Inactive")
    image = db.Column(db.String(255), nullable=True)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    def to_dict(self):
        return {
            "id": self.id, 
            "nome": self.nome,
            "preco": self.preco, 
            "quantidade": self.quantidade, 
            "status": self.status,
            "image": self.image,
            "user_id": self.user_id
        }
    
    