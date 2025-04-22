nome = str(input('Qual é seu nome: '))

if nome == 'Gustavo':
    print('Que nome bonito!')

elif nome == 'João' or nome == 'Maria':
    print('Seu nome é bem popular no Brasil.')

elif nome in 'Ana Mariana Bia':
    print('Belo nome feminino')

else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))
