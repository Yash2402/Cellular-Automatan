import random
import pygame
from cell import Cell
import copy

pygame.init()

W = 1024
H = 900
w = 8
screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
initial_state = []

for x in range(0, W, w):
    buffer = []
    for y in range(0, H, w):
        i = x//w
        j = y//w
        if (i == 0 or j == 0) or (i == (W//w) - 1 or j == (H//w) - 1):
            buffer.append(
                Cell((i, j), (x, y, w, w), 'wall'))
        else:
            buffer.append(
                Cell((i, j), (x, y, w, w), 'air'))
    initial_state.append(buffer)

cells = copy.deepcopy(initial_state)
run = True
clock = pygame.time.Clock()
upd = True
elementchoosen = 'sand'
editWidth = 3
while run:
    clock.tick(120)
    screen.fill((64, 64, 64))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                elementchoosen = 'sand'
                editWidth = 3
            if event.key == pygame.K_2:
                elementchoosen = 'fluid'
                editWidth = 3
            if event.key == pygame.K_3:
                elementchoosen = 'smoke'
                editWidth = 1
            if event.key == pygame.K_4:
                elementchoosen = 'wall'
                editWidth = 2
            if event.key == pygame.K_SPACE:
                upd = not upd
            if event.key == pygame.K_r:
                cells = copy.deepcopy(initial_state)
            
        if pygame.mouse.get_pressed()[0]:
            mousepos = pygame.mouse.get_pos()
            if (mousepos[0] < W - 1 and mousepos[1] < H - 1 and mousepos[0] > 0 and mousepos[1] > 0) and elementchoosen != 'wall':
                i = int(mousepos[0]/(w))
                j = int(mousepos[1]/(w))
                for x in range(i-editWidth, i+editWidth+1):
                    for y in range(j-editWidth, j+editWidth+1):
                        prob = random.randint(0, 1)
                        if prob:
                            cells[x][y].element = elementchoosen
            if (mousepos[0] < W - 1 and mousepos[1] < H - 1 and mousepos[0] > 0 and mousepos[1] > 0) and elementchoosen == 'wall':
                i = int(mousepos[0]/(w))
                j = int(mousepos[1]/(w))
                for x in range(i-editWidth, i+editWidth+1):
                    for y in range(j-editWidth, j+editWidth+1):
                        prob = 1
                        if prob:
                            cells[x][y].element = elementchoosen
                        
        if pygame.mouse.get_pressed()[2]:
            mousepos = pygame.mouse.get_pos()
            if mousepos[0] < W - 1 and mousepos[1] < H - 1 and mousepos[0] > 0 and mousepos[1] > 0:
                i = int(mousepos[0]/w)
                j = int(mousepos[1]/w)
                for x in range(i-editWidth, i+editWidth+1):
                    for y in range(j-editWidth, j+editWidth+1):
                        cells[x][y].element = 'air'

    if upd:
        cells = Cell.update(cells)
    for i in range(len(cells)):
        for j in range(len(cells[0])):
            cells[i][j].show(screen)

    pygame.display.update()