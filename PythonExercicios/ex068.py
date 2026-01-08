from random import randint
cont = cont1 = 0
print("=-=-=-=-=-=-=-=-=-=-=-=-=-==-")
print("VAMOS JOGAR!")
print("=-=-=-=-=-==-=-=-=-=-=-=-=-=-")
while True:
	n = int(input("Digite o número: "))
	e = str(input("Escolha PAR ou IMPAR: "))
	if e == "PAR":
		print("Eu fico com IMPAR!")
	else:
		print("Eu fico com PAR!")
	num = randint(1, 10)
	print("O número que escolho é: {}".format(num))
	dec = n + num
	if dec % 2 ==0 and e == "PAR":
		print("Você ganhou!")
		cont = cont + 1
	if dec % 2 != 0 and e == "IMPAR":
		print("Você ganhou!")
		cont = cont + 1
	if dec % 2 != 0 and e == "PAR":
		print("Você perdeu!")
		cont1 = cont1 + 1
		break
	if dec % 2 ==0 and e == "IMPAR":
		print("Você perdeu!")
		cont1 = cont1 + 1
		break
print("Voce ganhou {} vezes, e perdeu {} vezes.".format(cont, cont1))
print("Não fique triste, vamos jogar denovo?")