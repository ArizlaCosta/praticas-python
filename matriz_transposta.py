original = [
    [1, 2, 3],
    [4, 5, 6]
]

linha = len(original) #conta quantas linhas tem original
coluna = len(original[0]) #conta quantas colunas tem original a partir da linha 0
transposta = [] #cria a lista que vai guardar a matriz nova transposta

for i in range(coluna): #cria 3 linhas
    transposta.append([0] * linha)#multiplica o numero de colunas(3) pelo de linha(2)  
    # e cria a matriz inversa
                                

for x in range(linha): #acessa as linhas da original
    for y in range(coluna): #acessa a coluna da original
        transposta[y][x] = original[x][y] #preenche a transposta de acordo com os numeros
        #da origimal na ordem da transposta

for linha in transposta: #le as linhas da transposta
    print(linha) #printa
