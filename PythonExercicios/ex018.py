from math import cos, sin, tan, radians
n = int(input("Digite um ângulo: "))
print("O seno de {} é {:.2f}\no cosseno é {:.2f}\ne a tangente é {:.2f}.".format(n, sin(radians(n)), cos(radians(n)), tan(radians(n))))