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
print(f"{cores['bold']}Calculadora de descontos{cores['reset']}")
print(f"{cores['magenta']}-=-{cores['reset']}" * 20)

valor_original = float(input('Informe o preço do produto: '))

print(f"{cores['magenta']}-=-{cores['reset']}" * 20)

print(f"{cores['azul']}Escolha a forma de pagamento:{cores['reset']}")

print("[ 1 ] Dinheiro/Cheque")
print("[ 2 ] À Vista no cartão")
print("[ 3 ] 2x no cartão")
print("[ 4 ] 3x ou mais no cartão")

forma_pagamento = int(input(f"{cores['bold']}Sua opção: {cores['reset']}"))

if forma_pagamento == 1:
    desconto = valor_original * 0.10
    valor_final = valor_original - desconto
    print(f"{cores['verde']}Valor com 10% de desconto: R$ {valor_final:.2f}{cores['reset']}")

elif forma_pagamento == 2:
    desconto = valor_original * 0.05
    valor_final = valor_original - desconto
    print(f"{cores['verde']}Valor com 5% de desconto: R$ {valor_final:.2f}{cores['reset']}")

elif forma_pagamento == 3:
    parcela = valor_original / 2
    print(f"{cores['azul']}2x de R$ {parcela:.2f} (Total: R$ {valor_original:.2f}){cores['reset']}")

elif forma_pagamento == 4:
    try:
        parcelas = int(input("Quantas parcelas? (3 ou mais): "))
        if parcelas < 3:
            print(f"{cores['vermelho']}Mínimo de 3 parcelas!{cores['reset']}")
            exit()
    except ValueError:
        print(f"{cores['vermelho']}Digite um número válido!{cores['reset']}")
        exit()
    
    juros = valor_original * 0.20
    valor_final = valor_original + juros
    parcela = valor_final / parcelas
    print(f"{cores['vermelho']}Valor com 20% de juros: R$ {valor_final:.2f}")
    print(f"{parcelas}x de R$ {parcela:.2f}{cores['reset']}")

else:
    print(f"{cores['vermelho']}Opção inválida! Escolha entre 1 e 4.{cores['reset']}")
