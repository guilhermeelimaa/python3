from random import randint
from time import sleep

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)

n = int(input('Digite um número entre 0 e 5: '))

if n < 0 or n > 5:
    print('Número inválido! Digite um valor entre 0 e 5.')

else:
    escolhido = randint(0, 5)

if escolhido == n:
    print('PROCESSANDO...')
    sleep(3)
    print('Você acertou! O número escolhido foi {}.' .format(escolhido))

else:
    print('PROCESSANDO...')
    sleep(2)
    print('Você perdeu! O número escolhido foi {}'.format(escolhido))