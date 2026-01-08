
maior = 0
menor = 0
for p in range(1, 5):
    peso = float(input("Peso da {}° pessoa: ".format(p)))
    if p == 0:
        maior = p
        menor = p
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print("O maior peso é o de {}Kg".format(maior))
print("O menor peso foi o de {}Kg".format(menor))