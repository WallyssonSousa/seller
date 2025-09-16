from flask import Blueprint, jsonify, make_response
from src.Application.Controller.user_controller import UserController

auth_bp = Blueprint("auth", __name__)

@auth_bp.route('/api', methods=['GET'])
def health():
    return make_response(jsonify({
        "mensagem": "API - OK"
    }), 200)

@auth_bp.route('/users', methods=['POST'])
def register_user():
    return UserController.register_user()
