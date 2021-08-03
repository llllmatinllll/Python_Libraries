import pygame, sys, random, time

from pygame.display import update
from pygame.draw import rect
import color 
from pygame.locals import *


pygame.init()
fps = 10
win_width = 800
win_height = 600
worm_x = 380
worm_y = 280 
speed_worm_x = 0
speed_worm_y = 0
food_x = random.randrange(0, 780, 20)
food_y = random.randrange(0, 580, 20)
worm_list = []
worm_length = 0
GameOver = False
a = ["r", "l", "u", "d"]
score = 0
font_score = pygame.font.Font(None, 40)
font_GameOver = pygame.font.Font(None, 80)
scr = 0
bomb_x = random.randrange(0, 780, 20)
bomb_y = random.randrange(0, 580, 20)


win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

def worm_function(wrm_lst, wrm_x, wrm_y):
    g_over = False
    worm_head = [wrm_x, wrm_y]
    wrm_lst.append(worm_head)
    for lst in wrm_lst:
        pygame.draw.rect(win, color.green, (lst[0], lst[1], 20, 20))
    for each_section in wrm_lst[:-1]:
        if each_section == worm_head:
            g_over = True
    return g_over

while not GameOver:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT and "l" in a:
                speed_worm_x = 20
                speed_worm_y = 0
                a.clear()
                a.append("l")
                a.append("u")
                a.append("d")
            if event.key == K_LEFT and "r" in a:
                speed_worm_x = -20
                speed_worm_y = 0
                a.clear()
                a.append("r")
                a.append("u")
                a.append("d")
            if event.key == K_DOWN and "d" in a:
                speed_worm_y = 20
                speed_worm_x = 0
                a.clear()
                a.append("l")
                a.append("r")
                a.append("d")
            if event.key == K_UP and "u" in a:
                speed_worm_y = -20
                speed_worm_x = 0
                a.clear()
                a.append("r")
                a.append("l")
                a.append("u")
    worm_x += speed_worm_x
    worm_y += speed_worm_y
    if worm_x < 0 :
        worm_x = 780
    if worm_x > 780 :
        worm_x = 0
    if worm_y < 0 :
        worm_y = 580
    if worm_y > 580 :
        worm_y = 0
    if worm_x == food_x and worm_y == food_y:
        food_x = random.randrange(0, 780, 20)
        food_y = random.randrange(0, 580, 20)
        worm_length += 1
        if score%6 != 5:
            scr += 1
            score += 1
        else:
            scr += 5
            score += 1 
    if len(worm_list) > worm_length:
        worm_list.pop(0)
    win.fill(color.black)
    if worm_function(worm_list, worm_x, worm_y):
        GameOver = True
    if score%5 != 0 or score==0:
        pygame.draw.rect(win, color.red, (food_x, food_y, 20, 20))
    if score%5 == 0 and score!=0:
        pygame.draw.rect(win, color.blue, (food_x, food_y, 20, 20))
    pygame.draw.rect(win, color.green, (worm_x, worm_y, 20, 20))
    t_score = font_score.render("Score : " + str(scr), True, (color.yellow))
    win.blit(t_score, (30, 30))
    pygame.display.update()
    clock.tick(fps)
t_GameOver = font_GameOver.render("Game Over", True, (color.red))
win.blit(t_GameOver, (270, 270))
pygame.display.update()
time.sleep(3)
