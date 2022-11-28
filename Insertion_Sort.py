def insercao_OrdCres(vet, tam):
    for i in range(1, tam):
        aux_Position = vet[i]
        j = i - 1
        while (j >= 0) and (aux_Position < vet[j]):
            vet[j + 1] = vet[j]
            j = j - 1
        vet[j + 1] = aux_Position

def insercao_OrdDec(vet, tam):
    for i in range(1, tam):
        aux_Position = vet[i]
        j = i - 1
        while (j >= 0) and (aux_Position > vet[j]):
            vet[j + 1] = vet[j]
            j = j - 1
        vet[j + 1] = aux_Position


vet = [-80, 97, -99, -50, 88, -19, 65, -64, -12, -6, 99, -53, 48, 39, 46]

print('Vetor Desordenardo: ', vet)

escolha = int(input('Digite a opção de ordenação.\n1. Ordenação Crescente.\n2. Ordenação Decrescente.\n'))

if escolha >= 1 and escolha <= 2:
    if escolha == 1:
        insercao_OrdCres(vet, len(vet))
    else: 
        insercao_OrdDec(vet, len(vet))
else:
    print('Opção Inválida!!')

print('Vetor Ordenardo: ', vet)
