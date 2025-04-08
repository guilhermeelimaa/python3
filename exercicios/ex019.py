import random
print("=======SORTEIO PARA APAGAR O QUADRO=======")
a1 = str(input("Primeiro aluno: "))
a2 = str(input("Segundo aluno: "))
a3 = str(input("Teceiro aluno: "))
a4 = str(input("Quarto aluno: "))
lista = [a1, a2, a3, a4]
escolhido = random.choice(lista)
print("O Aluno escolhido foi {}".format(escolhido))
