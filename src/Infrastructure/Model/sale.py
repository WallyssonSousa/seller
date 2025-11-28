from src.Config.data_base import db
from datetime import datetime

class Sale(db.Model):
    __tablename__ = "sales"

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    status = db.Column(db.Boolean, default=True)
    seller_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    product = db.relationship("Product")
    seller = db.relationship("User")
    
    def to_dict(self):
        return {
            "id": self.id,
            "product_id": self.product_id,
            "product_nome": self.product.nome,
            "quantity": self.quantity,
            "price": self.price,
            "status": self.status,
            "seller_id": self.seller_id,
            "seller_name": self.seller.name,
            "created_at": self.created_at.isoformat()
        }