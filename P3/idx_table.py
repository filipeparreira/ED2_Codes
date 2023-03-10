def armazena(item, lista, arquivo):
    arquivo = open(arquivo, 'r')
    linhas = arquivo.readlines()

    for rrn,linha in enumerate(linhas):
        itens = linha.split('|')
        item['ID'] = itens[0]
        item['Nome'] = itens[1]
        item['Curso'] = itens[2]
        item['Cidade'] = itens[3].replace('\n', '')
        item['RRN'] = rrn
        if item['ID'] != '00745':
            lista.append(item.copy())

def gera_idx(lista, x, y):
    idx = list()
    for item in lista:
        sub1 = item[x]
        sub2 = item[y]
        elemento = (sub1, sub2)
        idx.append(elemento)
    return idx

def gera_keys(lista):
    for item in lista:
        ident = item['ID']
        nome = item['Nome']
        item['CC'] = ident + nome.upper()


if __name__ == '__main__':
    item = dict()
    lista = list()
    arquivo = 'entrada.txt'

    armazena(item, lista, arquivo)
    gera_keys(lista)
    idx = gera_idx(lista, 'CC', 'RRN')
    print('Depois:')
    idx.sort(key = lambda tup: tup[0]) 
    for item in idx:
        print(item)

    