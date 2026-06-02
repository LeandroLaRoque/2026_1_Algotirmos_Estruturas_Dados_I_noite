from busca import busca_seq, busca_bin

vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

print("Vetor ordenado (1 a 20):")
print(vetor)
print("-" * 50)

valor = int(input("Digite o valor que deseja buscar: "))

pos_seq, it_seq = busca_seq(vetor, len(vetor), valor)

pos_bin, it_bin = busca_bin(vetor, len(vetor), valor)

print("\n--- Resultados ---")

if pos_seq != -1:
    print(
        f"Busca Sequencial: valor {valor} encontrado na posição {pos_seq} com {it_seq} iteração(ões).")
else:
    print(
        f"Busca Sequencial: valor {valor} não encontrado após {it_seq} iteração(ões).")

if pos_bin != -1:
    print(
        f"Busca Binária:   valor {valor} encontrado na posição {pos_bin} com {it_bin} iteração(ões).")
else:
    print(
        f"Busca Binária:   valor {valor} não encontrado após {it_bin} iteração(ões).")
