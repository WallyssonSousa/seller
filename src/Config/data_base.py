from flask_sqlalchemy import SQLAlchemy

# Inicializa o SQLAlchemy
db = SQLAlchemy()

def init_db(app):
    """
    Inicializa a base de dados com o app Flask e o SQLAlchemy usando SQLite.
    """

    # SQLite: o banco será criado no arquivo local 'market_management.db'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market_management.db'
    
    # Desativa notificações de alteração de objeto (melhora performance)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Inicializa o SQLAlchemy com o app Flask
    db.init_app(app)
