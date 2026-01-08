from random import choice

print("\033[1;33m--------- JOKENPÔ! --------\033[m")

print("\033[1;34m >>>> Você começa!\033[m\n1 - Pedra\n2 - Papel\n3 - Tesoura")
print("\033[;37m-------------- 1, 2, 3 e... JÁ! ---------------\033[m\n")
x = int(input("\033[1;34m >>>> Digite o número da sua escolha: \033[m"))

if x == 1:
    print("\033[1;34m >>>> Sua escolha é\033[1;33m Pedra\033[m\033[1;34m!\033[m")
elif x == 2:
    print("\033[1;34m >>>> Sua escolha é \033[1;33mPapel\033[m\033[1;34m!\033[m")
elif x == 3:
    print("\033[1;34m >>>> Sua escolha é\033[1;33m Tesoura\033[m\033[1;34m!\033[m")

lista = ['Pedra', 'Papel', 'Tesoura']
y = choice(lista)
print("\033[1;34m >>>> A minha escolha é...\033[m \033[1;33m{}\033[m\033[1;34m!\033[m".format(y))

if x == 1 and y == lista[0] or x == 2 and y == lista[1] or x == 3 and y == lista[2]:
    print("\033[1;34m >>>>\033[m\033[1;35m Empate! Nosso pensamento está interligado!\033[m")
elif x == 1 and y == lista[1] or x ==2 and y == lista[2] or x == 3 and y == lista[0]:
    print("\033[1;34m >>>>\033[m \033[1;31mUhuul! Ganhei!\033[m")
elif x == 1 and y ==lista[2] or x == 2 and y == lista[0] or x == 3 and y == lista[1]:
    print("\033[1;34m >>>>\033[m \033[1;32mVocê ganhou! Mandou bem.")