s = 0
for c in range(3, 501, 3):  
    if c % 2 != 0:  # Verifica se é ímpar
        s += c
print('A soma dos números ímpares múltiplos de 3 entre 1 e 500 é: {}'.format(s))