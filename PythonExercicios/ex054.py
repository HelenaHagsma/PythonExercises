s = 0
s2 = 0
for i in range(1,8):
    a = int(input("Digite seu ano de nascimento: "))
    idade = 2025 - a
    if idade<18:
        s = s + 1
    else:
         s2 = s2 + 1
print("{} ainda não atingiram a maioridade.".format(s))
print("{} já atingiram a maioridade.".format(s2))






