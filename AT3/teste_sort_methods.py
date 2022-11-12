from sorting_techniques import pysort

#Criação do objeto que representa o pysort
object_sort = pysort.Sorting()

lista_pessoas = []

pessoas = {'key' : 30, 'nome' : 'Filipe', 'idade' : 21, 'sexo' : 'Masculino'}
lista_pessoas.append(pessoas)
pessoas = {'key' : 20, 'nome' : 'Almeida', 'idade' : 20, 'sexo' : 'Masculino'}
lista_pessoas.append(pessoas)
pessoas = {'key' : 10, 'nome' : 'Bento', 'idade' : 23, 'sexo' : 'Masculino'}
lista_pessoas.append(pessoas)


print(lista_pessoas[0]['nome'])

print(lista_pessoas[0]['nome'])

quick = object_sort.quickSort(arr.copy(), 0, len(arr) - 1)
print(quick)
merge = object_sort.mergeSort(arr.copy())
print(merge)
heap = object_sort.heapSort(arr.copy())
print(heap)
insertion = object_sort.insertionSort(arr.copy())
print(insertion)
