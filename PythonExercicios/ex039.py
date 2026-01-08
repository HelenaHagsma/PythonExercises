a = int(input("Digite seu ano de nascimento: "))
idade = 2025 - a
if idade < 18:
    print("Você ainda irá se alistar. Falta {} ano(s).".format(18-idade))
elif idade==18:
    print("Você pode se alistar!")
else:
    print("Seu prazo para alistamento passou. Passaram {} ano(s).".format(idade-18))