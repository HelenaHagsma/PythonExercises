d = int(input("Informe quantos dias o carro foi alugado: "))
km = float(input("Informe quantos km foram rodados durante esse período: "))
pd = d*60
pkm = km*0.15
print("O valor a pagar é: R${:.2f}".format(pd+pkm))