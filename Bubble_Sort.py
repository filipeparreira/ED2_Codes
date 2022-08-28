def bolha_Curta(vet):
    trocou = True 
    while trocou == True:
        trocou = False
        for i in range(0, len(vet) + 1):
            if vet[i] > vet[i + 1]:
                vet[i], vet[i + 1] = vet[i +1], vet[i]
                trocou = True 

vet = [-80, 97, -99, -50, 88, -19, 65, -64, -12, -6, 99, -53, 48, 39, 46]

bolha_Curta(vet)

print('O vetor ordenado: ', vet)