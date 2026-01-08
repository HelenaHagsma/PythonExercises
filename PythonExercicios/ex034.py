s = float(input("Digite seu salário: "))
if s>1250:
    print("Seu salário teve um aumento de 10%. Seu novo salário é: R${:.2f}".format(s*1.10))
else:
    print("Seu salário teve um aumento de 15%. Seu novo salário é: R${:.2f}".format(s * 1.15))