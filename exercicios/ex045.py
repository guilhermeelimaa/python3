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

# Exercicio 045 - Jogando Pedra, Papel e Tesoura
# Importando bibliotecas
import time
from random import choice

# Definindo as opções do jogo
opcoes = ('Pedra', 'Papel', 'Tesoura')

# Imprimindo o cabeçalho
print(f"{cores['azul']}{cores['bold']}JOKENPÔ{cores['reset']}")
print(f"{cores['azul']}-=-{cores['reset']}" * 20)

# Imprimindo as opções
print(f"{cores['azul']}{cores['bold']}Suas opções:{cores['reset']}")
print(f"{cores['azul']}{cores['bold']}[ 0 ] Pedra{cores['reset']}")
print(f"{cores['azul']}{cores['bold']}[ 1 ] Papel{cores['reset']}")
print(f"{cores['azul']}{cores['bold']}[ 2 ] Tesoura{cores['reset']}")

# Lendo a opção do usuário
while True:
    try:
        jogador = int(input(f"{cores['azul']}{cores['bold']}Qual é a sua jogada?{cores['reset']} "))
        if jogador < 0 or jogador > 2:
            raise ValueError
        break
    except ValueError:
        print(f"{cores['vermelho']}{cores['bold']}Opção inválida!{cores['reset']}")

print(f"{cores['amarelo']}Carregando....{cores['reset']}")
time.sleep(2) # Atraso de 2 segundos


# Imprimindo a opção do jogador
print(f"{cores['azul']}{cores['bold']}Você jogou {opcoes[jogador]}!{cores['reset']}")
# Imprimindo a opção do computador
computador = choice(opcoes)
print(f"{cores['azul']}{cores['bold']}O computador jogou {computador}!{cores['reset']}")

# Verificando quem ganhou
if jogador == 0 and computador == 'Tesoura':
    print(f"{cores['verde']}{cores['bold']}Você venceu!{cores['reset']}")
elif jogador == 1 and computador == 'Pedra':
    print(f"{cores['verde']}{cores['bold']}Você venceu!{cores['reset']}")
elif jogador == 2 and computador == 'Papel':
    print(f"{cores['verde']}{cores['bold']}Você venceu!{cores['reset']}")
elif jogador == 0 and computador == 'Papel':
    print(f"{cores['vermelho']}{cores['bold']}Você perdeu!{cores['reset']}")
elif jogador == 1 and computador == 'Tesoura':
    print(f"{cores['vermelho']}{cores['bold']}Você perdeu!{cores['reset']}")
elif jogador == 2 and computador == 'Pedra':
    print(f"{cores['vermelho']}{cores['bold']}Você perdeu!{cores['reset']}")
elif jogador == computador:
    print(f"{cores['amarelo']}{cores['bold']}Empate!{cores['reset']}")
else:
    print(f"{cores['vermelho']}{cores['bold']}Opção inválida!{cores['reset']}")

# Fim do jogo
print(f"{cores['azul']}-=-{cores['reset']}" * 20)