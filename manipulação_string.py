x = int(input("digite um numero de 0 a 9999:"))
if x < 0:
    int(input("digite um numero de 0 a 9999:"))
elif x > 9999:
    int(input("digite um numero de 0 a 9999:"))
else:
    a = str(x)
    a.strip()
    unidade = x // 1 % 10
    dezena = x // 10 % 10
    centena = x // 100 % 10
    milhar = x // 1000 % 10
    print(f"unidade: {unidade} dezena: {dezena} centena: {centena} milhar: {milhar}")
