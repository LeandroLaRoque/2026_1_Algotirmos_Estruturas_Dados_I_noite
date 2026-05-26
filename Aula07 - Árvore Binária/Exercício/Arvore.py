from No import No
from Fila import Fila


class Arvore:
    def __init__(self):
        self.raiz = None

    def inserir(self, raiz: No, carro):
        if raiz is None:
            nodo = No(carro)
            if self.raiz is None:
                self.raiz = nodo
            return nodo

        if carro.placa < raiz.dado.placa:
            raiz.esq = self.inserir(raiz.esq, carro)
        elif carro.placa > raiz.dado.placa:
            raiz.dir = self.inserir(raiz.dir, carro)
        else:
            print(f"Carro com placa {carro.placa} já existe!")
        return raiz

    def buscar(self, placa):
        contador = 0
        atual = self.raiz
        while atual:
            contador += 1
            if placa == atual.dado.placa:
                return True, contador, atual.dado
            elif placa < atual.dado.placa:
                atual = atual.esq
            else:
                atual = atual.dir
        return False, contador, None

    def imprimirEmOrdem(self, raiz: No):
        if raiz is not None:
            self.imprimirEmOrdem(raiz.esq)
            print(
                f"{raiz.dado.placa} - {raiz.dado.modelo} - {raiz.dado.ano}", end=" - ")
            self.imprimirEmOrdem(raiz.dir)

    def imprimirPreOrdem(self, raiz: No):
        if raiz is not None:
            print(
                f"{raiz.dado.placa} - {raiz.dado.modelo} - {raiz.dado.ano}", end=" - ")
            self.imprimirPreOrdem(raiz.esq)
            self.imprimirPreOrdem(raiz.dir)

    def imprimirPosOrdem(self, raiz: No):
        if raiz is not None:
            self.imprimirPosOrdem(raiz.esq)
            self.imprimirPosOrdem(raiz.dir)
            print(
                f"{raiz.dado.placa} - {raiz.dado.modelo} - {raiz.dado.ano}", end=" - ")

    def imprimirReverso(self, raiz: No):
        if raiz is not None:
            self.imprimirReverso(raiz.dir)
            print(
                f"{raiz.dado.placa} - {raiz.dado.modelo} - {raiz.dado.ano}", end=" - ")
            self.imprimirReverso(raiz.esq)

    def imprimirEmNivel(self, raiz: No):
        if raiz is None:
            print("Árvore vazia")
            return
        fila = Fila()
        fila.add(raiz)

        while fila.inicio is not None:
            tamanho = fila.tamanho
            for _ in range(tamanho):
                atual = fila.remover()
                print(
                    f"{atual.dado.placa} - {atual.dado.modelo} - {atual.dado.ano}", end=" - ")
                if atual.esq is not None:
                    fila.add(atual.esq)
                if atual.dir is not None:
                    fila.add(atual.dir)
            print()
