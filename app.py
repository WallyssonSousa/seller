from flask import Flask
from src.routes import auth_bp, product_bp, sale_bp
from src.Config.data_base import init_db, db
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager
from flask_cors import CORS
import os

load_dotenv()

def create_app():
    app = Flask(__name__)

    # CORS
    CORS(
        app,
        resources={r"/*": {"origins": "*"}},
        supports_credentials=True,
        allow_headers=["Content-Type", "Authorization"],
        methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"]
    )

    # Configurações
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.getenv("FLASK_SECRET_KEY")
    app.config['JWT_SECRET_KEY'] = os.getenv("JWT_SECRET_KEY")

    init_db(app)
    JWTManager(app)

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(product_bp, url_prefix='/product')
    app.register_blueprint(sale_bp, url_prefix='/sale')

    @app.route("/")
    def health():
        return {"status": "ok"}, 200

    return app


def create_tables(app):
    with app.app_context():
        db.create_all()
        print("✅ Tabelas criadas com sucesso!")


if __name__ == '__main__':
    app = create_app()
    create_tables(app)
    app.run(host="127.0.0.1", port=5000, debug=True)
