#Erros 
    #Pokemon Emerald com erro na saída    
    #Caracteres Especiais oculpando mais de um espaço

#Definição do classe jogo
class Jogo:
    jogo = 'Jogo'

    def __init__(self, titulo=None, prod=None, genero=None, plataforma=None, 
    ano=None, classificacao=None, preco = None, midia=None, tam=None):

        self.titulo = titulo[0:50]
        self.prod = prod[0:40] 
        self.genero = genero[0:25]
        self.plataforma = plataforma[0:15]
        self.ano = ano[0:4]
        self.classificacao = classificacao[0:12]
        self.preco = preco[0:7]
        self.midia = midia[0:8]
        self.tam = tam[0:7]

#Função que imprime e gera a chave de cada jogo ao mesmo tempo
#Caso algum jogo não esteja preenchido com todas as informações, ele pula a linha do jogo
def imprimir_gen_key(nome_arq, tam):
    arq_jogos = open(nome_arq, 'w')
    key_list =[]
    count_aux = 0
    while count_aux < tam:    
        pipecount = 0
        pipecount = jogos[count_aux].count('|')
        while pipecount != 8:
            count_aux += 1
            pipecount = jogos[count_aux].count('|')
        itens = jogos[count_aux].split('|')
        Lista_Jogo = Jogo(itens[0], itens[1], itens[2], itens[3], itens[4], itens[5], itens[6], itens[7], itens[8])
        arq_jogos.write('{:50}|'.format(str(Lista_Jogo.titulo)).strip())
        arq_jogos.write('{:40}|'.format(str(Lista_Jogo.prod)))
        arq_jogos.write('{:25}|'.format(str(Lista_Jogo.genero)))
        arq_jogos.write('{:15}|'.format(str(Lista_Jogo.plataforma)))
        arq_jogos.write('{:4}|'.format(str(Lista_Jogo.ano)))
        arq_jogos.write('{:12}|'.format(str(Lista_Jogo.classificacao)))
        arq_jogos.write('{:7}|'.format(str(Lista_Jogo.preco)))
        arq_jogos.write('{:8}|'.format(str(Lista_Jogo.midia)))
        arq_jogos.write('{}'.format(str(Lista_Jogo.tam)))
        nome = str(Lista_Jogo.titulo).upper().replace(' ', '')
        ano = str(Lista_Jogo.ano).replace(' ', '')
        key_list.append(nome + ano)
        count_aux += 1
    arq_jogos.close()
    return key_list

#Função GREP versão 1, ele busca uma palavra digitada e retorna um vetor com o indice das linhas
#em que a palavra foi encontrada
def grep_v1(arq_saida, palavra_busca):
    arquivo = open(arq_saida, 'r')
    jogos = arquivo.readlines()
    tam = len(jogos)
    grep_list = []

    for count in range(0, tam):
        if jogos[count].upper().find(palavra_busca) != -1:
            grep_list.append(count + 1)
    
    arquivo.close()
    return grep_list

#Função GREP versão 2, ele busca uma palavra digitada e escreve em um segundo arquivo os registros
#onde essa palavra foi encontrada
def grep_v2(arq_saida, palavra_busca):
    arquivo = open(arq_saida, 'r')
    arquivo_2 = open('saida_teste_grep.txt', 'w')
    jogos = arquivo.readlines()
    tam = len(jogos)
    arquivo_2.write('Os registros onde a palavra/numero {} foi encontrada são:\n\n'.format(palavra_busca))
    for count in range(0, tam):
        if jogos[count].upper().find(palavra_busca) != -1:
            arquivo_2.write((jogos[count]))

    arquivo.close()



arq_Jogos = open('gamesv2.txt', 'r')
jogos = arq_Jogos.readlines()
arq_Jogos.close()

tam = len(jogos)
arquivo_saida = str(input('Digite o nome do arquivo de saída: ')).strip()
arquivo_saida = arquivo_saida + '.txt'

key_list = imprimir_gen_key(arquivo_saida, tam)

palavra_busca  = str(input('Digite uma palavra para ser buscada no arquivo: ')).strip().upper()
grep_list = grep_v1(arquivo_saida, palavra_busca)
print('As linhas em que a palavra/numero {} se encontra são: {}'.format(palavra_busca ,grep_list))

grep_v2(arquivo_saida, palavra_busca)







