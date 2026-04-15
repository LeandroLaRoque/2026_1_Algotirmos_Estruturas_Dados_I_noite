from Torre import Torre

class Apartamento:
    def __init__(self, id_ap=0, numero_ap=0, vaga=0, torre=None):
        self.id = id_ap
        self.numero = numero_ap
        self.vaga = vaga          # 0 = sem vaga, >0 = número da vaga
        self.torre = torre
        self.prox = None          # usado para encadear na fila ou lista

    def cadastrar(self, id_ap, numero_ap, vaga, torre):
        self.id = id_ap
        self.numero = numero_ap
        self.vaga = vaga
        self.torre = torre
        self.prox = None

    def imprimir(self):
        status_vaga = self.vaga if self.vaga > 0 else "sem vaga"
        print(f"Apto {self.numero} (ID:{self.id}) | Vaga: {status_vaga} | Torre: {self.torre.nome}")