'''
Possiveis erros:
- Arquivo de entrada e arquivo de operações com linhas em branco (Resolvido)
- Registros com informações faltantes (Resolvido)
- O arquivo de input vir vazio (Resolvido)
- O arquivo de operações vir vazio (Resolvido)
- O elemento sexo vir com outra opção além de 'm', 'f' ou 'n'
- Implementar o limite de caracteres de cada elemento do dicionario professores (Resolvido)
- Em caso de no arquivo de operações, o elemento que indica as op vir diferente de 
  'i' ou 'd', caso venha, não executar aquela operação (Resolvido)
- Na operação de remover, tratar para caso o registro requisitado não exista (Resolvido)
'''

#Bibliotecas
from sys import argv

#Funções - Principais

#Esta função recebe um dicionario e uma lista vazios para serem preenchidos,
#e retorna o valor do topo da pilha de disponibilidade, contida no arquivo de entrada
def armazena(professores, lista_profs, tam):
    cabecalho = linhas[0].split('=')
    #For para armazenar as informações na lista
    #Caso o arquivo input tenha linhas em branco, ou registros com informações faltantes
    #ou fora de formatação, ele pula o registro e passa pro proximo 
    count = 1
    while count < tam:
        conteudo = linhas[count].split('|')
        if len(conteudo) == 7:        
            professores['ci'] = conteudo[0]
            professores['nome'] = conteudo[1]
            professores['sexo'] = conteudo[2]
            professores['idade'] = conteudo[3]
            professores['area'] = conteudo[4]
            professores['tel'] = conteudo[5]
            
            #Amazena o dicionario 'professores' em uma lista,
            #gerando assim, uma lista de dicionarios
            lista_profs.append(professores.copy())
            count += 1
        else:
            count += 1
    return cabecalho[2]

#Esta função recebe o arquivo temporario, a lista de dicionarios, e 
#a lista contendo os valores do topo, que simula o funcionamento de uma pilha,
#e com essas entradas, imprime no arquivo temporario, a lista de dicionarios
#logo ápos passarem pelas operações
def imprime(arquivo, lista_profs, lista_top):
    tam = len(lista_profs)
    arq_out = open(arquivo, 'w')
    
    #Atualizando o top dentro do arquivo, de acordo com o ultimo elemento da lista_top
    temp_top = linhas[0].split('=')
    temp_top[2] = lista_top[len(lista_top) - 1]
    linhas[0] = temp_top[0] + '=' + temp_top[1] + '=' + str(temp_top[2]) + '\n'
    arq_out.write(linhas[0])

    #Imprimindo a lista
    for count in range(0, tam):
        arq_out.write('{:3}|'.format(lista_profs[count]['ci'][:3]))
        arq_out.write('{:30}|'.format(lista_profs[count]['nome'][:30]))
        arq_out.write('{:1}|'.format(lista_profs[count]['sexo'][0]))
        arq_out.write('{:2}|'.format(lista_profs[count]['idade'][:2]))
        arq_out.write('{:30}|'.format(lista_profs[count]['area'][:30]))
        arq_out.write('{:14}|\n'.format(str(lista_profs[count]['tel']).replace('\n', ' ')[0:14]))

    arq_out.close()

#Esta função tem como entrada o arquivo de operações, o valor do topo 
#da pilha de disponibilidade e a lista de dicionarios, a partir disso
#ela verifica quais operações a serem realizadas, e de acordo com as
#operações ela atualiza o valor do topo e a lista de valores do topo 
def operacoes(arquivo_entrada, top, lista_profs):
    #Leitura e tratamento do arquivo de operações 
    arquivo = open(arquivo_entrada, 'r')
    linhas_arquivo = arquivo.readlines()
    arquivo.close()
    tam = len(linhas_arquivo)
    
    #Define o topo como sendo o ultimo, ou primeiro, valor de lista_top
    lista_top = [-1]
    top = lista_top[len(lista_top) - 1]
    
    #Realizando as operações
    count = 0
    while count < tam:
        divisao = linhas_arquivo[count].split(',')
        #Se a linha tiver em branco, ele pula ela
        if divisao[0] == '\n':
            count += 1
        
        else:
            temp = divisao[0].split(' ')
            tipo_op = temp[0]
            reg = divisao[1:]
            key = temp[1]
            count += 1
            #Verificação do tipo de operação a ser feita
            #Se i, adição de registro
            if tipo_op == 'i':
                top = add(key, reg, lista_profs, top, lista_top, tipo_op)
            #Se d, remoção de registro
            elif tipo_op == 'd':
                top = remov(key, lista_profs, top, lista_top, tipo_op)
    return lista_top

