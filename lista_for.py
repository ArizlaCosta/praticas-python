lista = []
for i in range(5):
    var = int(input("digite 5 numeros aleatorios "))
    lista.append(var)
mi = min(lista)
ma = max(lista)
posmi = lista.index(mi)
posma = lista.index(ma)
print(f"o menor valor é {mi}, na posição {posmi} \n o maior valor é {ma} na posição {posma}")
