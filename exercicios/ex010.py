print('===Conversor de real para dólar===')
real = float(input('Digite quantos R$ você tem na sua carteira:'))
dolar = 5.61
r = real / dolar
print('Você pode comprar US${:.2f} dólares'.format(r))