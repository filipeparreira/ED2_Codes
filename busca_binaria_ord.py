def armazena(heroi, lista_herois, tam):
    count = 0
    while count < tam:
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
    #Manipulação do arquivo
    arq_in = open('heroi.txt', 'r')
    linhas = arq_in.readlines()
    arq_in.close()
    
    tam = len(linhas)

    #Declarando o dicionario e uma lista(que vai se tornar uma lista de dicionarios)
    heroi = {}
    lista_herois = []

    #Chamando as funções para armazenar as informações do arquivo de entrada 
    #e a que armazena  na lista a chave canonica de cada item do arquivo de entrada
    armazena(heroi, lista_herois, tam)
    gera_key(lista_herois)

    #Ordenando a lista de dicionarios em forma decrescente, atraves da chave canonica
    lista_herois_ord = sorted(lista_herois, key=lambda row:row['key'])

    #Imprime a lista ordenada em um outro arquivp
    imprime(lista_herois_ord, 'saida_teste_ord1.txt')