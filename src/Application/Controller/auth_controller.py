from flask import request, jsonify, make_response, current_app
from flask_jwt_extended import create_access_token
from src.Application.Service.user_service import UserService

class AuthController:
    @staticmethod
    def login():
        data = request.get_json() or {}
        email = data.get('email')
        password = data.get('password')

        if not all([email, password]):
            return make_response(jsonify({"erro": "email e password são obrigatórios"}), 400)

        user, err = UserService.authenticate(email, password)
        if err:
           
            return make_response(jsonify({"erro": err}), 401)

        additional_claims = {"role": "seller"} 
        access_token = create_access_token(identity=str(user.id), additional_claims={"role": "seller"})
        return make_response(jsonify({
            "access_token": access_token,
            "user": user.to_dict()
        }), 200)
