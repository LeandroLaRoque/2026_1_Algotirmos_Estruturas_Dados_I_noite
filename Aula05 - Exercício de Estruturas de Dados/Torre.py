class Torre:

    def __init__(self, id_torre=0, nome="", endereco=""):
        self.id = id_torre
        self.nome = nome
        self.endereco = endereco

    def cadastrar(self, id_torre, nome, endereco):
        self.id = id_torre
        self.nome = nome
        self.endereco = endereco

    def imprimir(self):
        print(f"Torre {self.id}: {self.nome} - {self.endereco}")