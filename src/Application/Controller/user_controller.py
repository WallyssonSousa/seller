from flask import request, jsonify, make_response
from src.Application.Service.user_service import UserService

class UserController:
    @staticmethod
    def register_user():
        data = request.get_json() or {}

        name = data.get('name')
        cnpj = data.get('cnpj')
        email = data.get('email')
        celular = data.get('celular')
        password = data.get('password')
        status = data.get('status', 'Inativo')

        if not all([name, cnpj, email, celular, password]):
            return make_response(jsonify({"erro": "Campos obrigatórios faltando"}), 400)

        try:
            user = UserService.create_user(name, cnpj, email, celular, password, status)
            return make_response(jsonify({
                "mensagem": "Usuário cadastrado com sucesso. Código de verificação enviado via WhatsApp.",
                "usuario": user.to_dict()
            }), 201)
        except ValueError as e:
            return make_response(jsonify({"erro": str(e)}), 400)
        except Exception as e:
            import traceback
            traceback.print_exc()  
            return make_response(jsonify({"erro": f"Erro ao cadastrar usuário: {str(e)}"}), 500)


    @staticmethod
    def verificar_codigo():
        data = request.get_json() or {}
        email = data.get('email')
        code = data.get('code')

        if not all([email, code]):
            return make_response(jsonify({"erro": "email e code são obrigatórios"}), 400)

        user, err = UserService.activate_user_by_code(email, code)
        if err:
            return make_response(jsonify({"erro": err}), 400)
        return make_response(jsonify({"mensagem": "Usuário verificado e ativado com sucesso", "usuario": user.to_dict()}), 200)

    @staticmethod
    def list_users():
        users = UserService.list_users()
        return make_response(jsonify({
            "users": users
        }), 200)
    
    @staticmethod
    def get_user_by_id(user_id):
        user = UserService.get_user_by_id(user_id)
        if not user:
            return make_response(jsonify({"erro": "Usuário não encontrado"}), 404)
        return make_response(jsonify({"user": user}), 200)