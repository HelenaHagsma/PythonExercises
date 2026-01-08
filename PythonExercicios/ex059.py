import random
e = 0
while e != 5:
 n1 = int(input("Primeiro número: "))
 n2 = int(input("Segundo número: "))
 e = int(input("Escolha uma das opções: \n1) SOMAR\n2) MULTIPLICAR\n3) MAIOR\n4) TROCAR NÚMEROS\n5) SAIR DO PROGRAMA\n---->"))
 if e == 1:
  s = n1 + n2
  print("O resultado da soma é: {}".format(s))
 if e == 2:
  m = n1 * n2
  print("O resultado da multiplicação é: {}".format(m))
 if e == 3:
  if n1 > n2:
   print("O maior número é: {} ".format(n1))
  if n2 > n1:
   print("O maior número é: {}".format(n2))
 if e == 4:
  n1 = random.randint(0, 10)
  n2 = random.randint(0, 10)
  print("Os números foram trocados! Os valores agora são: {} e {}".format(n1, n2))
print("Programa encerrado.")