from datetime import date

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


nascimento = int(input(f'{cores['bold']}Digite o ano que você nasceu: '))

ano = date.today().year
idade = ano - nascimento

if idade < 18:
    print(f'{cores['verde']}Você tem {idade} anos, ainda não precisa se alistar.{cores['reset']}')

elif idade == 18:
    print(f'{cores['amarelo']}Você tem {idade} anos, você precisa se alistar.{cores['reset']}')

elif idade > 18:
    print(f'{cores['vermelho']}Você tem {idade} anos, já passou do tempo do alistamento.{cores['reset']}')


