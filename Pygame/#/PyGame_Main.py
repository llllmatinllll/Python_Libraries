import pygame, color, sys, time
from pygame.locals import *

pygame.init()

width = 800
height = 600

win = pygame.display.set_mod((width, height))
pygame.display.set_caption("PyGame")

while True:
    for event in pygame.event.get():
        if event == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()