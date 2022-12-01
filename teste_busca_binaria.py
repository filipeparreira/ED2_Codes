def busca_binaria(arr, valores, key_busca):
    inicio = 0
    fim = len(arr) - 1
    while inicio <= fim:
        meio = int((inicio + fim) / 2)
        num = arr[meio]
        
        if num == key_busca:
            valores.append(num)
            del(arr[meio])
            busca_binaria(arr, valores, key_busca)
            return valores, True
        if num > key_busca:
            fim = meio - 1
        else: 
            inicio = meio + 1 
        
    return 0, False


my_list = [57,68,76,77,82,86,89,89,89,98,100]
valores = list()
print(f'Lista antes da busca binaria: {my_list}')
valor, res = busca_binaria(my_list, valores, 89)
if res == True:
    print(f'O valor buscado foi encontrado!!, o valor é: {valor}')
    print(f'Lista depois da busca binaria: {my_list}')

lista = list()
valor = ('FIlipe', 2)
lista.append(valor)
valor2 = ('Julio', 6)
lista.append(valor2)
print(lista[1][1])