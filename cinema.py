lotacao_atual = 150
ingresso_inteiras = 50
ingresso_meias = 25
fila_vips = 15
print ("seja bem vindo! \n filme:dgjrvhj,bjgkfhwffhhb \n classificação: 18 \n valores: \n meia = 25,00 \n inteira: 50,00 ")
idade_minima = int(input("digite sua idade"))
if idade_minima < 18:
    print("voce e menor de 18 anos, nao pode assistir o filme")
elif lotacao_atual >= 220:
    print("a sala está cheia, escolha outro horario")
else:
    ingresso = input("escolha seu ingresso: gratis/meia/inteira")
    if ingresso == "gratis":
        ingresso_gratis = input("possui credencial ou é funcionario de folga? s/n")
        if ingresso_gratis == "s":
            pass
        else:
            print("por favor, escolha outro ingresso")
    elif ingresso == "meia":
        ingresso_meia = input("é estudante, idoso ou doador de sangue? s/n")
        if ingresso_meia == "s":
            pass
        else:
            print("por favor, escolha outro ingresso")
    else:
        pass
if ingresso != "gratis":
    fila_vip = input("voce quer fila vip? s/n")
if ingresso == "inteira" and fila_vip == "s":
    total_ingresso = ingresso_inteiras + fila_vips
    print(f"o valor do seu ingresso é {total_ingresso}")
elif ingresso == "meia" and fila_vip == "s":
    total_ingresso = ingresso_meias + fila_vips
    print(f"o valor do seu ingresso é {total_ingresso}")
elif ingresso == "inteira":
    total_ingresso = ingresso_inteiras
    print(f"o valor do seu ingresso é {ingresso_inteiras}")
elif ingresso == "meia":
    total_ingresso = ingresso_meias
    print(f"o valor do seu ingresso é {ingresso_meias}")
else:
   pass
