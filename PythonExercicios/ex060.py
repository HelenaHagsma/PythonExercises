c = 0
print("_______FIBONACCI_______")
n = int(input("Digite um número: "))
for c in range(n-1, 0, -1):
    print(n, " x ", c, " = ", end= " ")
    n = n * c
    print(n)
