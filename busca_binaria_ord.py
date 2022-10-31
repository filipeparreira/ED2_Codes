def busca_binaria(arquivo_ord, key_busca):
    arquivo = open(arquivo_ord, 'r')
    linhas = arquivo.readlines()
    arquivo.close()

    inicio = 0
    fim = len(linhas) - 1

    registros = armazena(arquivo_ord)
    gera_key(registros)

    while inicio <= fim:
        meio = int((inicio + fim) / 2)
        reg = registros[meio]
        
        if reg['key'] == key_busca:
            return True
        if reg['key'] > key_busca:
            fim = meio - 1
        else: 
            inicio = meio + 1 
        
    return False
    

#É uma função que vai receber um arquivo e retornar
#uma lista com todos os registros do arquivo
def armazena(arquivo_in):
    arquivo = open(arquivo_in, 'r')
    linhas = arquivo.readlines()
    arquivo.close()

    heroi = {}
    lista_herois = []

    count = 0
    
    while count < len(linhas):
        conteudo = linhas[count].split('|')
        if len(conteudo) == 7:        
            heroi['nome'] = conteudo[0]
            heroi['sobrenome'] = conteudo[1]
            heroi['nome_heroi'] = conteudo[2]
            heroi['poder'] = conteudo[3]
            heroi['fraqueza'] = conteudo[4]
            heroi['local'] = conteudo[5]
            heroi['profissao'] = conteudo[6]
            
            #Amazena o dicionario 'heroi' em uma lista,
            #gerando assim, uma lista de dicionarios
            lista_herois.append(heroi.copy())
            count += 1
        else:
            count += 1
    
    return lista_herois


def gera_key(lista_herois):
    
    for count in range(0, len(lista_herois)):
        nome = lista_herois[count]['nome']
        sobrenome = lista_herois[count]['sobrenome']
        key = nome + sobrenome
        key = key.replace(' ', '').upper()
        lista_herois[count]['key'] = key

def imprime(lista_herois_ord, arquivo):
    
    arquivo = open(arquivo, 'w')
    
    for count in range(0, len(lista_herois_ord)):
        arquivo.write('{}|'.format(lista_herois_ord[count]['nome']))
        arquivo.write('{}|'.format(lista_herois_ord[count]['sobrenome']))
        arquivo.write('{}|'.format(lista_herois_ord[count]['nome_heroi']))
        arquivo.write('{}|'.format(lista_herois_ord[count]['poder']))
        arquivo.write('{}|'.format(lista_herois_ord[count]['fraqueza']))
        arquivo.write('{}|'.format(lista_herois_ord[count]['local']))
        arquivo.write('{}'.format(lista_herois_ord[count]['profissao']))
    
    arquivo.close()
        
if __name__ == "__main__":
    #Definindo os arquivos
    arq_in = 'heroi.txt'
    arquivo_ord = 'herois_ord.txt'

    #Chamando as funções para armazenar as informações do arquivo de entrada 
    #e a que armazena  na lista a chave canonica de cada item do arquivo de entrada
    lista_herois = armazena(arq_in)
    gera_key(lista_herois)

    #Ordenando a lista de dicionarios em forma decrescente, atraves da chave canonica
    lista_herois_ord = sorted(lista_herois, key=lambda row:row['key'])

    #Imprime a lista ordenada em um outro arquivp
    imprime(lista_herois_ord, arquivo_ord)

    key_busca = str(input('Digite o nome e sobrenome do heroi que deseja buscar: ')).replace(' ', '').upper().strip()
    print(key_busca)
    res = busca_binaria(arquivo_ord, key_busca)

    if res == True:
        print('O heroi buscado foi encontrado!!!')
    else:
        print('O heroi buscado não existe nos registros :(')
        
    