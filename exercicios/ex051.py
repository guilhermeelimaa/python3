n = int(input("Digite o primeiro termo da PA: "))
r = int(input("Digite a razão da PA: "))

# Calcula e mostra os 10 primeiros termos
print("Os 10 primeiros termos da PA são:")
for i in range(10):
    t = n + i * r
    print(t, end="→" if i < 9 else "→")

print("FIM")