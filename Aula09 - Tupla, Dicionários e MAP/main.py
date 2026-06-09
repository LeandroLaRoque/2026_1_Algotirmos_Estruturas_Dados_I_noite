carro01 = {"modelo": "Doblo", "ano": 2006}
carro02 = {"modelo": "Renegade", "ano": 2021}
carro03 = {"modelo": "Pulse", "ano": 2024}
carro03["placa"] = "JDH-1G98"
# print( carro03 )

frota = carro01, carro02
carro01["modelo"] = "Uno Mille"
print(frota)
# frota[0] = carro03


def calcular(x, y):
    return x + y, x - y, x * y, x / y


result = calcular(5, 2)
print(result)
a, b, c, d = result
print("Soma:", a)
print("Subtração:", b)
print("Multiplicação:", c)
print("Divisão:", d)

print("-----------------------------")


def printarNome(x):
    print("Nome: ", x)


def somarValores(valores):
    total = 0
    for n in valores:
        total += n
    return total


# Executa a função somarValores para cada elemento(1 = Tupla, 2 = array e 3 = array, então executa a função 3 vezes) da tupla numeros.
numeros = ((1, 2), [1, 2, 3], [10, 20, 30, 40])
somas = map(somarValores, numeros)
print(list(somas))
nomes = "João", "Maria", "José"

x = map(printarNome, nomes)
list(x)
