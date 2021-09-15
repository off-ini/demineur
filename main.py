import pygame
from random import randrange
from copy import deepcopy
from src.Surf import Surf

screen = w, h = 400, 400

nombre = (10,10)
nombre_mines = 10

BLACK, WHITE = (0,0,0), (255,255,255)
LEFT, RIGHT = 1, 3

screen_mode = pygame.display.set_mode(screen)
background = pygame.Surface(screen_mode.get_size())
background = background.convert()
background.fill(WHITE)

pygame.display.set_caption('Démineur')

def random_mines(grid_size, nb):
    list_mines = []
    for i in range(nb):
        x, y = randrange(grid_size[0]), randrange(grid_size[1])
        for el in list_mines:
            if (x+y) == el[0]+el[1]:
                 x, y = randrange(grid_size[0]), randrange(grid_size[1])
        # print((x,y))
        list_mines.append((x,y))
    return list_mines

# 
def make_grille_with_mines(nb, w, h):
    nb_w, nb_h = w/nb[0], h/nb[1]
    nb_x_draw, nb_y_draw = 0,0
    mines = random_mines(nb, nombre_mines)
    sufaces = []
    for y in range(nb[1]):
        tab = []
        nb_x_draw = 0
        for x in range(nb[0]):
            s = Surf(screen_mode, color=WHITE, rect=(nb_x_draw,nb_y_draw, nb_w-1,nb_h-1))
            for el in mines:
                if x == el[0] and y == el[1]:
                    s.status = 10
            nb_x_draw += nb_w
            tab.append(s)
        nb_y_draw += nb_h
        sufaces.append(tab)
    return sufaces

def make_grille_with_number(surfs):
    tmp = cloning(surfs)
    x,y = 0,0
    for y in range(len(tmp)):
        while x < len(tmp[y]):
            e = getElement(x, y, tmp).getStatus()
            if e != 10:
                v = getElementStatus(x,y, tmp)
                tmp[y][x].setStatus(v)
                # print(tmp[y][x].status)
            tmp[y][x].opened = 0
            x += 1
        x=0
        y+=1
    return tmp

def length(surfs):
    w,h,check = 0,0,True
    h = len(surfs)

    for i in range(len(surfs)):
        if i == 0:
            tmp = len(surfs[i])
        elif tmp != len(surfs[i]):
            check = False
            break
    if check == False:
        return (0,0)
    w = len(surfs[0])
    return (w,h)

def cloning(li1): 
    li_copy = deepcopy(li1) 
    return li_copy

def parse_status(status):
    if(status == 10): return 1
    else: return 0

def getElement(x,y, surfs):
    w,h = length(surfs)
    if x < 0 or x > w-1 or y < 0 or y > h-1:
        return Surf(screen_mode, color=WHITE)
    return surfs[y][x]

def getElementStatus(x,y, surfs):
    v = int(0)
    v = v + parse_status(getElement(x-1, y-1, surfs).getStatus())
    v = v + parse_status(getElement(x-1, y+1, surfs).getStatus())
    v = v + parse_status(getElement(x-1, y, surfs).getStatus())
    v = v + parse_status(getElement(x, y-1, surfs).getStatus())
    v = v + parse_status(getElement(x, y+1, surfs).getStatus())
    v = v + parse_status(getElement(x+1, y-1, surfs).getStatus())
    v = v + parse_status(getElement(x+1, y+1, surfs).getStatus())
    v = v + parse_status(getElement(x+1, y, surfs).getStatus())
    return v

def see(surfs, x,y):
    w,h = length(surfs)
    if surfs[y][x].opened == 1:
        return
    if surfs[y][x].status == 0:
        surfs[y][x].opened = 1
    elif (surfs[y][x].status >= 1 and surfs[y][x].status <= 8):
        surfs[y][x].opened = 1
        return
 
    if x < w-1:
        see(surfs, x+1,y)
    if x > 0:
        see(surfs, x-1,y)
    if y > 0:
        see(surfs, x,y-1)
    if y < h-1:
        see(surfs, x,y+1)  

def gameover(surfs):
    for col in surfs:
        for el in col:
            el.opened = 1

def win(surfs, nombre_mines):
    closed = 0
    w = False
    for col in surfs:
        for el in col:
            if el.opened == 0:
                closed = closed + 1
        if closed > nombre_mines:
            break
    if closed == nombre_mines:
        w = True

    return w

def game_play(surfs, element, x, y):
    stop = False
    if element.status >= 1 and element.status <= 8:
        element.opened = 1
    elif element.status == 10:
        element.status = 11
        gameover(surfs)
        stop = True
    else: see(surfs, x, y)

    return stop

sufs = []
sufs = make_grille_with_mines(nombre, w, h)
sufs = make_grille_with_number(sufs)

playing = True
running = True
while(running):
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if playing == True:
            if e.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                y = 0
                for el in sufs:
                    x = 0
                    for s in el:
                        if s.rect.collidepoint(pos):
                            if e.button == LEFT:
                                if game_play(sufs, s, x, y) == True:
                                    playing = False
                            elif e.button == RIGHT:
                                if s.opened == 0:
                                    s.opened = 2
                                elif s.opened == 2:
                                    s.opened = 0
                        x = x+1
                    y = y+1  

        if playing == False: 
            if e.type == pygame.KEYDOWN or win(sufs, nombre_mines):
                if e.key == pygame.K_SPACE:
                    sufs = make_grille_with_mines(nombre, w, h)
                    sufs = make_grille_with_number(sufs)
                    playing = True
    
    screen_mode.blit(background, (0,0))
    for l in sufs:
        for el in l:
            el.draw(screen_mode)
    
    pygame.display.flip()
    pygame.time.Clock().tick(500)

pygame.quit()