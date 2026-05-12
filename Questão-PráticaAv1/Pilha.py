class Pilha:
    def __init__(self):
        self.topo = None

    def adicionar(self, veiculo):
        """Empilha um veículo (Carro ou Drone)."""
        veiculo.proximo = self.topo
        self.topo = veiculo
        print(f"Adicionado: {veiculo.marca} {veiculo.modelo}")

    def remover(self):
        """Desempilha o veículo do topo."""
        if self.topo is None:
            print("Pilha vazia! Nada a remover.")
            return None
        removido = self.topo
        self.topo = self.topo.proximo
        print(f"Removido: {removido.marca} {removido.modelo}")
        return removido

    def imprimir(self):
        """Exibe todos os elementos da pilha (do topo para a base)."""
        if self.topo is None:
            print("Pilha vazia.")
            return
        print("Pilha (do topo para a base):")
        aux = self.topo
        while aux:
            aux.imprimir()
            print("---")
            aux = aux.proximo