#Esta função recebe como entrada o arquivo temporario, o arquivo de saída e
#a lista dos valores da pilha de disponibilidade, com isto, ela faz a 
#'compressão' dos registros após as operações, 'excluindo' os registros
#que passaram pelo processo de remoção, ela também atualiza o topo,
#removendo os valores do topo de acordo com os registros que foram removidos,
#basicamente retornando o topo para o valor inicial
def compress(arquivo_in, arquivo_out, lista_top):
    #Tratamento dos arquivos 
    arquivo_entrada = open(arquivo_in, 'r')
    arquivo_saida = open(arquivo_out, 'w')
    tam = 0
    linhas_entrada = arquivo_entrada.readlines()
    tam = len(linhas_entrada)

    #Atualizando a pilha de disponibilidade
    for count in range(0, tam):
        if (linhas_entrada[count].startswith('*')):
            del(lista_top[len(lista_top) - 1])
    
    #Atualizando o top dentro do arquivo, de acordo com o ultimo elemento da lista_top
    temp_top = linhas_entrada[0].split('=')
    temp_top[2] = lista_top[len(lista_top) - 1]
    linhas_entrada[0] = temp_top[0] + '=' + temp_top[1] + '=' + str(temp_top[2]) + '\n'
    arquivo_saida.write(linhas_entrada[0])

    #Escrevendo no arquivo de saida todos os registros que não foram removidos
    for count in range(1, tam):
        if not (linhas_entrada[count].startswith('*')):
            arquivo_saida.write(linhas_entrada[count])
    
    arquivo_entrada.close()
    arquivo_saida.close()

def verifica_vazio(arquivo, linhas, tam):
    arq = open(arquivo, 'w')

    if tam == 0:
        arq.write('Arquivo de entrada vazio!!!')
        arq.close()
        exit()
    elif linhas[0] == '\n' or linhas[1] == '\n':
        arq.write('Arquivo de entrada vazio!!!')
        arq.close()
        exit()


#Funções -Auxiliares

#Esta função basicamente simula o funcionamento de uma pilha em uma lista,
#substituindo o valor do topo, para caso seja uma operação de adição,
#e inserindo no topo um valor, para caso seja uma opreação de remoção,
#logo, manipula-se somente o topo
def avail_list(tipo, top, lista_top):
    if tipo == 'i':
        del(lista_top[len(lista_top) - 1])
        top = lista_top[len(lista_top) - 1]
        return top
    else:
        lista_top.append(top)
        return top

#Está função é a responsavel por realizar a operação de adição,
#ela recebe o registro, e de acordo com o topo da pilha, ela 
#insere este registro no final ou na posição de disponibilidade
#fornecida pela pilha, e substitui o registro da posição de disponibilidade,
#atualizando a pilha com o auxilio da função avail_list
def add(key, reg, lista_profs, top, lista_top, tipo):
    #Tratar o registro
    elementos = reg
    professores = {}
    
    professores['ci'] = key
    professores['nome'] = elementos[0]
    professores['sexo'] = elementos[1]
    professores['idade'] = elementos[2]
    professores['area'] = elementos[3]
    professores['tel'] = elementos[4]
    
    #Posicionar o registro dentro do vetor 
    #Verificar se o top é -1, se for ele adiciona na ultima posição da lista_profs
    if top == -1:
        lista_profs.append(professores.copy())
    else:
        #Se não, ele adiciona na posição [top] da lista_profs
        del(lista_profs[top])
        lista_profs.insert(top, professores)
        #Atualizar o top
        top = avail_list(tipo ,top, lista_top)
    #Retornar o top
    return top

#Esta função, a partir de uma chave fornecida pelo arquivo de
#operações, procura na lista de dicionarios uma chave (elemento ci)
#que seja compativel com a chave fornecida pelo arquivo de operações
#ele substitui sua chave pelo valor topo da pilha de disponibilidade
#e seu indice é acrescentado a pilha, se tornando o novo topo.
#Caso não encontre a chave fornecida pelo arquivo de operações
#a função não faz nada e simplesmente disconsidera aquela operação
def remov(key, lista_profs, top, lista_top, tipo):
    
    for count in range(0, len(lista_profs)):
        ci = int(lista_profs[count]['ci'].replace('*', ''))
        if int(key) == ci:
            lista_profs[count]['ci'] = '*' + str(top).replace('\n', '')
            top = avail_list(tipo, count, lista_top)
    
    return top


#Main
if __name__ == "__main__":
    #Verificação da quantidade de argumentos
    if len(argv) != 5:
        print('''Quantidade de argumentos inválida!!\n Insira:
        [nome do programa] [arquivo de entrada] [arquivo de operações] [arquivo de saída temporário] [arquivo de saída final]''')
        exit()
    
    #Declaração do nome dos arquivos 
    input = argv[1]
    operations = argv[2]
    temp = argv[3]
    output = argv[4]

    #Manipulação do arquivo de entrada
    arq_in = open(input, 'r')
    linhas = arq_in.readlines()
    arq_in.close()
    tam = len(linhas)
    
    verifica_vazio(output, linhas, tam)

    #Declarando o dicionario e as listas
    professores = {}
    lista_profs = []
    lista_top = []
    
    #Executando a manipulação das informações 
    top = armazena(professores, lista_profs, tam)
    lista_top = operacoes(operations, top, lista_profs)
    imprime(temp, lista_profs, lista_top)
    compress(temp, output, lista_top)
