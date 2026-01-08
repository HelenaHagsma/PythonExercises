from random import randint
c = randint(0,10)
j = int(input("Tente adivinhar o número de 0 a 10: "))
while c != j:
    j = int(input("Errou! Tente denovo: "))
print("Você acertou!!")