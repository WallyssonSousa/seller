from flask import Blueprint, jsonify, make_response
from src.Application.controller.user_controller import UserController
from src.Application.controller.auth_controller import AuthController
from src.Application.controller.product_controller import ProductController

auth_bp = Blueprint("auth", __name__)
product_bp = Blueprint("product", __name__)

@auth_bp.route('/api', methods=['GET'])
def health():
    return make_response(jsonify({
        "mensagem": "API - OK",
    }), 200)

""" Registrar e verificar usuários """

@auth_bp.route('/users', methods=['POST'])
def register_user():
    return UserController.register_user()

@auth_bp.route('/users/verificar', methods=['POST'])
def verificar_codigo():
    return UserController.verificar_codigo()

@auth_bp.route('/users', methods=['GET'])
def list_users():
    return UserController.list_users()

@auth_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    return UserController.get_user_by_id(user_id)

""" Login """

@auth_bp.route('/login', methods=['POST'])
def login():
    return AuthController.login()

""" Produtos """

@product_bp.route('/', methods=['POST'])
def register_product():
    return ProductController.register_product()

@product_bp.route('/', methods=['GET'])
def list_products():
    return ProductController.list_products()

