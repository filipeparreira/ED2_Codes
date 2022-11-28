def rapid_Ord(vet, inicio, fim):
    if inicio < fim:
        pivo = particiona(vet, inicio, fim)
        rapid_Ord(vet, inicio, pivo - 1)
        rapid_Ord(vet, pivo + 1, fim)

def particiona(vet, inicio, fim):
    esq = inicio
    dir = fim
    pivo = vet[inicio]

    while esq < dir:
        while vet[esq] <= pivo and esq <= fim:
            esq = esq + 1
        while vet[dir] > pivo and dir >= inicio:
            dir = dir - 1
        if esq < dir:
            vet[esq], vet[dir] = vet[dir], vet[esq]
    vet[dir], vet[inicio] = vet[inicio], vet[dir]
    return dir

vet = [-80, 97, -99, -50, 88, -19, 65, -64, -12, -6, 99, -53, 48, 39, 46]
fim = len(vet) - 1

print('Vetor desordenado: ', vet)
rapid_Ord(vet, 0, fim)
print('Vetor ordenado: ', vet)