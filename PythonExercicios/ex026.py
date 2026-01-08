f = str(input("Digite uma frase: "))
count1 = str(f.count('a'))
print("Existem {} letras 'a' na frase.".format(count1))
count2 = f.find('a')
print("A primeira letra 'a' é encontrada a primeira vez na {}° posição.".format(count2))
print("A última vez que a letra 'a' aparece é na posição {}.".format(f.rfind('a')))




