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
    # Ler um registro com base no RRN (pesquisar)
    # Ordenar o arquivo de indices - Feito 
    # Gerar chave canonica - Feito
    # Criar tabela de indices, onde cada indice é uma tupla (RRN, cc) - Feito
    # Carregar as informações dos registros para a tabela de indices - Feito
    # Pesquisar baseado na chave canonica


#******************************** Manipulando os dados do arquivo ********************************

# Abro o arquivo de entrada, leio e armazeno as informações contidas nele
def armazena(arquivo, dicionario, lista):
    arquivo = open(arquivo, 'r')
    linhas = arquivo.readlines()
    arquivo.close()

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

    return lista

# Escreve no arquivo de saido os registros resultantes da busca
def imprime_resultado(arquivo_out, resultado_busca, regs):
    arquivo = open(arquivo_out, 'w')
    for rrn in resultado_busca:
        registro = regs[rrn]['ano'] + '|' + regs[rrn]['duracao'] + '|' + regs[rrn]['titulo'] + '|' + regs[rrn]['artista'] + '|' + regs[rrn]['genero'] + '|' + regs[rrn]['idioma']
        arquivo.write(registro)  
    arquivo.close()  

# Lê o arquivo auxiliar, e retorna o as informações contidas nele
def info_busca(arquivo_in):
    arquivo = open(arquivo_in, 'r')
    linhas = arquivo.readlines()
    arquivo.close()
    campo = linhas[0]
    item_pesquisa = linhas[1].strip().upper()
    return campo, item_pesquisa


#******************************** Fim manipulação do arquivo ********************************

#******************************** Funções auxiliares ********************************

# Função que gera chave canonica, retornando uma lista contendo as chaves canonicas do registros a chave canonica é TITULO + ARTISTA 
def gera_cc(registro):
    titulo = registro['titulo'].replace(' ', '').upper()
    artista = registro['artista'].replace(' ', '').upper()
    chave_cc = titulo + artista
    return chave_cc

#******************************** Fim das funções auxiliares ********************************

#******************************** Indice Primario ********************************
# A tabela de indices primarios é composto de uma lista de tuplas onde cada tupla é composta por (RRN, cc)
# Criar uma tabela de indices primarios e ordenar eles, e retornar a tabela de indices primarios
def tabela_idx_primario(registros):
    # Cria a tabela de indices primarios 
    idx_primario = list()
    for count, registro in enumerate(registros):
        key = gera_cc(registro)        
        tupla = (count, key)
        idx_primario.append(tupla)
    
    # Ordenar a tabela de indices primarios e retorna-la
    idx_primario.sort(key = lambda tup: tup[1])    
    return idx_primario

# Criando a tabela de indices secundarios formada pelo par ordenado: (RRN, campo)
def tabela_idx_secundario(registros, campo):
    # Lista que representa a tabela de indices primarios
    idx_secundarios = list()
    for count, registro in enumerate(registros):
        key = registro[campo]
        tupla = (count, key)
        idx_secundarios.append(tupla)
    # Ordenar e restornar a tabela de indices secundarios
    idx_primarios.sort(key = lambda tup: tup[1])
    return idx_secundarios
    
# Função que realiza a busca atraves do rrn na tabela de indices e caso exista retorna  o registro inteiro
#def pesquisarRegistro(chave): # [retornar 1 registro ou nada]
        # 1. Pesquisa/busca binária na Tabela de indices
        # na coluna Chave Canonica
        # 2a. Falhou -> return None
        # 2b. Encontrei: (Caralho! É isso)
        #   - acessar o RRN (tupla)
        #   - fazer a leitura do registro no arquivo de dados (via RRN)
        #   - retornar (registro)

#******************************** Fim Indice Primario ********************************

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
    campo, item_pesquisa = info_busca(arquivo_busca)
    registros = armazena(arquivo_in, registro, registros)
    idx_primarios = tabela_idx_primario(registros)
    idx_secundarios =     

    #teste = [0, 14, 33, 5, 30]
    #imprime_resultado(arquivo_out, teste, registros)

    
    

