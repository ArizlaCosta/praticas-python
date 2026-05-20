estoque = [
    ("Memória RAM 16GB", 3, 350.00),
    ("Gabinete White Edition", 12, 450.00),
    ("SSD M.2 1TB", 2, 290.00),
    ("Fonte ATX 750W", 8, 510.00),
    ("Water Cooler 240mm", 4, 400.00)
]

reposicao = []
valor_total = 0

for produto, quantidade, preco in estoque:
    valor_total += (quantidade * preco)

    if quantidade < 5:
        reposicao.append(produto)

print(f"valor total: {valor_total}")
print("Produtos que precisam de reposição (menos de 5 unidades):")
for item in reposicao:
    print(f"produtos com menos de 5 unidades: {item}")
