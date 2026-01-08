n = int(input("Informe um número: "))
print("Escolha a base de conversão:\n1 - Binário\n2 - Octal\n3 - Hexadecimal\n")
e = int(input("Digite a sua escolha: "))
if e == 1:
    print("A conversão de {} para binário é {}.".format(n, bin(n)[2:]))
elif e == 2:
    print("A conversão de {} para octal é {}.".format(n, oct(n)[2:]))
elif e == 3:
    print("A conversão de {} para hexadecimal é {}.".format(n, hex(n)[2:]))
