import math
oposto = float(input("Digite o comprimento do cateto oposto: "))
adjacente = float(input("Digite o comprimento do cateto adjacente:"))
hipotenusa = math.sqrt(oposto ** 2 + adjacente ** 2)
print("A hipotenusa é {:.2f}".format(hipotenusa))