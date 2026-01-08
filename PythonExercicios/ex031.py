d = float(input("Informe  a distância da viagem em Km: "))
if d<=200:
    print("O valor da passagem é R${}.".format(d*0.50))
else:
    print("O valor da passagem é R${}.".format(d*0.45))