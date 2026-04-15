from Torre import Torre
from Apartamento import Apartamento
from FilaEspera import FilaEspera
from ListaVagas import ListaVagas

def main():
    # Cadastra a torre
    torre = Torre()
    torre.cadastrar(1, "Torre Sul", "Av. Central, 1000")
    torre.imprimir()

    # Cadastra apartamentos (todos sem vaga no início)
    apto1 = Apartamento()
    apto1.cadastrar(101, 101, 0, torre)
    apto2 = Apartamento()
    apto2.cadastrar(102, 102, 0, torre)
    apto3 = Apartamento()
    apto3.cadastrar(103, 103, 0, torre)
    apto4 = Apartamento()
    apto4.cadastrar(104, 104, 0, torre)

    # Fila de espera e lista de ocupados
    fila = FilaEspera()
    lista = ListaVagas()

    #  Todos os aptos entram na fila
    print("\n--- Adicionando a fila de espera ---")
    fila.add(apto1)
    fila.add(apto2)
    fila.add(apto3)
    fila.add(apto4)

    #  Surgem vagas 1, 2, 3. Os primeiros da fila as recebem
    print("\n--- Atribuindo vagas 1, 2, 3 ---")
    for vaga in [1, 2, 3]:
        apto_ganhou = fila.remover(vaga)
        if apto_ganhou:
            lista.add(apto_ganhou)

    #  Liberação da vaga 2
    print("\n--- Liberacao da vaga 2 ---")
    apto_liberou = lista.remover(2)
    if apto_liberou:
        fila.add(apto_liberou)          # volta para a fila (sem vaga)
        apto_recebe = fila.remover(2)   # primeiro da fila recebe a vaga 2
        if apto_recebe:
            lista.add(apto_recebe)

    print("\n=== Estado Final ===")
    fila.imprimir()
    lista.imprimir()

if __name__ == "__main__":
    main()