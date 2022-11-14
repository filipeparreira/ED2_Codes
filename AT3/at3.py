#Bibliotecas 
from sorting_techniques import pysort
from sys import argv

'''
Possiveis erros:
- Arquivo de entrada vazio (resolvido)
- Informações do cabeçalho incorretas 
- Key com mais de 3 dígitos
'''

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
    
    #Transformando os itens da lista em inteiros
    for count in range(0, len(keys)):
        if keys[count] == '\n':
            del(keys[count])
    
    for count in range(0, len(keys)):
        keys[count] = int(keys[count])

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
    
    #Transformando para str
    for count in range(0, len(keys)):
            keys[count] = str(keys[count])

    #Começo do laço que imprime no arquivo de saída
    for count in range(0, len(keys)):
        #Identifica onde a linha da chave buscada começa
        busca = texto.find(keys[count])
        if busca != -1:
            busca_aux = texto.find('|', busca)
            key_aux = texto[busca:busca_aux]
            if key_aux == keys[count]:
                #Identifica o final da linha
                busca_aux = texto.find('\n', busca)
                arquivo.write(f'{texto[busca:busca_aux]}\n')
            elif key_aux != keys[count]:
                busca = texto.find(keys[count], busca_aux)
                busca_aux = texto.find('\n', busca)
                arquivo.write(f'{texto[busca:busca_aux]}\n')
                
    arquivo.close()

#Função que adiciona uma linha na ultima posição do arquivo,
#para que possa auxiliar na função imprime que identifica os
#registros atráves do '\n', sendo que por padrão os arquivos
#não vem com '\n' no final
def adiciona_linha(arquivo_in):
    arquivo = open(arquivo_in, 'a')
    arquivo.write('\n')
    arquivo.close()

#Apaga a ultima linha que contém o \n para que a quantidade
#de '\n's não se acumule com a execução do código
def apaga_linha(arquivo_in):
    arquivo = open(arquivo_in, 'r')
    linhas = arquivo.readlines()
    arquivo.close()
    
    arquivo = open(arquivo_in, 'w')
    for linha in linhas:
        if linha !=  '\n':
            arquivo.write(linha)
        
    arquivo.close()

def verifica_infos(ordem, tipo_ord, arq_out):
    arq = open(arq_out, 'w')
    if ordem != 'D' and ordem != 'C':
        arq.write('Arquivo Inválido!!')
        arq.close()
        exit()
    elif tipo_ord != 'Q' and tipo_ord != 'H' and tipo_ord != 'M' and tipo_ord != 'I':
        arq.write('Arquivo Inválido!!')
        arq.close()
        exit()

#Função que verifica se o arquivo de entrada está vazio 
def verifica_vazio(arquivo_in, arquivo_out):
    arq = open(arquivo_in, 'r')
    linhas = arq.readlines()
    arq.close()
    tam = len(linhas)
    arq = open(arquivo_out, 'w')

    if tam == 0 or tam == 1:
        arq.write('Arquivo Inválido!!')
        arq.close()
        exit()
    elif linhas[0] == '\n' or linhas[1] == '\n':
        arq.write('Arquivo Inválido!!')
        arq.close()
        exit()


#Main 
if __name__ == '__main__':
    #Verificando a quantidade de argumentos
    if len(argv) != 3:
        print('Quantidade de argumentos inválidos!!')
        print('Insira 3 argumentos: [nome do programa] [arquivo de entrada] [arquivo de saida]')
        exit()
    
    #Recebendo o arquivo:
    arquivo_in = argv[1]
    arquivo_saida = argv[2]
    
    #Verificando se o arquivo de entrada está vazio
    verifica_vazio(arquivo_in, arquivo_saida)

    #Chama a função que adiciona '\n' no final do arquivo
    adiciona_linha(arquivo_in)

    #Armazena quantidade, tipo_ord, ordem, keys, e a primeira linha
    quantidade, tipo_ord, ordem, keys, linha1 = armazena(arquivo_in)    

    #Verifica as informações do cabeçalho
    verifica_infos(ordem, tipo_ord, arquivo_saida)

    #Ordena a lista de chaves
    keys = ordena(keys, tipo_ord, ordem)
    
    #Armazena o texto do arquivo de entrada em uma variável
    # e chama a função que imprime no arquivo de saída
    arq = open(arquivo_in, 'r')
    texto = arq.readlines()
    arq.close()
    texto = texto[1:]
    texto = ''.join(texto)

    apaga_linha(arquivo_in)

    imprime(arquivo_saida, texto, keys, linha1)
    
    apaga_linha(arquivo_saida)
    
