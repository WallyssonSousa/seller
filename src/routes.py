from flask import Blueprint, jsonify, make_response
from src.Application.controller.user_controller import UserController
from src.Application.controller.product_controller import ProductController

auth_bp = Blueprint("auth", __name__)
product_bp = Blueprint("product", __name__)

@auth_bp.route('/api', methods=['GET'])
def health():
    return make_response(jsonify({
        "mensagem": "API - OK; Docker - Up",
    }), 200)

@auth_bp.route('/users', methods=['POST'])
def register_user():
    return UserController.register_user()

@auth_bp.route('/users/verificar', methods=['POST'])
def verificar_codigo():
    return UserController.verificar_codigo()

@product_bp.route('/', methods=['POST'])
def register_product():
    return ProductController.register_product()