nome = input("Digite seu nome completo: ")
print(nome.upper())
print(nome.lower())

countt = int(nome.count(' '))
len2 = int(len(nome))
subb = int(len2) - int(countt)
print(subb)

split = nome.split()
splitt = split[0] [0:]
print(len(splitt))