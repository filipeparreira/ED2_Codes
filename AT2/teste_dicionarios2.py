arq_in = open('input1.txt', 'r')
linhas = arq_in.readlines()
arq_in.close()
tam = len(linhas)


#declarando o dicionario e a lista
professores = {}
lista_profs = []
#For para armazenar as informações na lista
for count in range(1, tam):
    conteudo = linhas[count].split('|')
    
    professores['ci'] = conteudo[0]
    professores['nome'] = conteudo[1]
    professores['sexo'] = conteudo[2]
    professores['idade'] = conteudo[3]
    professores['area'] = conteudo[4]
    professores['tel'] = conteudo[5]
    lista_profs.append(professores.copy())
    
arq_out = open('saida_teste_dict.txt', 'w')

#Imprimindo a lista
arq_out.write(linhas[0])
for count in range(1, tam - 1):
    arq_out.write('{:3}|'.format(lista_profs[count]['ci']))
    arq_out.write('{:30}|'.format(lista_profs[count]['nome']))
    arq_out.write('{:1}|'.format(lista_profs[count]['sexo']))
    arq_out.write('{:2}|'.format(lista_profs[count]['idade']))
    arq_out.write('{:30}|'.format(lista_profs[count]['area']))
    arq_out.write('{:14}\n'.format(lista_profs[count]['tel']))

arq_out.close()

