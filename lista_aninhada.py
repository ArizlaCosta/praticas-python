nome_e_peso = []
lista_aninhada = []

for i in range(3):
    a = input("digite seu nome ")
    b = input("digite seu peso ")
    nome_e_peso.append(a)
    nome_e_peso.append(b)
    lista_aninhada.append(nome_e_peso[:])
    nome_e_peso.clear()

#o calculo deve ser feito depois do primeiro for e fora do loop, senão ele faz o calculo
#com a lista vazia

pesos = [float(p[1]) for p in lista_aninhada] #pega o peso
maisleve = min(pesos)
maispesado = max(pesos)

#o segundo for também tem que estar separado fo primeiro

for p in lista_aninhada:
    if float(p[1]) == maisleve:
        print(f"a pessoa mais leve é {p[0]}") #printa o nome
for p in lista_aninhada:
    if float(p[1]) == maispesado:
        print(f"a pessoa mais pesada é {p[0]}") #printa o nome
print(f"{len(lista_aninhada)} pessoas foram cadastradas")
