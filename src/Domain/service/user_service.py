class User:
    def __init__(self, name, cnpj, email, phone, password, status="Inativo"):
        self.name = name
        self.cnpj = cnpj
        self.email = email
        self.phone = phone
        self.password = password
        self.status = status
        
    def activate(self):
        self.status = "Ativo"
        
    def validate_email(self):
        return "@" in self.email
    
    def validate_cnpj(self):
        return len(self.cnpj) ==14 and self.cnpj.isdigit()
                   
    