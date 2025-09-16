from src.Domain.product import ProductDomain
from src.Infrastructure.Model.product import Product
from src.Config.data_base import db

class ProductService:
    @staticmethod
    def create_product(nome, preco, quantidade, status="Inactive", image=None):
        new_product = ProductDomain(nome, preco, quantidade, status, image)

        product = Product(
            nome = new_product.nome,
            preco = new_product.preco,
            quantidade = new_product.quantidade,
            status = new_product.status,
            image = new_product.image
        )

        db.session.add(product)
        db.session.commit()
        return product