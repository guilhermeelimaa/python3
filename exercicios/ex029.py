v = int(input('Digite a velocidade do veículo: '))
if v <= 80:
    print('O veículo está dentro do limite permitido de velocidade!')
else:
    m = (v - 80) * 7
    print('Você foi multado no valor de R${}'.format(m))