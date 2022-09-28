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

arq = open('games.txt', 'r')

jogos = arq.readlines()
tam = jogos

arq.close()

arq = open('saida_Teste.txt', 'a')

for cont_Aux in range(0, tam):
    itens = jogos[cont_Aux].split('|')
    Lista_Jogo = Jogo(itens[0], itens[1], itens[2], itens[3], itens[4], itens[5], itens[6], itens[7], itens[8])
    arq.write('{:50}|'.format(Lista_Jogo.titulo))
    arq.write('{:25}|'.format(Lista_Jogo.genero))
    arq.write('{:15}|'.format(Lista_Jogo.plataforma))
    arq.write('{:4}|'.format(Lista_Jogo.ano))
    arq.write('{:12}|'.format(Lista_Jogo.classificacao))
    arq.write(Lista_Jogo.preco)
    arq.write(Lista_Jogo.midia)
    arq.write(Lista_Jogo.tam)
    arq.write(Lista_Jogo.prod)

arq.close()



        