# Dicionário de cores (ANSI escape codes)
cores = {
    # Style
    'limpa': '\033[m',  
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

# Solicita os dados do usuário
print(f"{cores['azul']}===== SIMULADOR DE EMPRÉSTIMO BANCÁRIO ====={cores['limpa']}")
valor_casa = float(input(f"{cores['amarelo']}Digite o valor da casa: R$ {cores['limpa']}"))
salario = float(input(f"{cores['amarelo']}Digite o salário do comprador: R$ {cores['limpa']}"))
anos = int(input(f"{cores['amarelo']}Em quantos anos deseja pagar? {cores['limpa']}"))

# Calcula a prestação mensal
meses = anos * 12
prestacao = valor_casa / meses

# Verifica se a prestação excede 30% do salário
limite = salario * 0.30

if prestacao <= limite:
    print(f"\n{cores['verde']}{cores['bold']}Empréstimo APROVADO!{cores['limpa']}")
    print(f"Prestação mensal: {cores['verde']}R$ {prestacao:.2f}{cores['limpa']}")
else:
    print(f"\n{cores['vermelho']}{cores['bold']}Empréstimo NEGADO!{cores['limpa']}")
    print(f"A prestação de {cores['vermelho']}R$ {prestacao:.2f}{cores['limpa']} excede 30% do salário.")