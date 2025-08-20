from flask import Blueprint, request, jsonify
from Domain.service.user_service import User
from Adapters.sqlite_user_repository import UserRepositorySqlite

routes = Blueprint("routes", __name__)

repositorio = UserRepositorySqlite()

@routes.route("/cadastro", methods=["POST"])
def register():
    dados = request.json

    campos_necessarios = ["nome", "cnpj", "email", "celular", "senha"]
    for campo in campos_necessarios:
        if campo not in dados:
            return jsonify({"erro": f"Campo {campo} é obrigatório"}), 400

    usuario = User(
        nome=dados["nome"],
        cnpj=dados["cnpj"],
        email=dados["email"],
        celular=dados["celular"],
        senha=dados["senha"]
    )

    if not usuario.validar_email():
        return jsonify({"erro": "Email inválido"}), 400
    if not usuario.validar_cnpj():
        return jsonify({"erro": "CNPJ inválido"}), 400

    try:
        usuario_id = repositorio.salvar(usuario)
        return jsonify({"mensagem": "Usuário cadastrado com sucesso", "id": usuario_id}), 201
    except Exception as e:
        return jsonify({"erro": f"Falha ao cadastrar usuário: {str(e)}"}), 500
