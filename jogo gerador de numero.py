import random
import time
resultados = {}

for j in range(1,5):
    numero_aleatorio = random.randint(1,10)
    time.sleep(1)
    resultados[j] = numero_aleatorio
    print(f"jogador{j} tirou {numero_aleatorio}")

print("-------------------RESULTADOS---------------------------------------------")
resultados_ordenados = sorted(resultados.items(), key=lambda item: item[1], reverse=True)

for posicao, (jogador, pontos) in enumerate(resultados_ordenados):
    time.sleep(1)
    print(f"{posicao + 1}º lugar: Jogador {jogador} ficou com {pontos} pontos")

# posicao, (jogador, pontos)a posição tá separada porque ela é um valor independente, 
# enquanto (jogador,pontos) são valores que precisam estar juntos, 
# se não ele poderia escolher qualquer jogador pra qualquer ponto

#enumerate() cria as posicoes (1,2,3,4) e o {posicao + 1} impede que ele imprima 
#posicao 0

#sorted()le e organiza o dicionario
#resultado.items() junta as chaves com os valores e cria a tupla pro sorted ler
#key= coloca a chave em primeiro
#lambda item: item[1] decide qual elemento deve ser comparado 
#reverse=true ordena os resultados em ordem decrescente
