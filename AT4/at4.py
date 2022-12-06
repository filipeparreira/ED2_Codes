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

#******************************** Bibliotecas ********************************
from sys import argv
#******************************** Fim - Bibliotecas ********************************



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

    # Retorno a lista de dicionarios contendo os itens já em tamanhos definidos 
    return lista


# Escreve no arquivo de saida os registros resultantes da busca atraves do RRN
def imprime_resultado(arquivo_out, resultado_busca, regs):
    arquivo = open(arquivo_out, 'w')

    # Verifica se o resultado da busca é uma lista vazia
    if len(resultado_busca) == 0:
        arquivo.write('Nenhum registro foi encontrado!')
    else:
        for rrn in resultado_busca:
            registro = regs[rrn]['ano'] + '|' + regs[rrn]['duracao'] + '|' + regs[rrn]['titulo'] + '|' + regs[rrn]['artista'] + '|' + regs[rrn]['genero'] + '|' + regs[rrn]['idioma']
            arquivo.write(registro)  

    arquivo.close()  


# Lê o arquivo auxiliar, e retorna o as informações contidas nele
def info_busca(arquivo_in):
    arquivo = open(arquivo_in, 'r')
    linhas = arquivo.readlines()
    arquivo.close()

    campo = linhas[0].replace('\n', '').lower()
    item_pesquisa = linhas[1].strip().replace('\n', '')

    return campo, item_pesquisa
#******************************** Fim manipulação do arquivo ********************************



#******************************** Funções auxiliares ********************************
# Função que gera chave canonica, retornando uma lista contendo as chaves canonicas dos registros. A chave canonica é TITULO + ARTISTA 
def gera_cc(registro):
    titulo = registro['titulo'].replace(' ', '').upper()
    artista = registro['artista'].replace(' ', '').upper()
    chave_cc = titulo + artista
    return chave_cc


# A partir das CC's gerados pela busca na tabela de indices secudarios ele busca na tabela de indices primarios e retorna
# os RRN's correspondentes, para que possa ser realizada a impressão no arquivo de saída. (Foi implementado o algoritmo de busca binaria)
def busca_binaria(tabela_indices, chave_busca):
    inicio = 0
    fim = len(tabela_indices) - 1
    chave_busca = chave_busca.upper()

    while inicio <= fim:
        meio = int((inicio + fim) / 2)
        valor = tabela_indices[meio][1].upper()

        if valor == chave_busca:
            return tabela_indices[meio]
        if valor > chave_busca:
            fim = meio - 1
        else:
            inicio = meio + 1

    return False
#******************************** Fim das funções auxiliares ********************************



#******************************** Indice Primario / Indice Secundario ********************************
# A tabela de indices primarios/secundarios é composto de uma lista de tuplas onde cada tupla é composta por (RRN, CC) e (CC, Campo_Busca),
# respectivamente.

# Criar uma tabela de indices primarios, ordenar eles, e retornar a tabela
def tabela_idx_primario(registros):
    # Cria a tabela de indices primarios 
    idx_primario = list()

    # Para cada registro, verificase também o indice dele, que é adotado como RRN do registro
    for count, registro in enumerate(registros):
        key = gera_cc(registro)        
        tupla = (count, key)
        idx_primario.append(tupla)
    
    # Ordenar a tabela de indices primarios, com base na CC, e retorna-la
    idx_primario.sort(key = lambda tup: tup[1])    
    return idx_primario


# Criando a tabela de indices secundarios formada pelo par ordenado: (CC, campo)
def tabela_idx_secundario(registros, campo):
    # Lista que representa a tabela de indices primarios
    idx_secundarios = list()

    # Para cada registro a gente busca o campo no dicionario e adota o conteudo deste campo como
    # chave secundaria, mantendo a chave primaria como sendo a CC
    for registro in registros:
        key_sec = registro[campo].replace(' ', '').upper()
        key_primaria = gera_cc(registro)
        tupla = (key_primaria, key_sec)
        idx_secundarios.append(tupla)

    # Neste caso, não é necessario ordenar a tabela de indices, pois não é utilizada busca binaria encima dela
    #idx_secundarios.sort(key = lambda tup: tup[1])
    return idx_secundarios
