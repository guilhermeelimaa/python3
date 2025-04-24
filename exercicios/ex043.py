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

print(f"{cores['magenta']}-=-{cores['reset']}" * 20)
print(f"{cores['bg_branco']}Calculadora de IMC{cores['reset']}")
print(f"{cores['magenta']}-=-{cores['reset']}" * 20)

peso = float(input('Digite seu peso (kg): '))
altura = float(input('Digite sua altura (m): '))

imc = peso / (altura ** 2)  

print(f"{cores['azul']}Seu IMC é {imc:.2f}{cores['reset']}")

if imc < 18.5:
    print(f"{cores['ciano']}Você está ABAIXO DO PESO{cores['reset']}")
elif 18.5 <= imc <= 25:
    print(f"{cores['verde']}Você tem o PESO IDEAL{cores['reset']}")
elif 25 < imc <= 30:
    print(f"{cores['amarelo']}Você está com SOBREPESO{cores['reset']}")
elif 30 < imc <= 40:
    print(f"{cores['vermelho']}Você tem OBESIDADE{cores['reset']}")
else:
    print(f"{cores['vermelho']}Você tem OBESIDADE MÓRBIDA{cores['reset']}")