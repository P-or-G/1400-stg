import pygame
from settings import *
from cells import Board
from buildings import *
import os
from resources import BREAD, WOOD, STONE, IRON, MONEY, WHEAT, IRON_ORE, GOLD_ORE

pygame.init()


os.environ['SDL_VIDEO_WINDOW_POS'] = "448,0"
screen = pygame.display.set_mode(TRUE_SIZE, pygame.NOFRAME)

board = Board(CELL_HOR_NUM, CELL_VERT_NUM, CELL_SIDE)

all_sprites = board.render()

all_sprites.draw(screen)
all_sprites.update()

buildings = pygame.sprite.Group()

mh = MainHall(buildings, board)
mill = Mill(buildings, board)
sawmill = Sawmill(buildings, board)
mine = MineRock(buildings, board)

clock = pygame.time.Clock()

fl_open = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if mh.tick % 60 == 0 and not fl_open:
        m_x, m_y = pygame.mouse.get_pos()
        mh.select(m_x, m_y)

    if mine.tick % 60 == 0 and not fl_open:
        mine_x, mine_y = pygame.mouse.get_pos()
        mh.select(mine_x, mine_y)

    if sawmill.tick % 60 == 0 and not fl_open:
        sawmill_x, sawmill_y = pygame.mouse.get_pos()
        mh.select(sawmill_x, sawmill_y)

    if mill.tick % 60 == 0:
        mill_x, mill_y = pygame.mouse.get_pos()
        mh.select(mill_x, mill_y)

    clock.tick(60)
    screen.fill(pygame.Color('black'))

    all_sprites.draw(screen)
    all_sprites.update()

    buildings.draw(screen)
    buildings.update()

    pygame.display.flip()

pygame.quit()
