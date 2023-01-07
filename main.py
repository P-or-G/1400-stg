import pygame
from settings import *
from cells import Board
from buildings import *

pygame.init()
screen = pygame.display.set_mode(SIZE)

board = Board(CELL_HOR_NUM, CELL_VERT_NUM, CELL_SIDE)

all_sprites = board.render()
mh = MainHall(all_sprites, hall_crds[0], hall_crds[1])

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if mh.tick % 60 == 0:
        m_x, m_y = pygame.mouse.get_pos()
        mh.select(m_x, m_y)

    clock.tick(60)
    screen.fill(pygame.Color('black'))

    all_sprites.draw(screen)
    all_sprites.update()

    pygame.display.flip()

pygame.quit()
