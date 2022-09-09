def mesclar_Ord(vet, inicio, fim):
    if fim - inicio > 1:
        meio = (inicio + fim) // 2
        mesclar_Ord(vet, inicio, meio)
        mesclar_Ord(vet, meio, fim)
        mesclar(vet, inicio, meio, fim)

def mesclar(vet, inicio, meio, fim):
    vet_esquerda = vet[inicio:meio]
    vet_direita = vet[meio:fim]
    top_e, top_d = 0, 0

    for ind_aux in range(inicio, fim):
        if top_e >= len(vet_esquerda):
            vet[ind_aux] = vet_direita[top_d]
            top_d = top_d + 1

        elif top_d >= len(vet_direita):
            vet[ind_aux]= vet_esquerda[top_e]
            top_e = top_e + 1

        elif vet_esquerda[top_e] < vet_direita[top_d]:
            vet[ind_aux] = vet_esquerda[top_e]
            top_e = top_e + 1

        else:
            vet[ind_aux] = vet_direita[top_d]
            top_d = top_d + 1




vet = [-80, 97, -99, -50, 88, -19, 65, -64, -12, -6, 99, -53, 48, 39, 46]
fim = len(vet) - 1

print('Vetor desordenado: ', vet)
mesclar_Ord(vet, 0, fim)
print('Vetor ordenado: ', vet)