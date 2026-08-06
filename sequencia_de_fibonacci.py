print("-----------------------------SEQUENCIA DE FIBONACCI-----------------------")
numero = int(input("digite um numero: "))

voltas = 3
x = 0 
y = 1
print(x)
print(y)

while voltas <= numero:
    z = x + y
    x = y
    y = z
    print(z)
    voltas += 1
