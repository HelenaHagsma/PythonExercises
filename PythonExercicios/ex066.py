c = cont = s = 0
while True:
    n = int(input("Digite um número: "))
    if n == 999:
        break
    cont = cont + 1
    s = s + n
print("Foram digitados {} números e a soma entre eles é {}".format(cont, s))