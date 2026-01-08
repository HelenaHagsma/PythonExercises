from math import sqrt
co = float(input("Digite o cateto oposto do triângulo: "))
ca = float(input("Digite o cateto adjacente do triângulo: "))
hip = sqrt((co**2)+(ca**2))
print("O comprimento da hipotenusa é {:.2f}cm.".format(hip))