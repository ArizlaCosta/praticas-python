#Escreva um programa que percorra a lista de tentativas do usuário. Se a porta que ele 
#quer abrir NÃO estiver na lista de portas seguras, adicione essa porta em uma lista 
#chamada portas_bloqueadas. No final, se a lista de bloqueadas não estiver vazia, exiba 
#um alerta de segurança com as portas proibidas.

portas_seguras = [80, 443, 22, 8080]
tentativas_usuario = [80, 21, 443, 3306, 22, 25]
portas_bloqueadas = []

for i in tentativas_usuario:
    if i not in portas_seguras:
        portas_bloqueadas.append(i)
        contar = len(portas_bloqueadas)
    else:
        pass

if contar != 0:
            print("alerta")
              
print(portas_bloqueadas)
