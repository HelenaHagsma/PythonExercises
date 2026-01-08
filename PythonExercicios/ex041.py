a = int(input("Informe seu ano de nascimento: "))
idade = 2025 - a
if idade <=9:
    print("CATEGORIA MIRIM.")
elif idade >9 and idade <=14:
    print("CATEGORIA INFANTIL.")
elif idade > 14 and idade <=19:
    print("CATEGORIA JUNIOR.")
elif idade >19 and idade <=20:
    print("CATEGORIA SENIOR.")
else:
    print("CATEGORIA MASTER.")