from flask import Flask
from src.routes import auth_bp
from src.Config.data_base import init_db, db
from src.Infrastructure.Model.user import User

def create_app():
    app = Flask(__name__)

    # Inicializa o banco
    init_db(app)

    # Registra as rotas com prefixo /auth
    app.register_blueprint(auth_bp, url_prefix='/auth')

    return app

def create_tables(app):
    """
    Cria as tabelas do banco automaticamente com SQLAlchemy.
    """
    with app.app_context():
        db.create_all()  # Cria todas as tabelas definidas nos Models

if __name__ == '__main__':
    app = create_app()
    
    # Cria as tabelas SQLite
    create_tables(app)
    
    # Roda a API
    app.run(host="0.0.0.0", port=5000, debug=True)
