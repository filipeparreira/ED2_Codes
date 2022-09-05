def mesclar_Ord(vet, inicio, fim):
    if inicio < fim:
        meio = (inicio + fim) / 2
        mesclar_Ord(vet, inicio, meio)
        mesclar_Ord(vet, meio + 1, fim)
        mesclar(vet, inicio, meio, fim)

def mesclar(vet, inicio, meio, fim):
    vet_aux = []
    posicao_01 = inicio 
    posicao_02 = meio + 1
    
    while posicao_01 <= meio and posicao_02 <= fim:
        if vet[posicao_01] > vet[posicao_02]:
            vet_aux.append(vet[posicao_02])
        
        else:
            vet_aux.append(vet[posicao_01])
        
        if posicao_01 == meio:
            vet_aux.append(vet[posicao_02:])
        else:
            vet_aux.append(vet[:posicao_01])

        vet = vet_aux

vet = [-80, 97, -99, -50, 88, -19, 65, -64, -12, -6, 99, -53, 48, 39, 46]
inicio = 0
fim = len(vet) - 1

print('Vetor desordenardo: ', vet)
mesclar_Ord(vet, inicio, fim)
print('Vetor ordenardo: ', vet)
