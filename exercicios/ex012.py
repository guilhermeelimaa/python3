print('===Calculadora de descontos===')
preco = float(input('Digite o preço do produto:'))
desconto = 0.05
preco_final = preco * (1 - desconto)
print('Preço original: R${:.2f}'.format(preco))
print('Preço com 5% de desconto: R${:.2f}'.format(preco_final))