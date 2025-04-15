km = float(input('Digite a distância da viagem em KM: '))
if km < 200:
    v = km * 0.50
    print('O valor da passagem será de R${:.2f}'.format(v))
else:
    v = km * 0.45
    print('O valor da passagem será de R${:.2f}'.format(v))