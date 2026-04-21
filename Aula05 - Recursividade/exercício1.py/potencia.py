# 1) Implemente uma função recursiva para cálculo de potência

def potencia(a, b, resultado):
    if b == 0:
        print(resultado)
        return
    potencia(a, b - 1, resultado * a)


base = int(input("Base: "))
expoente = int(input("Expoente: "))
potencia(base, expoente, 1)
