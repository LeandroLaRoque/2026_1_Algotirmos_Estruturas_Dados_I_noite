def somarAte(n=0):
    if n == 0:
        return 0
    else:
        return n + somarAte(n - 1)


def fatorial(n=0):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)


print("Soma de 1 até 5: ", somarAte(5))
print("Fatorial de 5 é: ", fatorial(5))

#Exercícios:
#1) Implemente uma função recursiva para cálculo de potência
#2) Implemente uma função recursiva para contagem regressiva
#3) Implemente uma função recursiva para inverter uma string
