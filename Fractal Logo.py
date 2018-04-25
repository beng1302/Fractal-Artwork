"""makes some simple artwork in a jagged style"""

import random
import sys
import os
import itertools
import pygame

SIZE = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

pygame.init()
screen = pygame.display.set_mode((SIZE, SIZE))
pygame.display.set_caption('Fractal Logo')

def randomline(iterations, color, thickness):
    """create multiple random lines"""
    for _ in itertools.repeat(None, iterations):
        randx0 = random.randint(0, SIZE)
        randy0 = random.randint(0, SIZE)
        randx1 = random.randint(0, SIZE)
        randy1 = random.randint(0, SIZE)
        if randx0 == randx1:
            pygame.draw.line(screen, color, (randx0, 0), (randx1, SIZE), thickness)
        elif randy0 == randy1:
            pygame.draw.line(screen, color, (0, randy0), (SIZE, randy1), thickness)
        else:
            m = float(randy1-randy0)/(randx1-randx0)
            if m > 1 or m < -1:
                x0 = (randy0)/m+randx0
                x1 = (SIZE+randy0)/m+randx0
                pygame.draw.line(screen, color, (x0, 0), (x1, SIZE), thickness)
            else:
                y0 = m*(-randx0)+randy0
                y1 = m*(SIZE-randx0)+randy0
                pygame.draw.line(screen, color, (0, y0), (SIZE, y1), thickness)

def letters(color):
    """draw letters using polygons"""
    word = []
    #F
    word.append([[SIZE*0.12, SIZE*0.2],
    [SIZE*0.12, SIZE*0.4],
    [SIZE*0.14, SIZE*0.4],
    [SIZE*0.14, SIZE*0.3],
    [SIZE*0.22, SIZE*0.3],
    [SIZE*0.22, SIZE*0.28],
    [SIZE*0.14, SIZE*0.28],
    [SIZE*0.14, SIZE*0.22],
    [SIZE*0.22, SIZE*0.22],
    [SIZE*0.22, SIZE*0.2]])
    #R
    word.append([[SIZE*0.23, SIZE*0.2],
    [SIZE*0.23, SIZE*0.4],
    [SIZE*0.25, SIZE*0.4],
    [SIZE*0.25, SIZE*0.3],
    [SIZE*0.29, SIZE*0.3],
    [SIZE*0.31, SIZE*0.4],
    [SIZE*0.33, SIZE*0.4],
    [SIZE*0.31, SIZE*0.3],
    [SIZE*0.33, SIZE*0.3],
    [SIZE*0.33, SIZE*0.2]])
    #A
    word.append([[SIZE*0.34, SIZE*0.4],
    [SIZE*0.44, SIZE*0.4],
    [SIZE*0.39, SIZE*0.2]])
    #C
    word.append([[SIZE*0.45, SIZE*0.2],
    [SIZE*0.45, SIZE*0.4],
    [SIZE*0.55, SIZE*0.4],
    [SIZE*0.55, SIZE*0.38],
    [SIZE*0.47, SIZE*0.38],
    [SIZE*0.47, SIZE*0.22],
    [SIZE*0.55, SIZE*0.22],
    [SIZE*0.55, SIZE*0.2]])
    #T
    word.append([[SIZE*0.56, SIZE*0.2],
    [SIZE*0.56, SIZE*0.22],
    [SIZE*0.60, SIZE*0.22],
    [SIZE*0.60, SIZE*0.4],
    [SIZE*0.62, SIZE*0.4],
    [SIZE*0.62, SIZE*0.22],
    [SIZE*0.66, SIZE*0.22],
    [SIZE*0.66, SIZE*0.2]])
    #A
    word.append([[SIZE*0.67, SIZE*0.4],
    [SIZE*0.77, SIZE*0.4],
    [SIZE*0.72, SIZE*0.2]])
    #L
    word.append([[SIZE*0.78, SIZE*0.2],
    [SIZE*0.78, SIZE*0.4],
    [SIZE*0.88, SIZE*0.4],
    [SIZE*0.88, SIZE*0.38],
    [SIZE*0.80, SIZE*0.38],
    [SIZE*0.80, SIZE*0.2]])
    
    for letter in word:
        pygame.draw.polygon(screen, color, letter)
    #CIRCLE
    pygame.draw.circle(screen, color, [int(SIZE*0.28), int(SIZE*0.7)], int(SIZE*0.1), 0)
    #SQUARE
    pygame.draw.rect(screen, color, [SIZE*0.4, SIZE*0.6, SIZE*0.2, SIZE*0.2])
    #TRIANGLE
    pygame.draw.polygon(screen, color, [(SIZE*0.62, SIZE*0.8), (SIZE*0.82, SIZE*0.8), (SIZE*0.72, SIZE*0.6)])

def borderfill(image, x, y, color1, color2):
    """fill area with color1 until color2 is met"""
    if image.get_at((x, y)) != color1:
        return 0
    image.set_at((x, y), color1)
    bucket = [(x, y)]
    while bucket:
        (a, b) = bucket[0]
        del bucket[0]
        if a != 0 and a != SIZE-1 and b != 0 and b != SIZE-1:
            if image.get_at((a+1, b)) != color1 and image.get_at((a+1, b)) != color2:
                image.set_at((a+1, b), color1)
                bucket.append((a+1, b))
            if image.get_at((a-1, b)) != color1 and image.get_at((a-1, b)) != color2:
                image.set_at((a-1, b), color1)
                bucket.append((a-1, b))
            if image.get_at((a, b+1)) != color1 and image.get_at((a, b+1)) != color2:
                image.set_at((a, b+1), color1)
                bucket.append((a, b+1))
            if image.get_at((a, b-1)) != color1 and image.get_at((a, b-1)) != color2:
                image.set_at((a, b-1), color1)
                bucket.append((a, b-1))

def replace(color1, color2):
    """replace any color with another"""
    pxarray = pygame.PixelArray(screen)
    pxarray.replace(color1, color2, 0)
    del pxarray

def paint(lines, thickness, colors=[]):
    """make the artwork"""
    if not colors:
        for _ in itertools.repeat(None, 2):
            colors.append(tuple(random.sample(range(0, 255), 3)))
    tempcolor = tuple(random.sample(range(0, 255), 3))
    screen.fill(colors[0])
    letters(colors[1])
    randomline(lines, tempcolor, thickness)
    for x in range(0, SIZE):
        for y in range(0, SIZE):
            if screen.get_at((x, y)) == colors[1]:
                borderfill(screen, x, y, colors[1], tempcolor)
    replace(tempcolor, colors[0])

def main():
    """run the program"""
    paint(300, 1, [])
    pygame.display.update()
    name = os.path.join(os.path.dirname(__file__), "Fractal Logo.png")
    pygame.image.save(screen, name)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

if __name__ == '__main__':
    main()
