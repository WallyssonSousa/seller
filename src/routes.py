from flask import Blueprint, jsonify, make_response
from src.Application.Controller.user_controller import UserController

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
