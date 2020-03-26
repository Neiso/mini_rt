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

connected_points = [
                    [0,1],
                    [1,2],
                    [2,3],
                    [3,0],
                    [4,5],
                    [5,6],
                    [6,7],
                    [7,4],
                    [0,4],
                    [1,5], 
                    [2,6],
                    [3,7]
                    ]

vertices = [(-1,-1,-1),(1,-1,-1),(1,1,-1),(-1,1,-1),(-1,-1,1),(1,-1,1),(1,1,1),(-1,1,1)]

zoom = 50

for connected_point in connected_points:
    modified_points = []
    for x, y, z in [vertices[connected_point[0]], vertices[connected_point[1]]]:
        z -= 5
        focale = 400/abs(z)
        x , y = focale * x, focale * y 
        x += center_X
        y += center_Y
        modified_points += [[x, y]]
    pygame.draw.line(screen, WHITE, modified_points[0], modified_points[1])

print(modified_points)

while(ON):
    key = pygame.key.get_pressed()
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            ON = False
        elif key[pygame.K_ESCAPE]:
            ON = False
    
    pygame.display.flip()

pygame.quit()