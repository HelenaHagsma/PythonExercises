p = float(input("Informe o preço do produto: "))
f = int(input("Informe a condição de pagamento:\n1 - Dinheiro/ Cheque\n2 - Cartão à Vista\n3 - Em até 2x no Cartão\n4 - Acima de 3x no Cartão\nInforme:"))
if f == 1:
    print("Produto com 10% de desconto: R${:.2f}".format(p*0.90))
elif f == 2:
    print("Produto com 5% de desconto: R${:.2f}".format(p * 0.95))
elif f == 3:
    print("Produto com preço normal: R${:.2f}".format(p))
elif f == 4:
    print("Produto com 20% de acréscimo: R${:.2f}".format(p * 1.20))