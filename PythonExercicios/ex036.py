vc = float(input("Informe o valor da casa: "))
s = float(input("Informe o seu salário: "))
a = int(input("Informe em quantos anos irá pagar: "))
prest = vc / (a*12)
sal = s*(30/100)
if prest > sal:
    print("Empréstimo negado!")
else:
    print("Empréstimo aprovado!")