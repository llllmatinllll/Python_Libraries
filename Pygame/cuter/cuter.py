import pygame, color, time, sys
from pygame.constants import QUIT

pygame.init()

y2 = 0
sp = 0
epY = 0
epX = 0
frame = 0
fps = 0
starttime = round(time.time())
hold = False
cut = False
win = False

#scherm grootte, titel en icon
screen = pygame.display.set_mode((1280,720))
pygame.mouse.set_visible(0)
pygame.display.set_caption("cutting game")
icon = pygame.image.load("icon.png").convert_alpha()
pygame.display.set_icon(icon)

#doos
dozen = [pygame.image.load("doos1.png").convert_alpha(),
         pygame.image.load("doos2.png").convert_alpha(),
         pygame.image.load("doos3.png").convert_alpha(),
         pygame.image.load("doos4.png").convert_alpha(),
         pygame.image.load("doos5.png").convert_alpha()]
doosnum = 1

#cutting part
CPO = pygame.image.load("cutting part overlay.png").convert_alpha()

#cursor
cursor = pygame.image.load("stanley-mes.png").convert_alpha()
cursor = pygame.transform.scale(cursor, (200, 200))

#text
text = "cutting game"
titlefont = pygame.font.SysFont('Arial', 100, True)
fpsfont = pygame.font.SysFont('Arial', 30)

#win icon
winicon = pygame.image.load("win icon.png").convert_alpha()

running = True
while running == True:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            pygame.quit()
            sys.exit()
    screen.fill((color.blue))
    x, y = pygame.mouse.get_pos()
    x -= cursor.get_width()/2
    y -= cursor.get_height()/2
    if hold == False:
        y2 = y
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            hold = True
            spX, spY = pygame.mouse.get_pos()
        elif event.type == pygame.MOUSEBUTTONUP:
            hold = False
            cut = True
    if hold == True:
        screen.fill((color.red))
    if win == False:
        screen.blit(dozen[doosnum-1], (390, 550))
    if hold == True: 
        epX, epY = pygame.mouse.get_pos()
        pygame.draw.line(screen, (0, 0, 0), (spX, spY), (epX, spY))        
    if cut == True and win == False:
        if doosnum == 1:
            if epX < 405 and spX > 870 or epX > 870 and spX < 405:
                if spY > 570 and spY < 595:
                    text = "good cut"
                    cut = False
                    doosnum = 2
                else:
                    text = "bad cut"
                    cut = False
            else:
                text = "bad cut"
                cut = False
        elif doosnum == 2:
            if epX < 407 and spX > 872 or epX > 872 and spX < 407:
                if spY > 570 and spY < 590:
                    text = "good cut"
                    cut = False
                    doosnum = 3
                else:
                    text = "bad cut"
                    cut = False
                    doosnum = 1
            else:
                text = "bad cut"
                cut = False
                doosnum = 1
        elif doosnum == 3:
            if epX < 408 and spX > 868 or epX > 868 and spX < 408:
                if spY > 290 and spY < 590:
                    text = "good cut"
                    cut = False
                    doosnum = 4
                else:
                    text = "bad cut"
                    cut = False
                    doosnum = 1
            else:
                text = "bad cut"
                cut = False
                doosnum = 1
        elif doosnum == 4:
            if epX < 410 and spX > 869 or epX > 869 and spX < 410:
                if spY > 580 and spY < 585:
                    text = "good cut"
                    cut = False
                    doosnum = 5
                else:
                    text = "bad cut"
                    cut = False
                    doosnum = 1
            else:
                text = "bad cut"
                cut = False
                doosnum = 1
        elif doosnum == 5:
            if epX < 412 and spX > 868 or epX > 868 and spX < 412:
                if spY > 579 and spY < 583:
                    text = "game won"
                    cut = False
                    win = True
                else:
                    text = "bad cut"
                    cut = False
                    doosnum = 1
            else:
                text = "bad cut"
                cut = False
                doosnum = 1
    if hold == True:
        screen.blit(CPO, (0, 0))
    screen.blit(cursor, (x, y2))
    if win == True:
        screen.blit(winicon, (385, 150))
    text_r = titlefont.render(text, True, (color.white))
    text_pos = text_r.get_rect(center=(640, 60))
    screen.blit(text_r, text_pos)
    frame += 1
    if round(time.time()) - starttime == 1:
        fps = frame
        frame = 0
        starttime = round(time.time())
    screen.blit(fpsfont.render(str(fps), True, (color.white)), (1200, 650))
    pygame.time.Clock().tick(100)
    pygame.display.update()
