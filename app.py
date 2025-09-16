from flask import Flask
from src.routes import auth_bp
from src.Config.data_base import init_db, db
from dotenv import load_dotenv 
from src.routes import product_bp
import os


load_dotenv()

def create_app():
    app = Flask(__name__)


    init_db(app)

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(product_bp, url_prefix='/product')

    return app

def create_tables(app):
    with app.app_context():
        db.create_all() 

if __name__ == '__main__':
    app = create_app()
    
    create_tables(app)
    
    app.run(host="0.0.0.0", port=5000, debug=True)
