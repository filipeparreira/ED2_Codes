from sorting_techniques import pysort

#Função que lê as informações do arquivo de entrada,
#armazena as necessaria em variaveis e as  retorna
def armazena(arquivo_in):
    arquivo = open(arquivo_in, 'r')
    linhas = arquivo.readlines()
    linha1 = linhas[0]
    
    #Armazenando as informações do cabeçalho
    cabecalho = linhas[0].split('=')
    
    #Quantidade
    cabecalho_aux = cabecalho[3].split(' ')
    qntd = int(cabecalho_aux[0])

    #Tipo de ordenação
    cabecalho_aux = cabecalho[4].split(' ')
    tipo_ord = cabecalho_aux[0].upper().strip()

    #Ordem da ordenação
    cabecalho_aux = cabecalho[5].split(' ')
    ordem = cabecalho_aux[0].strip().upper()

    #Armazendando as keys
    count = 1
    keys = []
    
    while count < len(linhas):
        conteudo = linhas[count].split('|')
        keys.append(conteudo[0])
        count += 1

    arquivo.close()

    return qntd, tipo_ord, ordem, keys, linha1

#Função que identifica que tipo de ordenação é para ser feita
#e retorna o vetor de chaves já ordenado
def ordena(keys, tipo_ord, ordem):
    ordena = pysort.Sorting()

    if tipo_ord == 'Q':
        keys = ordena.quickSort(keys, 0, len(keys) - 1)
        if ordem == 'D':
            keys = list(reversed(keys))            
        return keys
    
    elif tipo_ord == 'H':
        keys = ordena.heapSort(keys)
        if ordem == 'D':
            keys = list(reversed(keys))            
        return keys
    
    elif tipo_ord == 'M':
        keys = ordena.mergeSort(keys)
        if ordem == 'D':
            keys = list(reversed(keys))            
        return keys
    
    elif tipo_ord == 'I':
        keys = ordena.insertionSort(keys)
        if ordem == 'D':
            keys = list(reversed(keys))            
        return keys

#Vai receber o arquivo de saida, o texto do arquivo de entrada
#e a lista de chaves já ordenadas, e vai imprimir os registros, 
#já ordenados, no arquivo de saída
def imprime(arquivo_saida, texto, keys, linha1):
    arquivo = open(arquivo_saida, 'w')
    arquivo.write(linha1)
    for count in range(0, len(keys)):
        busca = texto.find(keys[count])
        if busca != -1:
            busca_aux = texto.find('\n', busca)
            arquivo.write(f'{texto[busca:busca_aux]}\n')
        
    arquivo.close()


if __name__ == '__main__':
    #Recebendo o arquivo:
    arquivo_in = 'input1.txt'
    arquivo_saida = 'saida_teste1.txt'
    
    

    #Armazena quantidade, tipo_ord, ordem, keys, e a primeira linha
    quantidade, tipo_ord, ordem, keys, linha1 = armazena(arquivo_in)
    
    #Ordena a lista de chaves
    keys = ordena(keys, tipo_ord, ordem)
    
    #Armazena o texto do arquivo de entrada em uma variável
    # e chama a função que imprime no arquivo de saída
    arquivo = open(arquivo_in, 'r')
    texto = arquivo.read()
    arquivo.close()
    print(keys)
    imprime(arquivo_saida, texto, keys, linha1)
    
