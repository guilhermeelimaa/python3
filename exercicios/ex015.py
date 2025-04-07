dia = int(input("Quantos dias o carro foi alugado: "))
km = float(input("Quantos KM foram percorridos: "))
d = 60 * dia
k = 0.15 * km
t = d + k
print("O valor total a pagar é de R${}".format(t))
