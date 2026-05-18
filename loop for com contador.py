maior_de_idade = 0
menor_de_idade = 0
for x in range(7):
    from datetime import datetime
    data_pessoa = input("digite uma data nesse formato: DD/MM/AAAA ")
    data_str = datetime.strptime(data_pessoa, "%d/%m/%Y")
    calc = datetime.now() - data_str
    idade = int(calc.days/365.2425)
    if idade >= 18:
        maior_de_idade += 1
    else:
        menor_de_idade += 1
print(f"Total de pessoas maiores de idade: {maior_de_idade}")
print(f"Total de pessoas menores de idade: {menor_de_idade}")
