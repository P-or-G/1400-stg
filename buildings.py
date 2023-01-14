from settings import *
import pygame
from cells import *


class MainHall(pygame.sprite.Sprite):
    def __init__(self, group, board):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно !!!
        super().__init__(group)
        self.image = load_image('main_hall_lvl1.png')
        self.rect = self.image.get_rect()
        self.board = board
        self.tick = 0
        self.flag = True
        while True:
            self.rect.x, self.rect.y = random.randrange(0, WIDTH + 448, 16), random.randrange(16, HEIGHT + 16, 16)
            x = self.rect.x
            y = self.rect.y
            x1 = x + 16
            y1 = y + 16
            try:
                if board.get_cell(x, y).get_im() in safe_types and board.get_cell(x1, y).get_im() in safe_types \
                   and board.get_cell(x, y1).get_im() in safe_types and board.get_cell(x1, y1).get_im() in safe_types:
                    break

            except:
                pass

    def select(self, x, y):
        if self.rect.x <= x <= self.rect.x + 32 and self.rect.y <= y <= self.rect.y + 32:
            print("WIP")

    def update(self, *args, **kwargs):
        self.tick += 1


class Mill(pygame.sprite.Sprite):
    def __init__(self, group, board):
        super().__init__(group)
        self.image = load_image('mill_1.png')
        self.rect = self.image.get_rect()
        self.board = board
        self.tick = 0
        self.flag = True
        while True:
            self.rect.x, self.rect.y = random.randrange(16, WIDTH, 16), random.randrange(16, HEIGHT, 16)
            x = self.rect.x
            y = self.rect.y
            try:
                if board.get_cell(x, y).im in safe_types:
                    break
            except:
                pass

        # ----------------------------------------------------------------------------------------------------------------------
        #   ПЕРЕМЕННАЯ ВРЕМЕННА И ПОДЛЕЖИТ РАСТРЕЛУ!!!
        self.wheat = 0
        # ----------------------------------------------------------------------------------------------------------------------

#        self.rect.x, self.rect.y = random.randrange(448, WIDTH + 448 - 16, 16), random.randrange(16, HEIGHT + 16 - 16, 16)
#
#    def select(self, x, y):
#        if self.rect.x <= x <= self.rect.x + 32 and self.rect.y <= y <= self.rect.y + 32:
#            print('WIP')

    def update(self, *args, **kwargs):
        self.tick += 1
        if self.tick % 50 == 0:
            self.image = load_image('mill_1.png')
            self.wheat += 10
            print(self.wheat)
        elif self.tick % 50 == 13:
            self.image = load_image('mill_2.png')
        elif self.tick % 50 == 25:
            self.image = load_image('mill_3.png')
        elif self.tick % 50 == 38:
            self.image = load_image('mill_4.png')
