import pygame
import os
import time

pygame.init()
ON = True

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

width = 800
height = 800

center_X = width/2
center_Y = height/2
center_Z = height/2
screen = pygame.display.set_mode((width,height))

vertices = [[-1,-1,-1],[1,-1,-1],[1,1,-1],[-1,1,-1],[-1,-1,-1],[1,-1,-1],[1,1,-1],[-1,1,-1]]

zoom = 50

zoomed_vertices = []

for vertice in vertices:
    zoomed_vertices += [[center_X + vertice[0] * zoom, center_Y + vertice[1] * zoom, center_Z + vertice[2] * zoom]]

print(zoomed_vertices)

while(ON):
    key = pygame.key.get_pressed()
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            ON = False
        elif key[pygame.K_ESCAPE]:
            ON = False
    pygame.draw.lines(screen, WHITE, True,zoomed_vertices)
    pygame.display.flip()

pygame.quit()