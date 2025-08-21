from flask import Flask
from src.routes import auth_bp
from src.Config.data_base import init_db

def create_app():
    app = Flask(__name__)

    # Inicializa o banco
    init_db(app)

    # Registra as rotas com prefixo /auth
    app.register_blueprint(auth_bp, url_prefix='/auth')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)
