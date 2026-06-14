#Aqui são 3 exercicos em 1

#crie uma lista com cada número multiplicado por 3.
numeros = [1, 2, 3, 4, 5]
resultado = [n * 3 for n in numeros]
print(resultado)

#crie uma lista só com os nomes que têm mais de 4 letras.
nomes = ["ana", "bruno", "carlos", "diana"]
nomegrande = [n for n in nomes if len(n) > 4]
print(nomegrande)

#crie uma lista com os ímpares ao quadrado.
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
quadrados = [n ** 2 for n in num if n % 2 != 0]
print(quadrados)
