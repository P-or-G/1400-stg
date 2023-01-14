import pygame
from settings import *
from cells import Board
from buildings import *
import os
from resources import BREAD, WOOD, STONE, IRON, MONEY, WHEAT, IRON_ORE, GOLD_ORE
from interface import *

pygame.init()


os.environ['SDL_VIDEO_WINDOW_POS'] = "0,0"
screen = pygame.display.set_mode(TRUE_SIZE, pygame.NOFRAME)

board = Board(CELL_HOR_NUM, CELL_VERT_NUM, CELL_SIDE)

all_sprites = board.render()

all_sprites.draw(screen)
all_sprites.update()


buildings = pygame.sprite.Group()

mh = MainHall(buildings, board)


interface = pygame.sprite.Group()

Bt1 = Button(interface, 'mill_btn.png', 1024, 512)
Bt2 = Button(interface, 'mill_btn.png', 1060, 512)


clock = pygame.time.Clock()

fl_btn_select = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:

            x, y = pygame.mouse.get_pos()

            if fl_btn_select == 0:

                for btn in interface:
                    if btn.select(x, y):

                        x_tr = btn.rect.x
                        y_tr = btn.rect.y
                        im_tr = btn.type
                        tr_btn = btn
                        fl_btn_select = 1

            elif fl_btn_select == 1:

                fl_btn_select = 0
                Mill(buildings, board, pygame.mouse.get_pos()[0] // 16 * 16, pygame.mouse.get_pos()[1] // 16 * 16)
                tr_btn.kill()
                Button(interface, im_tr, x_tr, y_tr)

    if fl_btn_select == 1:
        tr_btn.rect = (pygame.mouse.get_pos()[0] // 16 * 16, pygame.mouse.get_pos()[1] // 16 * 16)

    clock.tick(60)
    screen.fill(pygame.Color('black'))

    all_sprites.draw(screen)
    all_sprites.update()

    buildings.draw(screen)
    buildings.update()

    interface.draw(screen)
    interface.update()

    pygame.display.flip()

pygame.quit()
