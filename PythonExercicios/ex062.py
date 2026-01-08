print("_________GERANDO P.A._________")
pt = int(input("Primeiro termo: "))
r = int(input("Razão: "))
t = int(input("Termos: "))
print(pt, end =" , ")
for c in range(0,t-1):
    pt=pt+r
    print(pt, end=" , ")
if t == 0:
    print("Fim.")
print("------> Fim da P.A.")
