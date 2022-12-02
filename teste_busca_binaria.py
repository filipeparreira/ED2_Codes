def binarySearch(array, item_busca, found, valores):
    if sorted(array) != array:
        print("Array is not sorted!")
        return found

    first = 0
    last = len(array)-1

    while first<=last and not found:
        midpoint = (first + last)//2
        if array[midpoint] == item_busca:
            valores.append(array[midpoint])
            del(array[midpoint])
            binarySearch(array, item_busca, found, valores)
            found = True
        else:
            if item_busca < array[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return found, valores

my_list = [57,68,76,77,82,86,89,89,89,98,100]
valores = list()
print(f'Lista antes da busca binaria: {my_list}')
#valor, res = busca_binaria(my_list, valores, 89, encontrado)
found = False
res, valores = binarySearch(my_list, 89, found, valores)
if res == True:
    print('O numero pesquisado foi encontrado')
print(f'Lista depois da busca binaria: {my_list}')