#******************************** Fim - Indice Primario / Indice Secundario ********************************



#******************************** Função - Manipulação Idx_Primario / Idx_Secundario ********************************
# É buscado na tabela de indices secundarios o item de busca, caso encontre, utiliza-se a CC para obter o RRN
# dentro da tabela de indices primarios, retornando uma lista contendo os RRN's; caso não encontre, retorna uma lista vazia.
def pesquisarRegistro(chave_busca, idx_primarios, idx_secundarios):
    # Pesquisar na tabela de indices secundarios a chave de busca, retornando uma lista de tuplas contendo os resultados 
    # para a busca, foi utilizado uma função da própria linguagem Python3: filter()
    chave_busca = chave_busca.upper().replace(' ', '')
    valores_idx_secundarios = list()
    valores_idx_secundarios = list(filter(lambda x:chave_busca in x[1], idx_secundarios))
    
    # Verifica se encontrou algum item, caso tenha encontrado (tamanho da lista de tuplas maior que 0),
    # percorre a lista de valores encontrados na tabela de indices secundarios, e utilizando a CC de cada valor,
    # realiza-se a busca binaria dentro da tabela de indices primarios, caso encontre ele guarda o rrn dentro da 
    # lista de RRN's
    if len(valores_idx_secundarios) > 0:
        valores_RRN = list()
        for valor in valores_idx_secundarios:
            resultado = busca_binaria(idx_primarios, valor[0])
            if resultado != False:
               valores_RRN.append(resultado[0])
        return valores_RRN              
    
    # Caso os valores de retorno da pesquisa dentro do idx_secundario venha vazio, retorna uma lista vazia
    return list()
#******************************** Fim - Função - Manipulação Idx_Primario / Idx_Secundario ********************************
    


#******************************** MAIN ********************************
if __name__ == '__main__':
    # Definindo os arquivos 
    arquivo_in = 'musics.txt'
    try:
        arquivo_busca = argv[1]
        arquivo_out = argv[2]
    except IndexError:
        print('ERROR: Quantidade inválida de argumentos insira no seguinte formato:')
        print(f'\n{"[nome do programa] [arquivo de dados] [arquivo de entrada] [arquivo de saída]":^100}\n')
        exit()
    
    # Criando a lista e os dicionarios
    registros = list()
    registro = dict()

    # Funções
    # 1º - Obtém do arquivo de entrada as informações que vão ser buscas na database
    try:
        campo, item_pesquisa = info_busca(arquivo_busca)
    except IndexError:
        arquivo = open(arquivo_out, 'w')
        arquivo.write('Arquivo de entrada vazio!!')
        arquivo.close()
        exit()
    except FileNotFoundError:
        print('ERROR: Arquivo de entrada inexistente!!')
        exit()
    
    # 2º - Armazena da lista todos os registros contidos na database
    registros = armazena(arquivo_in, registro, registros)

    # 3º - Cria tanto a tabela de indices primarios, quanto secudarios
    idx_primarios = tabela_idx_primario(registros)
    try:
        idx_secundarios = tabela_idx_secundario(registros, campo)
    except KeyError:
        arquivo = open(arquivo_out, 'w')
        arquivo.write(f'ERROR: Campo de busca - [{campo}] - inexistente dentro da database!!')
        arquivo.close()
        exit()

    # 4º - Com as tabelas de indices já criadas e a chave de busca já obtida, é buscado então a informação nas tabelas,
    # retornando uma lista contendo os RRN's dos itens caso encontrados, ou então uma lista vazia
    valores = pesquisarRegistro(item_pesquisa, idx_primarios.copy(), idx_secundarios.copy())

    # 5º - Com os RRN's em mãos, é impresso então os registros no arquivo de saída, utilizando o RRN como auxiliar de impressão
    imprime_resultado(arquivo_out, valores, registros)
#******************************** Fim - MAIN ********************************