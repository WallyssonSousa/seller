from flask import Flask
from src.routes import auth_bp

app = Flask(__name__)

# Registrando as rotas
app.register_blueprint(auth_bp, url_prefix='/auth')

if __name__ == '__main__':
    app.run(debug=True)
