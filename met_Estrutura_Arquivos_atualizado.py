#Estrutura do jogo:
    #Titulo: 50 caracteres 
    #Gênero: 25 caracteres 
    #Plataforma: 15 caracteres 
    #Ano: 4 caracteres
    #Classificação: 12 caracteres 
    #Preço: 7 caracteres 
    #Mídia: 8 caracteres
    #Tamanho: 7 caracteres
    #Produtora: 40 caracteres 

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

def grep(nome_arq, palavra_busca):

    arq_out = open(nome_arq, 'r')
    jogos = arq_out.readlines()
    print(jogos)
    #Palavra a ser buscada
    palavra_busca = str(palavra_busca).strip().upper() 

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
    arq_out.close()
    return (aux_indice)


arq_in = open('games2.txt', 'r')

jogos = arq_in.readlines()
tam = len(jogos)



arq_in.close()

arq_out = open('saida_Teste_Games.txt', 'w+')


for cont_Aux in range(0, tam):
    itens = jogos[cont_Aux].split('|')
    Lista_Jogo = Jogo(itens[0], itens[1], itens[2], itens[3], itens[4], itens[5], itens[6], itens[7], itens[8])
    arq_out.write('{:50}|'.format(Lista_Jogo.titulo))
    arq_out.write('{:40}|'.format(Lista_Jogo.prod))
    arq_out.write('{:25}|'.format(Lista_Jogo.genero))
    arq_out.write('{:15}|'.format(Lista_Jogo.plataforma))
    arq_out.write('{:4}|'.format(Lista_Jogo.ano))
    arq_out.write('{:12}|'.format(Lista_Jogo.classificacao))
    arq_out.write('{:7}|'.format(Lista_Jogo.preco))
    arq_out.write('{:8}|'.format(Lista_Jogo.midia))
    arq_out.write('{}'.format(Lista_Jogo.tam))

palavra_busca = str(input('Digite a palavra a ser buscada no arquivo: '))

nome_arq = 'games2.txt'

indices = grep(nome_arq, palavra_busca)

print(indices)

arq_out.close()



        