arquivo = open('vazio.txt', 'r')
linhas = arquivo.readlines()

print(len(linhas))
if linhas[0] == '\n':
    print('A primeira linhas é vazia')