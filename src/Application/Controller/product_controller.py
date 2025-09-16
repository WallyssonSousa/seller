from flask import request, jsonify, make_response
from src.Application.Service.product_service import ProductService

class ProductController:
    @staticmethod
    def register_product():
        data = request.get_json()

        nome = data.get('nome')
        preco = data.get('preco')
        quantidade = data.get('quantidade')
        status = data.get('status', 'Inactive')
        image = data.get('image')

        product = ProductService.create_product(nome, preco, quantidade, status, image)

        if not all([nome, preco, quantidade]):
            return make_response(jsonify({"error": "Missing required fields"}), 400)
        
        return make_response(jsonify({
            "message": "Product successfully registered",
            "product": product.to_dict()
        }), 201)
