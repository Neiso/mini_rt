import pygame
from global_variables import *
from function import *

pygame.init()

screen = pygame.display.set_mode((WIDTH,HEIGHT), pygame.HWSURFACE) # pygame.HWSURFACE uses graphical card to render

while(ON):
    key = pygame.key.get_pressed()
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            ON = False
        elif key[pygame.K_ESCAPE]:
            ON = False
    
    draw_cube(screen, cube_vertices, cube_edges)
    pygame.display.flip()

pygame.quit()