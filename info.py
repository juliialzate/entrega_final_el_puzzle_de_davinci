import pygame

# Aquí se encuentran las dimensiones de la panatalla y de cada celda, en total son 9 al ser una matriz 3x3
pantalla = 639, 813
celda = 213, 270

# Defino los colores que se usaran en el fondo de la pantalla
blanco = (255, 255, 255)
negro = (0, 0, 0)


#La matriz principal inicia las posiciones de las 9 imagenes que utilizo en cuadros.py
matriz_principal= [
    [None, None, None],
    [None, None, None],
    [None, None, None]
]

#La matriz_correcta sirve para comparar con la matriz_principal y rectificar si el jugador gano el juego
matriz_correcta= [
    [None, None, None],
    [None, None, None],
    [None, None, None]
]

# Cargo todas las imagenes que voy a utilizar
imagen1 = pygame.image.load("imagenes/monalisa1.png")
imagen2 = pygame.image.load("imagenes/monalisa2.png")
imagen3 = pygame.image.load("imagenes/monalisa3.png")
imagen4 = pygame.image.load("imagenes/monalisa4.png")
imagen5 = pygame.image.load("imagenes/monalisa5.png")
imagen6 = pygame.image.load("imagenes/monalisa6.png")
imagen7 = pygame.image.load("imagenes/monalisa7.png")
imagen8 = pygame.image.load("imagenes/monalisa8.png")
imagen9 = pygame.image.load("imagenes/monalisa9.png")


# Creo y nombro la pantalla
screen = pygame.display.set_mode(pantalla)
pygame.display.set_caption("EL puzzle de davinci")

# Aquí dibujo la matriz
def dibujar_matriz():
    for x in range(0, pantalla[0], celda[0]):
        pygame.draw.line(screen, negro, (x, 0), (x, pantalla[1]))
    for y in range(0, pantalla[1], celda[1]):
        pygame.draw.line(screen, negro, (0, y), (pantalla[0], y))