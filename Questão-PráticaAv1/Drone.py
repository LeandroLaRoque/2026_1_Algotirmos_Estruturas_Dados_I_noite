from Veiculo import Veiculo


class Drone(Veiculo):
    def __init__(self, marca, modelo, quantidade_helice):
        super().__init__(marca, modelo)
        self.__quantidade_helice = quantidade_helice

    def imprimir(self):
        super().imprimir()
        print(f"Quantidade de hélices: {self.__quantidade_helice}")
