s = float(input('Digite o valor do salário para saber o aumento: R$'))
if s >= 1250.00:
    a = (s * 10) / 100
    s_final = s + a
    print('Seu salário receberá um aumento de {:.2f}, e será no valor de {:.2f}'.format(a, s_final))

else:
    a = (s * 15) / 100
    s_final = s + a
    print('Seu salário receberá um aumento de {:.2f}, e será no valor de {:.2f}'.format(a, s_final))