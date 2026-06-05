#lista com os ips
ips_acesso = [
    "192.168.1.1", "10.0.0.5", "192.168.1.1", 
    "172.16.0.2", "10.0.0.5", "192.168.1.100"
]

#criando listas vazias para receber os ips unicos e duplicados
unico = []
duplicado = []

#criando o loop para percorrer a lista de ips_acesso
for ip in ips_acesso:
#para cada ip na lista de ips_acesso
        contar = ips_acesso.count(ip)
#crie uma variável para usar o count e contar quanto de cada tipo de elemento tem na lista
        if contar == 1:
#se a quantidade de elementos for maior que 1
                if ip not in unico:
#se o ip já não estiver na lista de úcnicos
                       unico.append(ip)
#adicionar os ips unicos á lista
        else:
#se não
                if ip not in duplicado:
#se o ip já não estiver na lista de duplicados
                        duplicado.append(ip)
#adicionar os ips duplicados á lista

print(unico)
#mostre a lista com os ips únicos
print(duplicado)
#mostre a lista com os ips duplicados

#OBS: Não dá pra utilizar comparadores em listas porque comparadores não conseguem comparar listas, apenas números. E a lista é composta por strings, o comparador só pode comparar números. por isso deve-se utilizar o método 
#count que devolve o numero de elementos da lista em inteiro
