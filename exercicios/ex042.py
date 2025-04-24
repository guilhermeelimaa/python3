# Dicionário de cores (ANSI escape codes)
cores = {
    # Style
    'reset': '\033[m',  
    'bold': '\033[1m',         
    'underline': '\033[4m',    
    'negative': '\033[7m',      
    
    # Cores de TEXTO (TEXT)
    'branco': '\033[30m',
    'vermelho': '\033[31m',
    'verde': '\033[32m',
    'amarelo': '\033[33m',
    'azul': '\033[34m',
    'magenta': '\033[35m',
    'ciano': '\033[36m',
    'cinza': '\033[37m',
    
    # Cores de FUNDO (BACK)
    'bg_branco': '\033[40m',
    'bg_vermelho': '\033[41m',
    'bg_verde': '\033[42m',
    'bg_amarelo': '\033[43m',
    'bg_azul': '\033[44m',
    'bg_magenta': '\033[45m',
    'bg_ciano': '\033[46m',
    'bg_cinza': '\033[47m'
}

print(f'{cores['magenta']}-=-{cores['reset']}' * 20)
print(f'{cores['bg_branco']}Analisador de triângulos{cores['reset']}')
print(f'{cores['magenta']}-=-{cores['reset']}' * 20)

s1 = float(input('Digite o valor de um segmento: '))
s2 = float(input('Digite o valor de um segmento: '))
s3 = float(input('Digite o valor de um segmento: '))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print(f'{cores['verde']}Os segmentos acima PODEM FORMAR triângulos!{cores['reset']}')

    # Verificando o tipo de triângulo
    if s1 == s2 == s3:
        print(f'{cores['azul']}Tipo: Equilátero (todos os lados iguais){cores['reset']}')

    elif s1 == s2 or s1 == s3 or s2 == s3:
        print(f'{cores['amarelo']}Tipo: Isósceles (dois lados iguais){cores['reset']}')
    else:
        print(f'{cores['ciano']}Tipo: Escaleno (todos os lados diferentes){cores['reset']}')
else:
    print(f'{cores['vermelho']}Os segmentos acima NÃO PODEM FORMAR triângulos!{cores['reset']}')