c = 0
s = 0
med = 0
cont = 0
maior = 0
menor = 0
while c < 10:
    n = int(input("Digite um número: "))
    e = int(input("1 - Parar | 2 - Continuar: "))
    cont  = cont + 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    s = s + n
    if e == 1:
        med = s/cont
        break
print("A média entre os valores informados é: {:.2f}".format(med))
print("O menor número informado é: {}, e o maior é: {}.".format(menor, maior))