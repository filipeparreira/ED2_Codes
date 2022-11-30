'''
    ** Itens que vão conter em cada registro:
        - Ano: o ano que a música foi lançada [5]
        - Duração: a duração em minutos e segundos [6] 
        - Título: o título da música [31]
        - Artista: o artista que gravou a música [21]
        - Gênero: o gênero da música [12]
        - Idioma: o idioma da canção [12]
    
    **Exigências do programa:
        - O programa vai receber três arquivos como parâmetro, um arquivo contendo as músicas,
        um arquivo de consultas e um arquivo de saída.
        - Será necessario implementar um índice primário, para que o secundário funcione
        - As funções que vão ser necessárias são: 
            - Criar, carregar e pesquisar (Tanto no indice primario quanto no indice secundario)
            - E funções auxiliares (Ler_registro_com_RRN, ordenarIndx, criar_RRN)
'''
# Bibliotecas 
from sys import argv

# Para o funcionamento do indice primario
    # Ler um registro com base no RRN
    # Ordenar o arquivo de indices 
    # Gerar chave canonica
    # Criar tabela de indices, onde cada indice é uma tupla (RRN, cc)
    # Carregar as informações dos registros para a tabela de indices 
    # Pesquisar baseado na chave canonica


#------------------------------------ Manipulando os dados do arquivo ----------------------------------                                                                                                        

# Abro o arquivo de entrada, leio e armazeno as informações contidas nele
def armazena(arquivo, dicionario, lista):
    arquivo = open(arquivo, 'r')
    linhas = arquivo.readlines()
    arquivo.close()

    # Guardadando a quantidade de registros no arquivo
    cabecalho = linhas[0].split('QTDE=')
    cabecalho_aux = cabecalho[1].split(' ')
    quantidade = int(cabecalho_aux[0])
    
    for count in range(1, len(linhas)):
        itens = linhas[count].split('|')
        if len(itens) == 6:
            dicionario['ano'] = itens[0]
            dicionario['duracao'] = itens[1]
            dicionario['titulo'] = itens[2]
            dicionario['artista'] = itens[3]
            dicionario['genero'] = itens[4]
            dicionario['idioma'] = itens[5]

            lista.append(dicionario.copy())

    # Defino o tamanho dos itens do arquivo
    for registro in lista:
        if len(registro['ano']) > 4:
            registro['ano'] = registro['ano'][:4]
        if len(registro['duracao']) > 5:
            registro['duracao'] = registro['duração'][:5]
        if len(registro['titulo']) > 31:
            registro['titulo'] = registro['titulo'][:31]
        if len(registro['artista']) > 21:
            registro['artista'] = registro['artista'][:21]
        if len(registro['genero']) > 12:
            registro['genero'] = registro['genero'][:12]
        if len(registro['idioma']) > 12:
            registro['idioma'] = registro['idioma'][:12]

    return quantidade, lista


#------------------------------------ Fim manipulação do arquivo ------------------------------------

#------------------------------------ Funções auxiliares ------------------------------------

# Função que gera chave canonica, retornando uma lista contendo as chaves canonicas do registros
# a chave canonica é definida pelo TITULO + ARTISTA 
def gera_cc(registros):
    chaves = list()

    for registro in registros:
        titulo = registro['titulo'].replace(' ', '').upper()
        artista = registro['artista'].replace(' ', '').upper()
        chave_cc = titulo + artista
        chaves.append(chave_cc)
    
    return chaves

#------------------------------------ Fim das funções auxiliares ------------------------------------

# Main
if __name__ == '__main__':
    # Definindo os arquivos 
    arquivo_in = argv[1]
    arquivo_busca = 'entrada1.txt'
    arquivo_out = 'saida1.txt'

    # Criando a lista e os dicionarios
    registros = list()
    registro = dict()

    # Funções
    quantidade, registros = armazena(arquivo_in, registro, registros)
    chaves_cc = gera_cc(registros)
    
    
    

