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

# Solicita o número e a base de conversão
numero = int(input("Digite um número inteiro: "))
print(f"{cores['azul']}Escolha a base de conversão:{cores['reset']}")
print("[ 1 ] Binário")
print("[ 2 ] Octal")
print("[ 3 ] Hexadecimal")

opcao = int(input(f"{cores['bold']}Sua opção: {cores['reset']}"))

# Converte o número conforme a opção
if opcao == 1:
    resultado = bin(numero)[2:]  # Remove o '0b' do início
    print(f"{cores['verde']}Binário: {resultado}{cores['reset']}")
elif opcao == 2:
    resultado = oct(numero)[2:]  # Remove o '0o' do início
    print(f"{cores['verde']}Octal: {resultado}{cores['reset']}")
elif opcao == 3:
    resultado = hex(numero)[2:]  # Remove o '0x' do início
    print(f"{cores['verde']}Hexadecimal: {resultado}{cores['reset']}")
else:
    print(f"{cores['vermelho']}Opção inválida!{cores['reset']}")
