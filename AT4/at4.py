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
# Para o funcionamento do indice primario
    # Ler um registro com base no RRN
    # Ordenar o arquivo de indices 
    # Gerar chave canonica
    # Criar tabela de indices, onde cada indice é uma tupla (RRN, cc)
    # Carregar as informações dos registros para a tabela de indices 
    # Pesquisar baseado na chave canonica

# Manipulando os dados do arquivo
    # Abro o arquivo de entrada, leio e armazeno as informações contidas nele
def armazena(arquivo, dicionario, lista):
    arquivo = open(arquivo, 'r')
    linhas = arquivo.readlines()
    
    # Guardadando a quantidade de registros no arquivo
    cabecalho = linhas[0].split('QTDE=')
    cabecalho_aux = cabecalho.split(' ')
    quantidade = cabecalho_aux[0]
    
    for count in range(1, len(linhas)):
        itens = linhas[count].split('|').strip()
        if len(itens) == 6:
            dicionario['ano'] = itens[0]
            dicionario['duracao'] = itens[1]
            dicionario['titulo'] = itens[2]
            dicionario['artista'] = itens[3]
            dicionario['genero'] = itens[4]
            dicionario['idioma'] = itens[5]

            lista.append(dicionario)
    
    return quantidade, dicionario
    
    # Defino o tamanho dos itens do arquivo

# Main
if __name__ == '__main__':
    # Definindo os arquivos 
    arquivo_in = 'musics.txt'
    arquivo_busca = 'entrada1.txt'
    arquivo_out = 'saida1.txt'

    # Criando a lista e os dicionarios
    registros = list()
    registro = dict()

    # Funções
    quantidade, registros = armazena(arquivo_in, registro, registros)


