from flask import request, jsonify, make_response
from src.application.Service.product_service import ProductService
from src.Infrastructure.Model.user import User
from src.Config.data_base import db
from flask_jwt_extended import jwt_required, get_jwt_identity

class ProductController:
    @staticmethod
    @jwt_required()
    def register_product():
        data = request.get_json() or {}

        user_id = get_jwt_identity()
        user = User.query.get(user_id)
        if not user or user.status != "Ativo":
            return make_response(jsonify({"error": "Usuário não autorizado"}), 403)

        nome = data.get('nome')
        preco = data.get('preco')
        quantidade = data.get('quantidade')
        status = data.get('status', 'Inactive')
        image = data.get('image')

        if not all([nome, preco, quantidade]):
            return make_response(jsonify({"error": "Missing required fields"}), 400)

        product = ProductService.create_product(nome, preco, quantidade, status, image, user_id=user_id)

        return make_response(jsonify({
            "message": "Product successfully registered",
            "product": product.to_dict()
        }), 201)
    
    
    @staticmethod
    @jwt_required()
    def list_products():
        products = ProductService.list_products()
        return make_response(jsonify({
            "products": products
        }), 200)

    @staticmethod
    @jwt_required()
    def get_product(product_id):
        user_id = get_jwt_identity()
        product = ProductService.get_product_by_id(product_id, user_id)
        if not product:
            return make_response(jsonify({"error": "Produto não encontrado ou não pertence ao usuário"}), 404)

        return make_response(jsonify({"product": product.to_dict()}), 200)

    @staticmethod
    @jwt_required()
    def inactivate_product(product_id):
        user_id = get_jwt_identity()
        product = ProductService.inactivate_product(product_id, user_id)
        if not product:
            return make_response(jsonify({"error": "Produto não encontrado ou não pertence ao usuário"}), 404)

        return make_response(jsonify({
            "message": "Produto inativado com sucesso",
            "product": product.to_dict()
        }), 200)
    
    @staticmethod
    @jwt_required()
    def update_product(product_id):
        user_id = get_jwt_identity()
        data = request.get_json() or {}

        product = ProductService.update_product(
            product_id,
            user_id,
            nome=data.get('nome'),
            preco=data.get('preco'),
            quantidade=data.get('quantidade'),
            status=data.get('status'),
            image=data.get('image')
        )

        if not product:
            return make_response(jsonify({"error": "Produto não encontrado ou não pertence ao usuário"}), 404)

        return make_response(jsonify({
            "message": "Produto atualizado com sucesso",
            "product": product.to_dict()
        }), 200)

        