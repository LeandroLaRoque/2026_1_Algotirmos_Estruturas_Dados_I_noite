class ListaVagas:
    
    def __init__(self):
        self.inicio = None

    def add(self, apto):
        #Insere o apartamento na lista mantendo ordem crescente pelo número da vaga.
        apto.prox = None
        if self.inicio is None:
            self.inicio = apto
        else:
            # Insere na posição correta (ordenado por vaga)
            if apto.vaga < self.inicio.vaga:
                apto.prox = self.inicio
                self.inicio = apto
            else:
                ant = self.inicio
                aux = self.inicio.prox
                while aux:
                    if apto.vaga < aux.vaga:
                        apto.prox = aux
                        ant.prox = apto
                        break
                    else:
                        ant = aux
                        aux = aux.prox
                if aux is None:
                    ant.prox = apto
        self.imprimir()

    def remover(self, numero_vaga):
        #Remove o apartamento que possui a vaga informada e o retorna (com vaga zerada).
        if self.inicio is None:
            print("Lista de vagas ocupadas está vazia.")
            return None

        # Ser for o primeiro
        if numero_vaga == self.inicio.vaga:
            removido = self.inicio
            self.inicio = self.inicio.prox
            removido.prox = None
            print(f"\nApto {removido.numero} liberou a vaga {numero_vaga}.")
            removido.vaga = 0
            self.imprimir()
            return removido

        # Procura nos demais
        ant = self.inicio
        aux = self.inicio.prox
        while aux:
            if numero_vaga == aux.vaga:
                removido = aux
                ant.prox = aux.prox
                removido.prox = None
                print(f"\nApto {removido.numero} liberou a vaga {numero_vaga}.")
                removido.vaga = 0
                self.imprimir()
                return removido
            ant = aux
            aux = aux.prox

        print(f"\nVaga {numero_vaga} não encontrada na lista de ocupados.")
        return None

    def imprimir(self):
        print("\n----------------------")
        print("Lista de Apartamentos com Vaga (ordenada por numero da vaga)")
        if self.inicio is None:
            print("Lista Vazia")
            return
        aux = self.inicio
        while aux:
            print(f"Apto {aux.numero} | Vaga: {aux.vaga} | Torre: {aux.torre.nome}")
            aux = aux.prox