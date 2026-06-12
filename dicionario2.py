produtos = [
    {"nome": "Teclado Mecânico", "preco": 150},
    {"nome": "Mouse Gamer", "preco": 80},
    {"nome": "Monitor 24'", "preco": 850},
    {"nome": "Headset USB", "preco": 210},
    {"nome": "Mousepad XL", "preco": 50}
]
soma = 0
desconto = 0
for p in produtos:
    print(f"{p['nome']}: ${p['preco']}")
    soma += p['preco']
    if p["preco"] > 200:
        desconto += p["preco"] * 0.90
    else:
        desconto += p["preco"]
print(f"O total final da compra com os descontos aplicados é: R$ {desconto}")
print(f"a soma de todos os produtos é {soma}")
