#Função que recebe o arquivo em que a palavra vai ser buscada
#e retorna uma lista com as linhas em que essa palavra foi encontrada 
#e um contador, que representa quantas vezes a palavra buscada foi encontrada
def grep(arquivo, palavra_busca):
    arquivo = open(arquivo, 'r')
    jogos = arquivo.readlines()
    tam = len(jogos)
    #Inicializando, tanto a lista contendo as linhas (grep_list), quanto o contador
    grep_list = []
    contador = 0

    for count in range(0, tam):
        #Quando find é diferente de -1 significa que a palavra foi encontrada na lista
        if jogos[count].upper().find(palavra_busca) != -1:
            grep_list.append(jogos[count])
            contador += 1
    
    arquivo.close()
    return grep_list, contador

if __name__ == "__main__":
    
    #Pré definindo o nome do arquivo de entrada para a função grep
    #e adotando a palavra de busca como sendo a palavra 'rpg'
    arquivo_in = 'lista_jogos_questao2.txt'
    palavra_busca = 'rpg'

    #Chamando a função, e guardando o retorno da lista de linhas e do contador
    #em ocorrencias e contador, respectivamente
    ocorrencias, contador = grep(arquivo_in, palavra_busca.upper())

    #Imprimindo na saída do console o valor do contador, e as linhas em que a palavra foi encontrada
    print('\nQuantidade de ocorrencias dentro do arquivo de entrada: ', contador)
    print('\nTodas as linhas em que a palavra foi encontrada: ')
    for count in range(0, len(ocorrencias)):
        print(ocorrencias[count])



