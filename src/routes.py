from flask import Blueprint, jsonify
from src.Application.controller.auth_controller import AuthController

auth_bp = Blueprint('auth', __name__)
auth_controller = AuthController()

@auth_bp.route('/login', methods=['GET'])
def login():
    return jsonify(auth_controller.login())

@auth_bp.route('/cadastro', methods=['GET'])
def cadastro():
    return jsonify(auth_controller.cadastro())
