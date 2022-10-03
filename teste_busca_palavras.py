from cgi import print_environ


class Jogo:
    jogo = 'Jogo'

    def __init__(self, titulo=None, prod=None, genero=None, plataforma=None, ano=None, classificacao=None,
     preco=None, midia=None, tam=None):

        self.titulo = titulo
        self.prod = prod
        self.genero = genero
        self.plataforma = plataforma
        self.ano = ano
        self.classificacao = classificacao
        self.preco = preco
        self.midia = midia
        self.tam = tam


arq_out = open('saida_Teste_Games.txt', 'r')

jogos = arq_out.readlines()

#Palavra a ser buscada
palavra_busca = 'RPG'

#Auxiliar de busca, onde ele armazena o indice em que a palavra esta, o ideal é retornar o indice da linha onde a palavra está 
aux_indice = []

#Encontrar o \n e pular para linha de baixo retornar o indice da linha
aux_count = 0
while aux_count < len(jogos):
    itens = jogos[aux_count].split('|')
    for aux_count1 in range(0, len(itens)):
        item = itens[aux_count1].upper().strip()
        if palavra_busca == item:
            aux_indice.append(aux_count)
    aux_count += 1

print(aux_indice)
         


'''
#Palavra a ser buscada
palavra_busca = 'THE WITCHER 3 - WILD HUNT'

#Auxiliar de busca, onde ele armazena o indice em que a palavra esta, o ideal é retornar o indice da linha onde a palavra está 
aux_indice = []

itens = jogos[0].split('|')

#Buscou e encontrou a palavra em um vetor de string e retornou o indice em que o vetor esta
for aux_count in range(0, len(itens)):
    item = itens[aux_count].upper().strip()
    print(item)
    if item == palavra_busca:
        aux_indice.append(aux_count)

print('A palavra buscada esta na posição [{}] do vetor'.format(aux_indice[0] + 1))
'''




arq_out.close()
