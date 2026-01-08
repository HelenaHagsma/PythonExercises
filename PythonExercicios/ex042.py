l1 = float(input("Digite o comprimento da primeira reta: "))
l2 = float(input("Digite o comprimento da segunda reta: "))
l3 = float(input("Digite o comprimento da terceira reta: "))

if l1 == l2 == l3:
    print("O triângulo é EQUILÁTERO.")
elif l1 == l2 != l3 or l1 == l3 != l2 or l2 == l3 != l1:
    print("O triângulo é ISÓSCELES.")
elif l1 != l2 != l3:
    print("O triÂngulo é ESCALENO.")
