from src.Infrastructure.Model.sale import Sale
from src.Infrastructure.Model.product import Product
from src.Infrastructure.Model.user import User
from src.Config.data_base import db

class SaleService:
    @staticmethod
    def create_sale(seller_id, product_id, quantity):
        seller = User.query.get(seller_id)
        if not seller or seller.status != "Ativo":
            return None, "Seller inativo ou não encontrado"

        product = Product.query.filter_by(id=product_id).first()
        if not product:
            return None, "Produto não encontrado"
        if product.status != "Active":
            return None, "Produto inativado"
        if product.quantidade < quantity:
            return None, "Quantidade insuficiente em estoque"

        product.quantidade -= quantity

        sale = Sale(
            product_id=product_id,
            quantity=quantity,
            price=product.preco,
            seller_id=seller_id
        )

        db.session.add(sale)
        db.session.commit()
        return sale, None

    @staticmethod
    def list_sales():
        sales = Sale.query.filter_by(status=True).all()
        return [s.to_dict() for s in sales]

    
    @staticmethod
    def get_sale_by_id(sale_id):
        sale = Sale.query.get(sale_id)
        return sale.to_dict() if sale else None
    

    @staticmethod
    def inactive_sale(sale_id): 
        sale = Sale.query.get(sale_id)
        if not sale: 
            return None, "Venda não encontrada"
        
        if sale.status == False: 
            return None, "Venda já está inativada"
        
        product = Product.query.get(sale.product_id)

        if not product: 
            return None, "Produto não encontrado"
        
        product.quantidade += sale.quantity

        sale.status = False
        db.session.commit()
        return sale, None