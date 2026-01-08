c = 0
cont = 0
s = 0
while c < 10:
    n = int(input("Digite um número: "))
    cont = cont + 1
    s = s + n
    if n == 999:
        s = s - 999
        break
print("Número proibido!")
print("Você digitou {} números.".format(cont))
print("A soma entre os números digitados é: {}.".format(s))

''' c= 0
    s = 0
    cont = 0
    while True:
        n = int(input("Digite um número: "))
        if n == 999:
            break(fim do loop true)
        s = s + n
    print("A soma é: )'''
