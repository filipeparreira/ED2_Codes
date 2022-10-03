arq = open('arquivo_teste.txt', 'w+')

arq.writelines('linha 1\n')
arq.writelines('linha 2')
arq.writelines('linha 3')
arq.writelines('linha 4')

arq.close()