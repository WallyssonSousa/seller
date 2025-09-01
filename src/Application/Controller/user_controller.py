from flask import request, jsonify, make_response
from src.Application.Service.user_service import UserService
from src.Infrastructure.Model.user import User
from src.Config.data_base import db

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

        # Verifica se todos os campos obrigatórios foram enviados
        if not all([name, cnpj, email, celular, password]):
            return make_response(jsonify({"erro": "Campos obrigatórios faltando"}), 400)

        user = UserService.create_user(name, cnpj, email, celular, password, status)
        return make_response(jsonify({
            "mensagem": "Usuário cadastrado com sucesso. Código de verificação enviado via WhatsApp.",
            "usuario": user.to_dict()
        }), 201)
    
    # Wallysson - Método para verificar o código de ativação
    @staticmethod
    def verificar_codigo():
        data = request.get_json()
        email = data.get('email')
        code = data.get('code')

        # Busca o usuário pelo email
        user = User.query.filter_by(email=email).first()

        if not user:
            return make_response(jsonify({"erro": "Usuário não encontrado"}), 404)
        
        # Verifica se o código é válido
        if user.verificacao_code == code:
            user.status = "Ativo"
            user.verificacao_code = None  # Limpa o código após verificação
            db.session.commit()
            return make_response(jsonify({"mensagem": "Usuário verificado e ativado com sucesso"}), 200)
        
        return make_response(jsonify({"erro": "Código inválido"}), 400)
