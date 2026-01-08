t = 0
n = int(input("Informe um número: "))
for c in range(1, n +1):
    if n%c==0:
        print('\033[33m', c, end='')
        t = t + 1
print("\nO número {} foi dividido {} vezes.".format(n, t))
if t ==2:
    print("Por isso, é primo.")
else:
    print("Por isso não é primo.")





