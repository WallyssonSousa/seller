class ProductDomain:
    def __init__(self, nome, preco, quantidade, status="Inactive", image=None):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.status = status
        self.image = image

    def to_dict(self):
        return {
            "nome": self.nome,
            "preco": self.preco,
            "quantidade": self.quantidade,
            "status": self.status,
            "image": self.image
        }
