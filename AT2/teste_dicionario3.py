import zlib, sys

#Salva em outro arquivo as linhas onde o registro não começa com *
file1 = open('arquivo_entrada.txt', 'r') #abre o arquivo de entrada para leitura  
file2 = open('arquivo_saida.txt', 'w') #abre o arquivo de saída para escrita 

for line in file1.readlines(): #precorre linha por linha do arquivo de entrada 
    
    if not (line.startswith('*')): #se a linha não conter *
      
        print(line) 
        file2.write(line) #a linha é escrita no arquivo de saída 

file2.close() #fecha o arquivo de saida
file1.close() #fecha o arquivo de entrada 

#Compacta o arquivo em que os registros que não começam com * foram salvos
file2 = "data"
file3 = "compressed_data"

with open(file2, mode="rb") as fin, open(file3, mode="wb") as fout:
    data = fin.read()
    compressed_data = zlib.compress(data, zlib.Z_BEST_COMPRESSION)
    #print(f"Original size: {sys.getsizeof(data)}")
    # Original size: 1000033
    #print(f"Compressed size: {sys.getsizeof(compressed_data)}")
    # Compressed size: 1024

    fout.write(compressed_data)