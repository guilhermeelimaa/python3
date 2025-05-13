n = int(input('Digite um número para saber sua tabuada: '))

print('========Tabuada do {}========'.format(n))
for c in range(1, 11):  
    print('{} x {} = {}'.format(n, c, n * c))