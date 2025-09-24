from twilio.rest import Client
import os 

class SMSService:
    def __init__(self, count_sid, auth_token, from_number):
        self.client = Client(count_sid, auth_token)
        self.from_number = from_number 

    def enviar_mensagem(self, to_number, code):
        try:
            message = self.client.messages.create(
                from_=self.from_number, 
                body=f"Seu código de verificação é: {code}",
                to=to_number
            )  
            print(f"Mensagem enviada para {to_number}: {message.sid}")
            return message.sid
        except Exception as e:
            import traceback
            traceback.print_exc()
            print(f"[Twilio] Erro ao enviar SMS: {e}")
            raise
