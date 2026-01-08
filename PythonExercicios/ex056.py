soma = 0
masc = 0
fem = 0
cad = 0
for cad in range(1, 5):
    print("--------{}° PESSOA--------".format(cad))
    n = input("Nome: ")
    idd = int(input("Idade: "))
    s = int(input("Sexo [1 - Masc/ 2 - Fem]: "))
    soma = soma + idd
    if s == 1:
        masc=masc+1
    if s == 2:
        fem = fem + 1
print("Ao todo são {} mulheres e {} homens.".format(fem, masc))
media = soma/4
print("A média de idade do grupo é de {} anos.".format(media))