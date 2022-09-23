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

arq = open('games.txt', 'a')

jogos = arq.readlines()

itens = jogos[0].split('|')
Lista_Jogo = Jogo(itens[0], itens[1], itens[2], itens[3], itens[4], itens[5], itens[6], itens[7], itens[8])
arq.writelines()
print(Lista_Jogo.titulo)
print(Lista_Jogo.genero)
print(Lista_Jogo.plataforma)
print(Lista_Jogo.ano)
print(Lista_Jogo.classificacao)
print(Lista_Jogo.preco)
print(Lista_Jogo.midia)
print(Lista_Jogo.tam)
print(Lista_Jogo.prod)

arq.close()



        