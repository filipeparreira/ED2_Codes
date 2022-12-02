'''def filter_set(aquarium_creatures, search_string):
	def iterator_func(x):
		for v in x.values():
			if search_string in v:
				return True
		return False
	return filter(iterator_func, aquarium_creatures)
'''
def names_vowels(x):
  return x[1].upper() in 'POP'

aquarium_creatures = [('SECRETARIAAMADOBATISTA', 'BREGA'), ('ABOYNAMEDSUEJOHNNYCASH', 'COUNTRY'), ('CLOSEEYESCHAOS', 'DANCE'), ('FADEALANWALKER', 'ELETRÔNICA'), ('THEMOTTOTIESTO', 'ELETRÔNICA'), ('WAKEMEUPAVICII', 'ELETRÔNICA'), ('THENIGHTSAVICII', 'ELETRÔNICA'), ('PROMISEEBEN', 'ELETRÔNICA'), ('ASTRANGER`SDEADCADMIUN&PAULFLINT', 'ELETRÔNICA'), ('ANGETENARROMPASSO', 'ELETRÔNICA'), ('BAILEDASERRABRAÃO', 'FUNK'), ('INKGAMESHPMUSIC', 'HIP-HOP'), ('ODIUMLXSTCXNTURY', 'HIP-HOP'), ('BABYSHARKPINKFONG', 'INFANTIL'), ('HOYMUEROFELIZFRANCISCO,ELHOMBRE', 'LATINA'), ('NOTHINGELSEMATTERSMETALLICA', 'METAL'), ('GAROTADEIPANEMATOMJOBIM', 'MPB'), ('IWANTITTHATWAYBACKSTREETBOYS', 'POP'), ('THRILLERMICHAELJACKSON', 'POP'), ('THUNDERIMAGINEDRAGONS', 'POP'), ('MADNE-YO', 'POP'), ('BONESIMAGINEDRAGONS', 'POP'), ('OSOLVITORKLEY', 'POP'), ('UMMINUTOPARAOFIMDOMUNDOCPM22', 'POP'), ('HEATWAVESGLASSANIMALS', 'POP'), ('HAYYAHAYYATRINIDADCARDONA', 'POP'), ('ONEWORLDREDONE', 'POP'), ('WEAREONEPITBULL', 'POP'), ('TATUBOMDEBOLAARLINDOCRUZ', 'POP'), ('WAKAWAKASHAKIRA', 'POP'), ('THETIMEOFOURLIVESIIDIVO', 'POP'), ('BOOMANASTACIA', 'POP'), ('LACOPADELAVIDARICKMARTIN', 'POP'), ('ACORDA,PEDRINHOJOVEMDIONÍSIO', 'POP ROCK'), ('LONELYAKON', 'R&B'), ('DIÁRIODEUMDETENTORACIONAISMC’S', 'RAP'), ('QUERVOARMATUÊ', 'RAP'), ('ACARADOCRIMEMCPOZEDORODO', 'RAP'), ('INDACLUB50CENT', 'RAP'), ('LOSEYOURSELFEMINEM', 'RAP'), ("HELLAIN'TABADPLACETOBEACDC", 'ROCK'), ('NUMBLINKINPARK', 'ROCK'), ('ENEMYIMAGINEDRAGONS', 'ROCK'), ('HOWYOUREMINDMENICKELBACK', 'ROCK'), ('BOULEVARDOFBROKENDREAMSGREENDAY', 'ROCK'), ('PRIMEIROSERROSCAPITALINICIAL', 'ROCK')]

filtered_names = filter(names_vowels, aquarium_creatures)

print(len(list(filtered_names)))
'''print(len(list(filter(lambda x: x[1] in 'POP', aquarium_creatures))))'''

'''lista_filtrada = list(filtered_records)

print(lista_filtrada)'''









'''def binarySearch(array, item_busca, found, valores):
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
print(f'Lista depois da busca binaria: {my_list}')'''
