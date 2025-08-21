from flask import request, jsonify, make_response
from src.Application.Service.user_service import UserService

class UserController:
    @staticmethod
    def register_user():
        data = request.get_json()
        
        name = data.get('name')
        cnpj = data.get('cnpj')
        email = data.get('email')
        celular = data.get('celular')
        password = data.get('password')
        status = data.get('status', 'Inativo')  # Default: Inativo

        if not all([name, cnpj, email, celular, password]):
            return make_response(jsonify({"erro": "Missing required fields"}), 400)

        user = UserService.create_user(name, cnpj, email, celular, password, status)
        return make_response(jsonify({
            "mensagem": "Usuário salvo com sucesso",
            "usuario": user.to_dict()
        }), 201)
