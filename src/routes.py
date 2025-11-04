from flask import Blueprint, jsonify, make_response
from src.application.controller.user_controller import UserController
from src.application.controller.auth_controller import AuthController
from src.application.controller.product_controller import ProductController
from src.application.controller.sale_controller import SaleController

auth_bp = Blueprint("auth", __name__)
product_bp = Blueprint("product", __name__)
sale_bp = Blueprint("sale", __name__)

@auth_bp.route('/api', methods=['GET'])
def health():
    return make_response(jsonify({
        "mensagem": "API - OK",
    }), 200)

""" Registrar, verificar e listar usuários """

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

@auth_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    return UserController.update_user(user_id)

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

@product_bp.route('/<int:product_id>', methods=['GET'])
def get_product(product_id):
    return ProductController.get_product(product_id)

@product_bp.route('/<int:product_id>/inactivate', methods=['PATCH'])
def inactivate_product(product_id):
    return ProductController.inactivate_product(product_id)

@product_bp.route('/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    return ProductController.update_product(product_id)

" Sales "

@sale_bp.route('/', methods=['POST'])
def create_sale():
    return SaleController.create_sale()

@sale_bp.route('/', methods=['GET'])
def list_sales():
    return SaleController.list_sales()

@sale_bp.route('/<int:sale_id>', methods=['GET'])
def get_sale(sale_id):
    return SaleController.get_sale(sale_id)