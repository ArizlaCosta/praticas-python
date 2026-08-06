import random
vitorias = 0
resultado = 0

while True:
    computador = random.randint(1,10)
    numero = int(input("digite um numero de um a dez: "))
    while numero < 1 or numero > 10:
        print("Número inválido! Digite apenas valores entre 1 e 10.")
        numero = int(input("digite um numero de um a dez: "))
    paroimpa = input("par ou ímpar? ").lower().strip().replace("í", "i")
    resultado = numero + computador
    if resultado % 2 == 0 and paroimpa == "par":
        print(f"O computador jogou {computador}. A soma deu {resultado}. Você GANHOU!")
        vitorias += 1
    elif resultado % 2 != 0 and paroimpa == "impar":
        print(f"O computador jogou {computador}. A soma deu {resultado}. Você GANHOU!")
        vitorias += 1
    else:
        print(f"O computador jogou {computador}. A soma deu {resultado}. Você PERDEU!")
        break

print(f"vc ganhou {vitorias} vezes")
