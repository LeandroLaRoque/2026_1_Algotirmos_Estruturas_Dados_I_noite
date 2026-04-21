# 2) Implemente uma função recursiva para contagem regressiva

def contagem_regressiva(n):
    if n < 0:
        return
    print(n)
    contagem_regressiva(n - 1)


valor = int(input("Digite um número para contagem regressiva: "))
contagem_regressiva(valor)
