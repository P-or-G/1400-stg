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
            self.rect.x, self.rect.y = random.randrange(0, WIDTH + 448 - 64, 16), random.randrange(16, HEIGHT + 16 - 64, 16)
            x = self.rect.x
            y = self.rect.y
            f1 = True
            f2 = True
            try:
                for i in range(0, 65, 16):
                    if board.get_cell(x + i, y).im in safe_types:
                        f1 = True
                    else:
                        f1 = False
                        break
                for i in range(0, 65, 16):
                    if board.get_cell(x, y + i).im in safe_types:
                        f2 = True
                    else:
                        f2 = False
                        break
                if f1 and f2:
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
