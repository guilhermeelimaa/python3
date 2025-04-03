salario = float(input('Digite o salário:'))
aumento = 0.15
novo_salario = salario * (1 + aumento)
print('Salário atual: R${:.2f}'.format(salario))
print('Novo salário com aumento de 15%: R${:.2f}'.format(novo_salario))