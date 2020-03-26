from global_variables import *
import pygame


#   In order to draw the cube, we'll have to create some depth. To do so,
#   the further Z is, the closer it will be from the center of the screen.
#   We take the size of the screen and divide it by z. We obtain the correct zoom.
#   Then multiply x and y by this value, add the center coordinate of the screen to 
#   centralize it and we are done.
#   For example :
#       let's have A (2, 2, 5) and B (2, 2, 10)
#       if we print them right away on the screen, we wont see B cause A is in front of it.
#       But if we had depth : 
#       For A : 
#           zoom = 800/5 
#           zoom = 160
#           A (360, 360)
#       For B :
#           zoom = 800/10
#           zoom = 80
#           B (160, 160)
#       So we now can see them on screen. B is the farest so it is the closer to the center.
#
#   But to actually see it on the screen, we'll have to stepback or we will be in the middle of the cube.
#   Simply add -5 to each point on Z to "push" the shape backward.
#   This way it seems like it is the camera that moved.

def draw_cube(screen, vertices, edges, camera = 0):
    for edge in edges:
        display_points = []
        for x, y, z in [vertices[edge[0]], vertices[edge[1]]]:
            z += 5
            focale = 800/abs(z)
            x , y = focale * x, focale * y 
            x += CENTER_X
            y += CENTER_Y
            display_points += [[x, y]]
        pygame.draw.line(screen, WHITE, display_points[0], display_points[1])