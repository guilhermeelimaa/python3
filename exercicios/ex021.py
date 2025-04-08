import pygame
pygame.init()
try:
    pygame.mixer.music.load('exercicios/ex021.mp3')  # Carrega o arquivo de áudio
    pygame.mixer.music.play()  # Inicia a reprodução do arquivo de áudio
    while pygame.mixer.music.get_busy():  # Aguarda enquanto o áudio está sendo reproduzido
        pass
except pygame.error as e:
    print(f"Erro ao reproduzir o áudio: {e}")  # mostra impressão de um erro se o áudio não puder ser reproduzido