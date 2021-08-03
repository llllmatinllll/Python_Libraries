import pygame, sys
from pygame.locals import *
pygame.init()

win = pygame.display.set_mode((800, 600))
x = 0
y = 0
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)
purple = (255, 0, 255)
color = red

while True:
    win.fill(black)
    pygame.draw.line(win, color, (x, 0), (x, 600), 5)
    pygame.draw.line(win, color, (0, y), (800, y), 5)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit
            sys.exit()
        if event.type == MOUSEMOTION:
            x, y = event.pos
        if event.type == KEYDOWN:
            if event.key == K_r:
                color = red
            if event.key == K_b:
                color = blue
            if event.key == K_g:
                color = green
            if event.key == K_w:
                color = white
            if event.key == K_p:
                color = purple
        pygame.display.update()
    
    