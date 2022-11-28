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

from asyncore import write


class Jogo:
    jogo = 'Jogo'

    def __init__(self, titulo=None, genero=None, plataforma=None, ano=None, classificacao=None,
     preco=None, midia=None, tam=None, prod=None):

        self.titulo = titulo
        self.genero = genero
        self.plataforma = plataforma
        self.ano = ano
        self.classificacao = classificacao
        self.preco = preco
        self.midia = midia
        self.tam = tam
        self.prod = prod

#Leitura do arquivo 
arq_Jogos = open('games.txt', 'r+')

jogos = arq_Jogos.readlines()

arq_Jogos.close()

arq_Jogos = open('saida.txt', 'a')

tam = len(jogos)

for cont_Aux in range(0, tam):    
    itens = jogos[cont_Aux].split('|')
    Lista_Jogo = Jogo(itens[0], itens[1], itens[2], itens[3], itens[4], itens[5], itens[6], itens[7], itens[8])
    arq_Jogos.write(Lista_Jogo.titulo)
    arq_Jogos.write(Lista_Jogo.genero)
    arq_Jogos.write(Lista_Jogo.plataforma)
    arq_Jogos.write(Lista_Jogo.ano)
    arq_Jogos.write(Lista_Jogo.classificacao)
    arq_Jogos.write(Lista_Jogo.preco)
    arq_Jogos.write(Lista_Jogo.midia)
    arq_Jogos.write(Lista_Jogo.tam)
    arq_Jogos.write(Lista_Jogo.prod)



arq_Jogos.close()



        