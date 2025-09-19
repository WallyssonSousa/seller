from flask import request, jsonify, make_response
from src.Application.Service.product_service import ProductService
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

        product = ProductService.create_product(nome, preco, quantidade, status, image)

        return make_response(jsonify({
            "message": "Product successfully registered",
            "product": product.to_dict()
        }), 201)
    def listar_produtos():
        try:
            produtos = Product.query.all()  # pega todos os produtos diretamente do banco de dados
            produtos_list = [p.to_dict() for p in produtos]
            return make_response(jsonify(produtos_list), 200)
        except Exception as e:
            return make_response(jsonify({"erro": str(e)}), 500)
