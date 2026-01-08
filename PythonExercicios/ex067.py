c = 0
print("----TABUADA!----")
while True:
    n = int(input("Digite um número: "))
    if n < 0:
        break
    for i in range (0, 11):
        print(n, " x ", i, " = ", n * i)
print("Programa encerrado.")

