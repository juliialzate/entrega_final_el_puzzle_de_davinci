import pygame
import sys
from info import *
from cuadros import *
import random

pygame.init()


#Aqui nombro variables y las igualo a las clases trabajadas en cuadros.py para poder llamar sus métodos correctamente dentro del bucle principal
mostrar = Matricez()
mostrar.completar_matriz()
juliana = Teclas()



def principal():

    random.shuffle(matriz_principal)
    for i in matriz_principal:
        random.shuffle(i)


    running = True
    
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if running:
            mostrar.imprimir_matriz()
            juliana.mover_celdas()

            if matriz_principal == matriz_correcta:
                    fuente = pygame.font.SysFont("Helvetica", 36)
                    text = fuente.render("Ganaste, resolviste el puzzle de Davinci", True, (255, 255, 255))
                    text_rect = text.get_rect(center=(pantalla[0]//2, pantalla[1]//2))
                    screen.blit(text, text_rect)

            pygame.display.flip()

        

principal()


