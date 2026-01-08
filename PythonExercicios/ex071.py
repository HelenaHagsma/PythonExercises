from math import floor
print("==================")
print("BANCO DEV")
print("==================")
saque = float(input("Quanto voce quer sacar? R$"))
n50 = saque / 50
n50r = saque % 50
n20 = n50r /20
n20r = saque % 20
n10 = n20r /10
n10r = saque % 10
n5 = n10r/5
print("Notas de R$50 ---> {}".format(floor(n50)))
print("Notas de R$20 ---> {}".format(floor(n20)))
print("Notas de R$10 ---> {}".format(floor(n10)))
print("Notas de R$5 ---> {}".format(floor(n5)))
print("=================")
print("Volte sempre!")