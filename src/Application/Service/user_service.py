# Wallysson
import random
from twilio.rest import Client
#
from src.Domain.user import UserDomain
from src.Infrastructure.Model.user import User
from src.Config.data_base import db 
import os
from src.Infrastructure.http.whats_app import WhatsAppService

class UserService:
    @staticmethod
    def create_user(name, cnpj, email, celular, password, status="Inativo"):
        new_user = UserDomain(name, cnpj, email, celular, password, status)

        codigo_de_verificao = str(random.randint(1000, 9999))

        user = User(
            name=new_user.name,
            cnpj=new_user.cnpj,
            email=new_user.email,
            celular=new_user.celular,
            password=new_user.password,
            status=new_user.status,
            verificacao_code=codigo_de_verificao
        )

        db.session.add(user)
        db.session.commit()


        whatsapp = WhatsAppService(
            os.getenv("TWILIO_ACCOUNT_SID"),
            os.getenv("TWILIO_AUTH_TOKEN"),
            os.getenv("TWILIO_PHONE_NUMBER")  
        )
        whatsapp.enviar_mensagem(celular, codigo_de_verificao)

        return user

