"""draw a fractal tree"""

import os
import pygame
import sys
import math

SIZE = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

iterations = 4
length = int(SIZE*0.2)

pygame.init()
screen = pygame.display.set_mode((SIZE, SIZE))
pygame.display.set_caption('Fractal Snowflake')
screen.fill(WHITE)

def tree(iterations, color, x, y, length, start_angle, theta):
    """draw the tree"""
    if iterations == 0:
        xn = x+length*0.4*math.cos(start_angle)
        yn = y-length*0.4*math.sin(start_angle)
        pygame.draw.line(screen, color, (xn, yn), (xn, yn), 4)
    else:
        #bottom left
        new_angle01 = start_angle+3.5*theta
        x01 = length*0.4*math.cos(new_angle01)
        y01 = length*0.4*math.sin(new_angle01)
        pygame.draw.line(screen, color, (x, y), (x+x01, y-y01), iterations*6)
        tree(iterations-1, color, x+x01, y-y01, int(length*0.5), new_angle01-1.2*theta, theta)
        #bottom right
        new_angle02 = start_angle-3.5*theta
        x02 = length*0.4*math.cos(new_angle02)
        y02 = length*0.4*math.sin(new_angle02)
        pygame.draw.line(screen, color, (x, y), (x+x02, y-y02), iterations*6)
        tree(iterations-1, color, x+x02, y-y02, int(length*0.5), new_angle02+1.2*theta, theta)
        #top left
        new_angle11 = start_angle+theta
        x11 = x+length*0.6*math.cos(new_angle11)
        y11 = y-length*0.6*math.sin(new_angle11)
        pygame.draw.line(screen, color, (x, y), (x11, y11), iterations*8)
        new_angle21 = new_angle11+theta
        x21 = x11+length*0.6*math.cos(new_angle21)
        y21 = y11-length*0.6*math.sin(new_angle21)
        pygame.draw.line(screen, color, (x11, y11), (x21, y21), iterations*8)
        tree(iterations-1, color, x21, y21, int(length*0.7), new_angle21-1.2*theta, theta)
        #top right
        new_angle12 = start_angle-theta
        x12 = x+length*0.6*math.cos(new_angle12)
        y12 = y-length*0.6*math.sin(new_angle12)
        pygame.draw.line(screen, color, (x, y), (x12, y12), iterations*8)
        new_angle22 = new_angle12-theta
        x22 = x12+length*0.6*math.cos(new_angle22)
        y22 = y12-length*0.6*math.sin(new_angle22)
        pygame.draw.line(screen, color, (x12, y12), (x22, y22), iterations*8)
        tree(iterations-1, color, x22, y22, int(length*0.7), new_angle22+1.2*theta, theta)

def main():
    """execute tree drawing"""
    pygame.draw.line(screen, BLACK, (int(SIZE*0.5), int(SIZE*0.9)), (int(SIZE*0.5), int(SIZE*0.8)), iterations)
    tree(iterations, BLACK, int(SIZE*0.5), int(SIZE*0.805), length, math.pi/2, math.pi/10)
    pygame.display.update()
    name = os.path.join(os.path.dirname(__file__), "Fractal Tree.png")
    pygame.image.save(screen, name)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

if __name__ == '__main__':
    main()
