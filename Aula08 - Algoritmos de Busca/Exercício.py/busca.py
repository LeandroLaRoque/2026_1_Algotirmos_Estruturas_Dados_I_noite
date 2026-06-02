def busca_seq(v, n, k):
    iteracoes = 0
    for i in range(n):
        iteracoes += 1
        if v[i] == k:
            return i, iteracoes
    return -1, iteracoes


def busca_bin(v, n, k):
    iteracoes = 0
    inicio = 0
    fim = n - 1
    while inicio <= fim:
        iteracoes += 1
        centro = inicio + (fim - inicio) // 2
        if k == v[centro]:
            return centro, iteracoes
        elif k > v[centro]:
            inicio = centro + 1
        else:
            fim = centro - 1
    return -1, iteracoes
