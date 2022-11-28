def selecao_OrdDec(vetor):
    tam = len(vetor)
    for i in range(0, tam - 1):
        menor = i    
        for x in range(i, tam):
            if vetor[menor] < vetor[x]:
                menor = x
        if menor != i:
            vetor[menor], vetor[i] = vetor[i], vetor[menor]

def selecao_OrdCresc(vetor):
    tam = len(vetor)
    for i in range(0, tam - 1):
        menor = i
        for x in range(i, tam):
            if vetor[menor] > vetor[x]:
                menor = x
        if menor != i:
            vetor[menor], vetor[i] = vetor[i], vetor[menor]
vetor = [-80, 97, -99, -50, 88, -19, 65, -64, -12, -6, 99, -53, 48, 39, 46]


print('Vetor desordenado: ',vetor)
print('Digite a opção de ordenação do vetor.')
opcao = int(input('1. Crescente.\n2. Decrescente\n'))
if opcao == 1:
    selecao_OrdCresc(vetor)
    print('Vetor ordenado: ',vetor)
elif opcao == 2:
    selecao_OrdDec(vetor)
    print('Vetor ordenado: ',vetor)
else:
    print('Opção não existente.')

            