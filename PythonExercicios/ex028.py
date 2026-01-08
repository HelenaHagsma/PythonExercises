import random
num = random.randint(1, 10)
print("--------- ADIVINHE O NÚMERO! ----------")
print("Acerte o número de 1 a 10!")
n = int(input("Digite um número: "))
print("O número sorteado foi: {}".format(num))
if n==num:
    print("\033[1;32mVocê acertou!\033[m")
else:
    print("\033[1;31mVocê errou. Vou sortear outro número!\033[m")
