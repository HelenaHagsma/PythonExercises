v = float(input("Informe a velocidade do carro: "))
if v>80:
    print("VOCÊ FOI MULTADO! Terá que pagar uma multa de R${:.2f}.".format((v-80)*7))