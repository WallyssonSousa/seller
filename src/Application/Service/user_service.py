import random, os
from src.Domain.user import UserDomain
from src.Infrastructure.Model.user import User
from src.Config.data_base import db
from src.Infrastructure.http.whats_app import WhatsAppService

def formatar_celular(numero: str) -> str:
    numero = numero.strip()
    if not numero.startswith("+"):
        numero = "+55" + numero
    return numero


class UserService:
    @staticmethod
    def create_user(name, cnpj, email, celular, password, status="Inativo"):
        if User.query.filter((User.email == email) | (User.cnpj == cnpj)).first():
            raise ValueError("Email ou CNPJ já cadastrado")

        new_user = UserDomain(name, cnpj, email, celular, password, status)

        codigo_de_verificacao = str(random.randint(1000, 9999)).zfill(4)

        user = User(
            name=new_user.name,
            cnpj=new_user.cnpj,
            email=new_user.email,
            celular=new_user.celular,
            status=new_user.status,
            verificacao_code=codigo_de_verificacao
        )
        user.password = new_user.password

        db.session.add(user)
        db.session.commit()

        celular_formatado = formatar_celular(celular)

        whatsapp = WhatsAppService(
            os.getenv("TWILIO_ACCOUNT_SID"),
            os.getenv("TWILIO_AUTH_TOKEN"),
            os.getenv("TWILIO_PHONE_NUMBER")
        )
        whatsapp.enviar_mensagem(celular_formatado, codigo_de_verificacao)

        return user

    @staticmethod
    def activate_user_by_code(email, code):
        user = User.query.filter_by(email=email).first()
        if not user:
            return None, "Usuário não encontrado"

        if user.verificacao_code == code:
            user.status = "Ativo"
            user.verificacao_code = None
            db.session.commit()
            return user, None

        return None, "Código inválido"

    @staticmethod
    def authenticate(email, password):
        user = User.query.filter_by(email=email).first()
        if not user:
            return None, "Usuário não encontrado"
        if user.status != "Ativo":
            return None, "Usuário não ativado"
        if not user.check_password(password):
            return None, "Credenciais inválidas"
        return user, None

    @staticmethod
    def list_users():
        users = User.query.all()
        return [u.to_dict() for u in users]
    
    @staticmethod
    def get_user_by_id(user_id):
        user = User.query.get(user_id)
        return user.to_dict() if user else None