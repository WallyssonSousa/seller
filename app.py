import socket

orig = socket.getaddrinfo
def force_ipv4(host, port, family=0, type=0, proto=0, flags=0):
    return orig(host, port, socket.AF_INET, type, proto, flags)
socket.getaddrinfo = force_ipv4


from flask import Flask
from src.routes import auth_bp, product_bp
from src.Config.data_base import init_db, db
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager
from src.routes import sale_bp
from flask_cors import CORS
import os

load_dotenv()

def create_app():
    app = Flask(__name__)
    CORS(
        app,
        resources={r"/*": {"origins": "*"}},
        supports_credentials=True,
        allow_headers=["Content-Type", "Authorization"],
        methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"]
    )   

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.getenv("FLASK_SECRET_KEY", "change_me")
    app.config['JWT_SECRET_KEY'] = os.getenv("JWT_SECRET_KEY", "change_me_jwt")

    init_db(app)

    jwt = JWTManager(app)

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(product_bp, url_prefix='/product')
    app.register_blueprint(sale_bp, url_prefix='/sale')

    return app

def create_tables(app):
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)
