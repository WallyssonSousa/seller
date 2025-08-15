from src.Domain.service.auth_service import AuthService

auth_service = AuthService()

class AuthController:
    def login(self):
        return auth_service.login()

    def cadastro(self):
        return auth_service.cadastro()
