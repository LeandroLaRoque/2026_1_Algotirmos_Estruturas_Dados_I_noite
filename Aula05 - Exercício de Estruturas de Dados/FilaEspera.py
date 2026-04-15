class FilaEspera:

    def __init__(self):
        self.inicio = None
        self.fim = None

    def add(self, apto):
        #Adiciona apartamento no final da fila.
        apto.prox = None
        if self.inicio is None:
            self.inicio = apto
        else:
            self.fim.prox = apto
        self.fim = apto
        self.imprimir()

    def remover(self, numero_vaga):
        #Remove o primeiro da fila, atribui a vaga e retorna o apto.
        if self.inicio is None:
            print("\nFila de espera vazia. Ninguém para receber a vaga.")
            return None
        apto = self.inicio
        self.inicio = self.inicio.prox
        if self.inicio is None:
            self.fim = None
        apto.prox = None   # desconecta da fila
        apto.vaga = numero_vaga
        print(f"\nApto {apto.numero} recebeu a vaga {numero_vaga} e saiu da fila.")
        self.imprimir()
        return apto

    def imprimir(self):
        print("\n----------------------")
        print("Fila de Espera - FIFO")
        if self.inicio is None:
            print("Fila Vazia")
            return
        aux = self.inicio
        txt = ""
        while aux:
            txt += f"Apto {aux.numero} (ID:{aux.id}) - "
            aux = aux.prox
        print(txt)