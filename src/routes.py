from flask import Blueprint, jsonify
from src.Application.Controller.auth_controller import AuthController
from src.Application.Controller.product_controller import ProductController
from src.Application.Controller.user_controller import UserController
from flask import make_response, request

auth_bp = Blueprint("auth", __name__)
product_bp = Blueprint("product", __name__)

@auth_bp.route('/api', methods=['GET'])
def health():
    return make_response(jsonify({
        "mensagem": "API - OK",
    }), 200)

@auth_bp.route('/users', methods=['POST'])
def register_user():
    return UserController.register_user()

@auth_bp.route('/users/verificar', methods=['POST'])
def verificar_codigo():
    return UserController.verificar_codigo()

@auth_bp.route('/login', methods=['POST'])
def login():
    return jsonify(AuthController.login())

@auth_bp.route('/cadastro', methods=['GET'])
def cadastro():
    return jsonify(AuthController.cadastro())

@product_bp.route('/products', methods=['GET'])
def listar_produtos():
    return ProductController.listar_produtos()

@auth_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    return UserController.get_user_by_id(user_id)
