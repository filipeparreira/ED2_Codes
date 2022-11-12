
def armazena(arquivo_in):
    arquivo = open(arquivo_in, 'r')
    linhas = arquivo.readlines()
    
    #Armazenando as informações do cabeçalho
    cabecalho = linhas[0].split('=')
    
    #Quantidade
    cabecalho_aux = cabecalho[3].split(' ')
    qntd = int(cabecalho_aux[0])

    #Tipo de ordenação
    cabecalho_aux = cabecalho[4].split(' ')
    tipo_ord = cabecalho_aux[0]

    #Ordem da ordenação
    cabecalho_aux = cabecalho[5].split(' ')
    ordem = cabecalho_aux[0]

    #Armazendando as keys
    count = 1
    keys = []
    
    while count < len(linhas):
        conteudo = linhas[count].split('|')
        keys.append(conteudo[0])
        count += 1

    arquivo.close()

    return qntd, tipo_ord, ordem, keys


if __name__ == '__main__':
    #Recebendo o arquivo:
    arquivo_in = 'input1.txt'
    arquivo_saida = 'saida_teste1.txt'
    
    #Armazena quantidade, tipo_ord, ordem, keys
    quantidade, tipo_ord, ordem, keys = armazena(arquivo_in)

    
