from flask import Flask
from src.routes import auth_bp, product_bp
from src.Config.data_base import init_db, db
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager
from src.routes import sale_bp
import os

load_dotenv()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market_management.db'
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
    create_tables(app)
    app.run(host="0.0.0.0", port=5000, debug=True)
