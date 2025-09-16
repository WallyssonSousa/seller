from flask import Flask
from src.routes import auth_bp
from flask_jwt_extended import JWTManager


app = Flask(__name__)


app.config["JWT_SECRET_KEY"] = "27d25a37-lnpw-4eb7-b76c-40a7321b45db" 
jwt = JWTManager(app)

# Registrando as rotas
app.register_blueprint(auth_bp, url_prefix='/auth')

if __name__ == '__main__':
    app.run(debug=True)
