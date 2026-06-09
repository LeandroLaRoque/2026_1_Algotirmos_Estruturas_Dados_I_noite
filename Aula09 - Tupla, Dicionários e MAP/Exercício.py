# Construa um algoritmo que possua uma tupla com os números escritos
# por extenso de “zero” a “nove”. Peça ao usuário para digitar um número
# de 0 a 9 e retorne a ele o número por extenso, sem usar estruturas
# condicionais (if e switch).

extenso = ("zero", "um", "dois", "três", "quatro",
           "cinco", "seis", "sete", "oito", "nove")

numero = int(input("Digite um número de 0 a 9: "))
print("Número por extenso:", extenso[numero])

print("\n" "-----------------------------" "\n")


# Construa um algoritmo que peça ao usuário para informar o nome, a
# nota01 e a nota02 de um aluno. Guarde estas informações em um
# dicionário. Após, calcule a nota final deste aluno [(nota01 + nota02) /2]
# e adicione ao dicionário. Ao final, imprima todos os dados do
# dicionário.

aluno = {}

aluno["nome"] = input("Nome do aluno: ")
aluno["nota01"] = float(input("Nota 1: "))
aluno["nota02"] = float(input("Nota 2: "))

aluno["media"] = (aluno["nota01"] + aluno["nota02"]) / 2

print("\n--- Dados do Dicionário aluno ---")
print("Nome:", aluno["nome"])
print("Nota 1:", aluno["nota01"])
print("Nota 2:", aluno["nota02"])
print("Média:", aluno["media"])
