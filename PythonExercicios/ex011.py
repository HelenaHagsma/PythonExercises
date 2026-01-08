l = float(input("Digite a largura da sua parede: "))
a = float(input("Digite a altura da sua parede: "))
area = l*a
print("A área da sua parede é: {} metros quadrados,\ne a quantidade de tinta que será usada para pintá-la é: {:.0f} litros.".format(area, area/2))