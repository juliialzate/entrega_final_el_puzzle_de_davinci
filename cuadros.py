import pygame
from info import *


pygame.init()

#La clase cuadro en su funcion crear_imagen me permite convertir las imagenes a usar a una image  con sus caracteristicas de surface
class Cuadro:

    def crear_imagen(self,imagen):
        self.image = imagen
    
    
        
#Aquí aplico la funcion anterior para convertir todas las imagenes a las características de surface
mona1 = Cuadro()
mona1.crear_imagen(imagen1)

mona2 = Cuadro()
mona2.crear_imagen(imagen2)

mona3 = Cuadro()
mona3.crear_imagen(imagen3)

mona4 = Cuadro()
mona4.crear_imagen(imagen4)

mona5 = Cuadro()
mona5.crear_imagen(imagen5)

mona6 = Cuadro()
mona6.crear_imagen(imagen6)

mona7 = Cuadro()
mona7.crear_imagen(imagen7)

mona8 = Cuadro()
mona8.crear_imagen(imagen8)

mona9 = Cuadro()
mona9.crear_imagen(imagen9)

#Aquí establezco una posicion de matriz a cada imagen, el orden corresponde al orden correcto del puzzle 
class Matricez():

    def __init__ (self):
        self.celda = celda 
    
    def completar_matriz(self):

        matriz_principal[0][0] = mona1
        matriz_principal[0][1] = mona2
        matriz_principal[0][2] = mona3
        matriz_principal[1][0] = mona4
        matriz_principal[1][1] = mona5
        matriz_principal[1][2] = mona6
        matriz_principal[2][0] = mona7
        matriz_principal[2][1] = mona8
        matriz_principal[2][2] = mona9

        matriz_correcta[0][0] = mona1
        matriz_correcta[0][1] = mona2
        matriz_correcta[0][2] = mona3
        matriz_correcta[1][0] = mona4
        matriz_correcta[1][1] = mona5
        matriz_correcta[1][2] = mona6
        matriz_correcta[2][0] = mona7
        matriz_correcta[2][1] = mona8
        matriz_correcta[2][2] = mona9
    
    #Gracias a establecer coordenadas y recorrer la matriz con dos ciclos for "blit" imprime las imagenes convertidas anteriormente a surface
    def imprimir_matriz(self): 
        coor_x = (pantalla[0] - (len(matriz_principal[0]) * self.celda[0])) //2
        coor_y = (pantalla[1] - (len(matriz_principal) * self.celda[1])) //2

        for i in range(len(matriz_principal)):
            for j in range(len(matriz_principal[i])):
                screen.blit(matriz_principal[i][j].image, (coor_x + j * self.celda[0], coor_y + i * self.celda[1]))

#Esta clase contiene la logica de movimiento en donde cada imagen se mueve al sumar o restar una posicion de matriz 
class Teclas(Cuadro):

    def __init__ (self):
        self.verificar_right = False
        self.verificar_left = False
        self.verificar_up = False
        self.verificar_down = False
    
    def mover_celdas(self):
        
        key = pygame.key.get_pressed()
        
        
        

        if key[pygame.K_RIGHT] and not self.verificar_right:
            self.verificar_right = True
            for i in range(len(matriz_principal)):
                for j in range (len(matriz_principal[i])):
                    if matriz_principal[i][j].image == imagen9 and j != 0: #encuentro donde esta la imagen en blanco llamada "imagen 9"
                        movimiento = matriz_principal [i][j-1] #se define una posicion
                        matriz_principal[i][j-1] = matriz_principal[i][j] #se actualiza la posicion
                        matriz_principal[i][j] = movimiento #se mueve
                        #matriz_principal[i][j-1] = imagen9 
        
        if not key[pygame.K_RIGHT]:
            self.verificar_right = False 
        
        if key[pygame.K_LEFT] and not self.verificar_left:
            self.verificar_left = True
            for i in range (len(matriz_principal)):
                for j in range (len(matriz_principal[i])):
                    if matriz_principal[i][j].image == imagen9 and j != 2: #encuentro donde esta la imagen en blanco llamada "imagen 9"
                        movimiento = matriz_principal[i][j+1] #se define una posicion
                        matriz_principal[i][j+1] = matriz_principal[i][j] #se actualiza la posicion
                        matriz_principal [i][j] = movimiento #se mueve
                        #en un momento del cilo en vez de sumar una fila suma dos, la variable un_movimiento permite actualizar el true para que se sume una fila
                        un_movimiento = True
                        if un_movimiento == True:
                            return un_movimiento



        if not key[pygame.K_LEFT]:
            self.verificar_left = False

    
        if key[pygame.K_DOWN] and not self.verificar_down:
            self.verificar_down = True
            for i in range (len(matriz_principal)):
                for j in range (len(matriz_principal[i])):
                    if matriz_principal[i][j].image == imagen9 and i != 0: #encuentro donde esta la imagen en blanco llamada "imagen 9"
                        movimiento = matriz_principal[i-1][j] #se define una posicion
                        matriz_principal[i-1][j] = matriz_principal[i][j]  #se actualiza la posicion
                        matriz_principal [i][j] = movimiento #se mueve
        
        if not key[pygame.K_DOWN]:
            self.verificar_down = False

        if key[pygame.K_UP] and not self.verificar_up:
            self.verificar_up = True
            for i in range (len(matriz_principal)):
                for j in range (len(matriz_principal[i])):
                    if matriz_principal[i][j].image == imagen9 and i != 2: #encuentro donde esta la imagen en blanco llamada "imagen 9"
                        movimiento = matriz_principal[i+1][j] #se define una posicion
                        matriz_principal[i+1][j] = matriz_principal[i][j] #se actualiza la posicion
                        matriz_principal [i][j] = movimiento #se mueve
                        #en un momento del cilo en vez de sumar una fila suma dos, la variable un_movimiento permite actualizar el true para que se sume una fila
                        un_movimiento = True
                        if un_movimiento == True:
                            return un_movimiento
        
        if not key[pygame.K_UP]:
            self.verificar_up = False


