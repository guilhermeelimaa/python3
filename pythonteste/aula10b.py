n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
if m >= 6:
    print('Sua média foi {:.2f} \nVocê foi aprovado!'.format(m))
else:
    print('Sua Média foi {:.2f} \nVocê foi reprovado!'.format(m))