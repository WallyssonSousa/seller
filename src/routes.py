from flask import Blueprint, jsonify, make_response
from src.Application.controller.user_controller import UserController

# Criando o Blueprint
auth_bp = Blueprint("auth", __name__)

# Health check
@auth_bp.route('/api', methods=['GET'])
def health():
    return make_response(jsonify({
        "mensagem": "API - OK; Docker - Up",
    }), 200)

# Cadastro de usuário
@auth_bp.route('/users', methods=['POST'])
def register_user():
    return UserController.register_user()

# Ativa Uuário 
@auth_bp.route('/users/verificar', methods=['POST'])
def verificar_codigo():
    return UserController.verificar_codigo()