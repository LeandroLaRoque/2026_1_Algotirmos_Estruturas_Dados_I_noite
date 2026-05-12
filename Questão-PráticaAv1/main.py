from Carro import Carro
from Drone import Drone
from Pilha import Pilha

pilha_carros = Pilha()
pilha_drones = Pilha()

while True:
    print("\n===== MENU =====")
    print("1 - Adicionar carro")
    print("2 - Remover carro")
    print("3 - Adicionar drone")
    print("4 - Remover drone")
    print("5 - Imprimir pilha de carros")
    print("6 - Imprimir pilha de drones")
    print("0 - Sair")
    opcao = input("Escolha: ")

    if opcao == "1":
        marca = input("Marca do carro: ")
        modelo = input("Modelo: ")
        portas = input("Número de portas: ")
        carro = Carro(marca, modelo, portas)
        pilha_carros.adicionar(carro)

    elif opcao == "2":
        pilha_carros.remover()

    elif opcao == "3":
        marca = input("Marca do drone: ")
        modelo = input("Modelo: ")
        qtd = input("Quantidade de hélices: ")
        drone = Drone(marca, modelo, qtd)
        pilha_drones.adicionar(drone)

    elif opcao == "4":
        pilha_drones.remover()

    elif opcao == "5":
        print("\n--- PILHA DE CARROS ---")
        pilha_carros.imprimir()

    elif opcao == "6":
        print("\n--- PILHA DE DRONES ---")
        pilha_drones.imprimir()

    elif opcao == "0":
        print("Encerrando...")
        break

    else:
        print("Opção inválida!")
