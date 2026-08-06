dados = {}
nome = input("digite seu nome: ")
nascimento = int(input("digite o ano de nascimento: "))
carteira_trabalho = int(input("número da carteira de trabalho: "))
dados["nome"] = nome
dados["idade"] = 2026 - nascimento
dados["numero da carteira de trabalho"] = carteira_trabalho

if dados.get("numero da carteira de trabalho") == 0:
    print(dados)
else:
    ano_contratacao = int(input("digite o ano em que voce foi contratado: "))
    salario = float(input("digite o seu salario: "))
    dados["ano de contratação"] = ano_contratacao
    dados["salário"] = salario
    ano_aposentadoria = ano_contratacao + 35
    dados["aposentadoria"] = ano_aposentadoria - nascimento
    print(dados)
