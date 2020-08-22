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
lado_x    = (ancho/2)-60
lado_y    = (alto/2)
tam_cubo  = 25
lado_x_2  = (ancho/2)+50
lado_y_2  = (alto/2)
velocidad = 0

# -BUCLÉ 
while True:
    for accion in pygame.event.get():
        if accion.type==pygame.QUIT:
            quit()
        if accion.type==pygame.KEYDOWN:
            if accion.key == pygame.K_c:
               velocidad = 30

    # Para que tenga efecto la velocidad en los cubos
    lado_x   += velocidad
    lado_x_2 -= velocidad

    pantalla.fill(blanco)
    # Impresión de los cubos
    cubo_1 = pygame.draw.rect ( pantalla , negro , ( lado_x   , lado_y   , tam_cubo , tam_cubo ) )
    cubo_2 = pygame.draw.rect ( pantalla , rojo  , ( lado_x_2 , lado_y_2 , tam_cubo , tam_cubo ) )
    pygame.display.update()
    pygame.time.delay(30)
