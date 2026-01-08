f = input("Digite uma frase: ").strip().upper()
palavras = f.split()
junto = ''.join(palavras)
inverso=''
for letra in range(len(junto) -1, -1, -1):
    inverso = inverso + junto[letra]
if inverso == junto:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")