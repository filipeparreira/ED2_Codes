from random import randrange


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

def imprime(lista_herois, lista_herois_ord, arquivo):
    
    arquivo = open(arquivo, 'w')
    arquivo.write('Lista Herois desordenada:\n\n')
    for count in range(0, len(lista_herois)):
        arquivo.write('{}|'.format(lista_herois[count]['nome']))
        arquivo.write('{}|'.format(lista_herois[count]['sobrenome']))
        arquivo.write('{}|'.format(lista_herois[count]['nome_heroi']))
        arquivo.write('{}|'.format(lista_herois[count]['poder']))
        arquivo.write('{}|'.format(lista_herois[count]['fraqueza']))
        arquivo.write('{}|'.format(lista_herois[count]['local']))
        arquivo.write('{}|'.format(lista_herois[count]['profissao']))

    arquivo.write('Lista Herois ordenada:\n\n')
    for count in range(0, len(lista_herois_ord)):
        arquivo.write('{}|'.format(lista_herois_ord[count]['nome']))
        arquivo.write('{}|'.format(lista_herois_ord[count]['sobrenome']))
        arquivo.write('{}|'.format(lista_herois_ord[count]['nome_heroi']))
        arquivo.write('{}|'.format(lista_herois_ord[count]['poder']))
        arquivo.write('{}|'.format(lista_herois_ord[count]['fraqueza']))
        arquivo.write('{}|'.format(lista_herois_ord[count]['local']))
        arquivo.write('{}|'.format(lista_herois_ord[count]['profissao']))
    
    arquivo.close()
        


arq_in = open('heroi.txt', 'r')
linhas = arq_in.readlines()
arq_in.close()
tam = len(linhas)

heroi = {}
lista_herois = []

armazena(heroi, lista_herois, tam)
gera_key(lista_herois)

lista_herois_ord = sorted(lista_herois, key=lambda row:row['key'])

print(lista_herois_ord[0]['nome'])

imprime(lista_herois, lista_herois_ord, 'saida.txt')
