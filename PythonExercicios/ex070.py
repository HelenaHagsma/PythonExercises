contMil = s = cont = menor = 0
barato=""
print("--------MERCADO BOM DE PREÇO‐-------")
while True:
	n = str(input("Nome do produto: "))
	p = float(input("Preço do produto: "))
	e = int(input("Vai continuar? 1 - SIM | 2 - NÃO: "))
	cont = cont + 1
	s = s + p
	if p > 1000:
		contMil = contMil + 1
	if cont == 1:
		menor = p
		barato = n
	else:
		if p < menor:
			menor = p
			barato = n
	if e == 2:
		break
print("O valor total da compra é: R${}".format(s))
print("Existem {} produto(s) com valor maior que R$1000!".format(contMil))
print("O produto com menor valor é o/a {}".format(barato))
print("Programa encerrado.")
