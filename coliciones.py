# !/usr/bin/env-python
# -*- coding: utf-8 -*-

import pygame

# -COLORES
negro    = ( 0   , 0   , 0   )
blanco   = ( 255 , 255 , 255 )
rojo     = ( 200 , 0   , 0   )
verde    = ( 0   , 200 , 00  )
azul     = ( 0   , 0   , 200 )
amarillo = ( 200 , 200 , 0   )

# -VENTANA
tamaño    = ancho,alto=300,300 # Tamaño de la pantalla
pantalla  = pygame.display.set_mode(tamaño) # Se cre una pantall con pygame con el tamaño prediseñado
pygame.display.set_caption("Coliciones") # Se le pone un nombre al borde de la pantalla

# -DATOS DE  LOS CUBOS
tam_cubo    = 25
lado_x      = (ancho/2)-75
lado_y      = (alto/2)
lado_x_2    = (ancho/2)+50
lado_y_2    = (alto/2)
velocidad   = 0


# -BUCLÉ 
while True:
    for accion in pygame.event.get():
        # Si se presiona el boton 'X' salimos
        if accion.type == pygame.QUIT:
            quit()
        if accion.type    == pygame.KEYDOWN:
            # Si presionamos la tecla 'c'
            if accion.key == pygame.K_c:
               velocidad = 10


    # Para que tenga efecto la velocidad en los cubos
    lado_x   += velocidad
    lado_x_2 -= velocidad

    lado_cubo_1 = lado_x   + tam_cubo 
    lado_cubo_2 = lado_x_2  

    # Muestra la pantalla con fondo de color
    pantalla.fill(blanco)

    # Impresión de los cubos
    cubo_1 = pygame.draw.rect ( pantalla , negro , ( lado_x   , lado_y   , tam_cubo , tam_cubo ) )
    cubo_2 = pygame.draw.rect ( pantalla , rojo  , ( lado_x_2 , lado_y_2 , tam_cubo , tam_cubo ) )
    
    """ Condición para evitar que los objetos salgan de pantalla"""
    # Si el cubo va de izquierda a derecha
    if lado_cubo_1 >= ancho:
        lado_x = 0

    if lado_x <= 0:
        lado_x = 0
        velocidad *= -1

    # Si el cubo va de derecha a izquierda
    if lado_x_2 <= 0:
        lado_x_2 = 275 

    if lado_cubo_2 >= ancho:
        lado_x_2 = 275 
        velocidad *= -1

    # Condición de colisión
    if cubo_1.colliderect(cubo_2):
        velocidad *=-1

    # Manejo de la pantalla
    pygame.display.update()
    # Actualización de la pantalla
    pygame.time.delay(30)
