def gera_key(arquivo, linha):
    arquivo = open(arquivo, 'r')
    linhas = arquivo.readlines()
    linha = linhas[linha]
    
    itens = linha.split('|')

    nome, sobrenome = itens[0].strip().upper().replace(' ', ''), itens[1].strip().upper().replace(' ', '')
    key = nome + sobrenome
    
    arquivo.close()

    return key

def ord(arquivo):
    arquivo = open(arquivo, 'r')
    linhas = arquivo.readlines()
    tam = len(linhas)
    arquivo.close()




if __name__ == "__main__":
    
    arquivo = 'heroi.txt'

    key = gera_key(arquivo, 4)




