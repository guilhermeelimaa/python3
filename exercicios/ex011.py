altura = float(input('Digite a altura da parede em metros:'))
largura = float(input('Digite a largura da parede em metros:'))
area = largura * altura
tinta = area / 2
print('Área total: {:.1f}m²'.format(area))
print('Tinta necessária {:.1f} litros'.format(tinta))