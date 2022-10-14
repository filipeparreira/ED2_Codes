'''
Informações de cada professor:
    - Código Identificador: Inteiro de até 3 dígitos
    - Nome: até 30 caracteres
    - Sexo: 1 caractere, 3 opções(f, m, n)
    - Idade: Inteiro de 2 dígitos
    - Área de Especialidade: até 30 caracteres
    - Telefone: 14 digitos, seguindo o formato, (XX)XXXXX-XXXX
Notas:
    - O programa deverá conter funções de adição, remoção, inserção e updates
    - O programa vai recerber duas entradas e terá que ter duas saídas
    - Entrada: 
        - Arquivo de registro, contendo o registro de professores e na primeira linha, o tamanho de cada registro em 
        bytes e o endereço do primeiro registro da pilha de disponibilidade
        - Arquivo de operações, onde contém todas as operações que tem de ser feitas encima do arquivo de registro,
        serão descritas duas operações, inserção e remoção, elas tem sintaxe própria
    - Saída:
        - Arquivo de saída temporário, arquivo onde vai conter as edições feitas no arquivo de entrada logo após passa-
        rem pelo arquivo de operações, este arquivo vai passar pelo processo de compactação, "apagando" os registros
        que contém '*' no inicio.
        - Arquivo de saída final, arquivo que contém os registros restantes após todas as manipulações feitas pelo pro-
        grama, e após a compactação desses registros. 
'''

#Definição da classe Professores
class Professores:
    professores = 'Professores'

    def __init__(self, codIdent = None, nome = None, sexo = None, idade = None, espec = None,
    tel = None):
        self.codIdent = codIdent[0:3]
        self.nome = nome[0:30]
        self.sexo = sexo[0]
        self.idade = idade[0:2]
        self.espec = espec[0:30]
        self.tel = tel[0:14]


def imprime(arq_out, vet_linhas):
    arquivo = open(arq_out, 'w')
    tam = len(vet_linhas)
    
    for count in range(1, tam):
        elementos_reg = vet_linhas[count].split('|')
        
        Lista = Professores(elementos_reg[0], elementos_reg[1], elementos_reg[2], elementos_reg[3], elementos_reg[4], elementos_reg[5])

        arquivo.write('{:3}|'.format(Lista.codIdent))
        arquivo.write('{:30}|'.format(Lista.nome))
        arquivo.write('{:1}|'.format(Lista.sexo))
        arquivo.write('{:2}|'.format(Lista.idade))
        arquivo.write('{:30}|'.format(Lista.espec))
        arquivo.write('{:14}\n'.format(Lista.tel))
        
    arquivo.close()


#Retorna a chave canonica de uma linha do arquivo
def gera_chave(linha):
    elementos_reg = linha.split('|')
    chave = int(elementos_reg[0])
    return chave


#Busca uma chave canonica em um arquivo e retorna a linha caso encontre,
#ou retorna -999 caso não encontre
def busca_chave(arquivo, chave_busca):
    arquivo = open(arquivo, 'r')
    linhas = arquivo.readlines()
    tam = len(linhas)
    retorno = -999
    for count in range(1, tam):
        chave = gera_chave(linhas[count])
        if chave == chave_busca:
            retorno = count + 1 
    arquivo.close()
    return retorno


def remover(arquivo, chave):
    arquivo = open(arquivo, 'w+')
    linhas = arquivo.readlines()

    resultado_busca = busca_chave(arquivo, chave)

    if resultado_busca != -999:
        linhas.insert(resultado_busca, '*')
        arquivo.writelines(linhas)

    arquivo.close()    


if __name__ == "__main__":
    
    #Abrindo o arquivo e armazenando em input_reg, onde cada elemento do vetor é uma linha
    arq_in_reg = open('input1.txt', 'r')
    input_reg = arq_in_reg.readlines()
    arq_in_reg.close()
    
    #Testes encima do input_reg
    chave = gera_chave(input_reg[1]) 
    imprime('saida_teste.txt', input_reg)
    
    #print(chave)
    chave_busca = 50
    resultado = busca_chave('saida_teste.txt', chave_busca)
    print(resultado)
    print(input_reg[resultado + 1])
    remover('saida_teste.txt', 50)
