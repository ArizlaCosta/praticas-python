print("digite dois numeros")
numero1 = int(input("digite o 1 numero: "))
numero2 = int(input("digite o 2 numero: "))
a = 1
lista = []
lista.append(numero1)
lista.append(numero2)

while a == 1:
    print("------------------------------MENU-------------------------------------- \n escolha uma função: \n [1]somar \n [2]multiplicar \n [3]maior \n [4]novos numeros \n [5]sair do programa ")
    r = int(input(""))
    if r == 1:
        soma = numero1 + numero2
        print(f"a soma dos dois números é {soma}")
    elif r == 2:
        multiplicação = numero1 * numero2
        print(f"o produto dos dois números é {multiplicação}")
    elif r == 3:
        maior = max(lista)
        print(f" o maior número é {maior}")
    elif r == 4:
        print("digite dois numeros")
        numero1 = int(input("digite o 1 numero: "))
        numero2 = int(input("digite o 2 numero: "))
    elif r == 5:
        a = 0
        print("acabou")
    else:
        print("digite uma opção válida")
