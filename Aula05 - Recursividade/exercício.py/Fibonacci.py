# Peça ao usuário que informe um valor e então, usando recursividade,
# imprima os termos da sequência Fibonacci que são menores que este valor

def fibonacci(a, b, n):
    if a > n:
        return
    print(a, " - ")
    fibonacci(b, a+b, n)


x = int(input("Digite um valor: "))
fibonacci(0, 1, x)
