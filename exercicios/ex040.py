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

n1 = float(input(f"{cores['bold']}Digite a primeira nota: {cores['reset']}"))
n2 = float(input(f"{cores['bold']}Digite a segunda nota: {cores['reset']}"))

media = (n1 + n2) / 2

if media < 5:
    print(f"{cores['vermelho']}Você foi REPROVADO, sua média é {media} {cores['reset']}")
elif 5 <= media <= 6.9:  
    print(f"{cores['amarelo']}Você está de RECUPERAÇÃO, sua média é {media} {cores['reset']}")
elif media >= 7:
    print(f"{cores['verde']}PARABÉNS! Você foi APROVADO, sua média é {media} {cores['reset']}")