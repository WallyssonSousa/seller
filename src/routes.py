from flask import Blueprint, request, jsonify
from src.Application.controller.auth_controller import AuthController

auth_bp = Blueprint('auth', __name__)
auth_controller = AuthController()

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json() or {}
    username = data.get('username')
    password = data.get('password')
    resp, status = auth_controller.login(username, password)
    return jsonify(resp), status

@auth_bp.route('/cadastro', methods=['POST'])
def cadastro():
    data = request.get_json() or {}
    username = data.get('username')
    password = data.get('password')
    resp, status = auth_controller.cadastro(username, password)
    return jsonify(resp), status