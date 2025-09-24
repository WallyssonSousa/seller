from src.Domain.product import ProductDomain
from src.Infrastructure.Model.product import Product
from src.Config.data_base import db

class ProductService:
    @staticmethod
    def create_product(nome, preco, quantidade, status="Inactive", image=None, user_id=None):
        new_product = ProductDomain(nome, preco, quantidade, status, image)

        product = Product(
            nome = new_product.nome,
            preco = new_product.preco,
            quantidade = new_product.quantidade,
            status = new_product.status,
            image = new_product.image, 
            user_id=user_id
        )

        db.session.add(product)
        db.session.commit()
        return product
    
    @staticmethod
    def list_products():
        products = Product.query.all()
        return [p.to_dict() for p in products]
    
    @staticmethod
    def get_product_by_id(product_id, user_id):
        return Product.query.filter_by(id=product_id, user_id=user_id).first()

    @staticmethod
    def inactivate_product(product_id, user_id):
        product = Product.query.filter_by(id=product_id, user_id=user_id).first()
        if not product:
            return None
        product.status = "Inactive"
        db.session.commit()
        return product


    @staticmethod
    def update_product(product_id, user_id, nome=None, preco=None, quantidade=None, status=None, image=None):
        product = Product.query.filter_by(id=product_id, user_id=user_id).first()
        if not product:
            return None

        if nome is not None:
            product.nome = nome
        if preco is not None:
            product.preco = preco
        if quantidade is not None:
            product.quantidade = quantidade
        if status is not None:
            product.status = status
        if image is not None:
            product.image = image

        db.session.commit()
        return product
