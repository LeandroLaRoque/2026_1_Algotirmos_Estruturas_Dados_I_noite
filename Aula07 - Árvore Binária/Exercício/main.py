from Carro import Carro
from Arvore import Arvore

arvore = Arvore()

while True:
    print("\n===== MENU =====")
    print("1 - Adicionar carro")
    print("2 - Imprimir em ordem (ERD)")
    print("3 - Imprimir pré ordem (RED)")
    print("4 - Imprimir pós ordem (EDR)")
    print("5 - Imprimir ordem reversa (DRE)")
    print("6 - Imprimir em nível")
    print("7 - Procurar carro")
    print("0 - Sair")
    opcao = input("Escolha: ")

    if opcao == "1":
        modelo = input("Modelo: ")
        placa = input("Placa: ")
        ano = input("Ano: ")
        carro = Carro(modelo, placa, ano)
        arvore.inserir(arvore.raiz, carro)

    elif opcao == "2":
        print("\n--- Em ordem (ERD) ---")
        arvore.imprimirEmOrdem(arvore.raiz)
        print()

    elif opcao == "3":
        print("\n--- Pré ordem (RED) ---")
        arvore.imprimirPreOrdem(arvore.raiz)
        print()

    elif opcao == "4":
        print("\n--- Pós ordem (EDR) ---")
        arvore.imprimirPosOrdem(arvore.raiz)
        print()

    elif opcao == "5":
        print("\n--- Ordem reversa (DRE) ---")
        arvore.imprimirReverso(arvore.raiz)
        print()

    elif opcao == "6":
        print("\n--- Em nível ---")
        arvore.imprimirEmNivel(arvore.raiz)

    elif opcao == "7":
        placa = input("Digite a placa do carro: ")
        encontrado, iteracoes, carro = arvore.buscar(placa)
        if encontrado:
            print(f"Carro ENCONTRADO após {iteracoes} iteração(ões).")
            print(
                f"Placa: {carro.placa} | Modelo: {carro.modelo} | Ano: {carro.ano}")
        else:
            print(
                f"Carro com placa {placa} NÃO encontrado após {iteracoes} iteração(ões).")

    elif opcao == "0":
        print("Encerrando...")
        break

    else:
        print("Opção inválida!")
