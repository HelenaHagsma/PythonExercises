contI = 0
contSM = 0
contSF = 0
while True:
    i = int(input("Informe a idade: "))
    s = input("Informe o sexo (F|M): ")
    e = int(input("Quer continuar? 1 - SIM | 2 - NÃO: "))
    if i > 18:
        contI = contI + 1
    if s in "Mm":
        contSM = contSM + 1
    if s in "Ff":
        if i < 20:
            contSF = contSF + 1
    if e == 2:
        break
print("Ao todo são {} pessoas maiores de idade. ".format(contI))
print("Ao todo são {} homens.".format(contSM))
print("Ao todo são {} mulheres menores de 20 anos.".format(contSF))
print("Programa encerrado. ")