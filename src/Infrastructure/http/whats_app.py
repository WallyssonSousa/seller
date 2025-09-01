# Wallysson - classe para gerenciar o envio de mensagem 
from twilio.rest import Client

class WhatsAppService:
    def __init__(self, conta_sid: str, auth_token: str, from_numero: str):
        self.cliente = Client(conta_sid, auth_token)
        self.from_numero = f"whatsapp:{from_numero}"

    def enviar_mensagem(self, to_numero: str, codigo: str):
        """ Envia o código de verificacao pelo WhatsApp """
        message = self.cliente.messages.create(
            from_=self.from_numero,
            body=f"Seu código de verificação é: {codigo}",
            to=f"whatsapp:{to_numero}"
        )
        return message.sid   
