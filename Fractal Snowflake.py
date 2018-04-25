"""make a koch snowflake"""

import sys
import os
import math
import itertools
import pygame

import time

SIZE = 600

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
MAGENTA	= (255, 0, 255)
CYAN = (0, 255, 255)

pygame.init()
screen = pygame.display.set_mode((SIZE, SIZE))
pygame.display.set_caption('Fractal Snowflake')
screen.fill(WHITE)

def triangley(a, e):
    """returns the 3 points of the triangle between a and e"""
    dist = math.sqrt((e[0]-a[0])**2+(e[1]-a[1])**2)/3 #length of the line
    theta = math.atan2(e[1]-a[1], e[0]-a[0]) #angle of the line
    b = (a[0]+(e[0]-a[0])/3, a[1]+(e[1]-a[1])/3)
    c = (b[0]+dist*math.cos(math.pi/3+theta), b[1]+dist*math.sin(math.pi/3+theta))
    d = (a[0]+(e[0]-a[0])*2/3, a[1]+(e[1]-a[1])*2/3)
    pointlist = [a, b, c, d]
    return pointlist

def pointy(order, a, e):
    """creates the pointlist"""
    pointlist = []
    pointlist.extend(triangley(a, e))
    for _ in itertools.repeat(None, order):
        newlist = []
        for y in range(0, len(pointlist)):
            if y == (len(pointlist)-1):
                newlist.extend(triangley(pointlist[y], e))
            else:
                newlist.extend(triangley(pointlist[y], pointlist[y+1]))
        pointlist = newlist
    return pointlist

def snowy(order, centerx, centery, radius, color, thickness):
    """create the snow fractal"""
    start = [] #create the starting points used for all others
    start.append((centerx, centery+radius))
    start.append((centerx+math.sqrt(3)*radius*0.5, centery-radius*0.5))
    start.append((centerx-math.sqrt(3)*radius*0.5, centery-radius*0.5))

    pointlist = [] #create full list of points
    pointlist.extend(pointy(order, start[0], start[1]))
    pointlist.extend(pointy(order, start[1], start[2]))
    pointlist.extend(pointy(order, start[2], start[0]))
    pygame.draw.lines(screen, color, True, pointlist, thickness) #plot the points

def floodfill(image, x, y, color):
    """paint bucket tool"""
    base = image.get_at((x, y))
    image.set_at((x, y), color)
    bucket = [(x, y)]
    while bucket:
        (a, b) = bucket[0]
        del bucket[0]
        if a != 0 or a != size-1 or b != 0 or b != size-1:
            if image.get_at((a+1, b)) == base:
                image.set_at((a+1, b), color)
                bucket.append((a+1, b))
            if image.get_at((a-1, b)) == base:
                image.set_at((a-1, b), color)
                bucket.append((a-1, b))
            if image.get_at((a, b+1)) == base:
                image.set_at((a, b+1), color)
                bucket.append((a, b+1))
            if image.get_at((a, b-1)) == base:
                image.set_at((a, b-1), color)
                bucket.append((a, b-1))

def drawing(order):
    """draw lots of flakes"""
    snowy(order, SIZE*0.5, SIZE*0.5, SIZE*0.15, BLACK, 1)
    snowy(order, SIZE*0.5, SIZE*0.8, SIZE*0.15, BLACK, 1)
    snowy(order, SIZE*0.5, SIZE*0.2, SIZE*0.15, BLACK, 1)
    snowy(order, int(SIZE*(0.5+0.3*math.cos(math.pi/6))), int(SIZE*(0.5+0.3*math.sin(math.pi/6))), int(SIZE*0.15), BLACK, 1)
    snowy(order, int(SIZE*(0.5+0.3*math.cos(math.pi/6))), int(SIZE*(0.5-0.3*math.sin(math.pi/6))), int(SIZE*0.15), BLACK, 1)
    snowy(order, int(SIZE*(0.5-0.3*math.cos(math.pi/6))), int(SIZE*(0.5+0.3*math.sin(math.pi/6))), int(SIZE*0.15), BLACK, 1)
    snowy(order, int(SIZE*(0.5-0.3*math.cos(math.pi/6))), int(SIZE*(0.5-0.3*math.sin(math.pi/6))), int(SIZE*0.15), BLACK, 1)

def coloring():
    """color the different snowflakes"""
    floodfill(screen, int(SIZE*0.5), int(SIZE*0.2), RED)
    floodfill(screen, int(SIZE*(0.5-0.3*math.cos(math.pi/6))), int(SIZE*(0.5+0.3*math.sin(math.pi/6))), GREEN)
    floodfill(screen, int(SIZE*(0.5+0.3*math.cos(math.pi/6))), int(SIZE*(0.5+0.3*math.sin(math.pi/6))), BLUE)
    floodfill(screen, int(SIZE*(0.5-0.3*math.cos(math.pi/6))), int(SIZE*(0.5-0.3*math.sin(math.pi/6))), YELLOW)
    floodfill(screen, int(SIZE*(0.5+0.3*math.cos(math.pi/6))), int(SIZE*(0.5-0.3*math.sin(math.pi/6))), MAGENTA)
    floodfill(screen, int(SIZE*0.5), int(SIZE*0.8), CYAN)
    floodfill(screen, int(SIZE*0.5), int(SIZE*0.5), BLACK)

def main():
    """create the artwork"""
    #snowy(5, SIZE*0.5, SIZE*0.5, SIZE*0.45, BLACK, 2)
    drawing(3)
    coloring()
    #floodfill(screen, int(SIZE*0.5), int(SIZE*0.5), BLACK)
    pygame.display.update()
    name = os.path.join(os.path.dirname(__file__), "Fractal Snowflake.png")
    pygame.image.save(screen, name)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

if __name__ == '__main__':
    main()
