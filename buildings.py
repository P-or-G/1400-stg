from settings import *
import pygame
from cells import *
from resources import *
from resources import BREAD, WOOD, STONE, IRON, MONEY, WHEAT, IRON_ORE, GOLD_ORE


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
            self.rect.x, self.rect.y = random.randrange(0, WIDTH + 448, 16), random.randrange(16, HEIGHT, 16)
            x = self.rect.x
            y = self.rect.y
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
    def __init__(self, group, board, x, y):
        super().__init__(group)
        self.image = load_image('mill_1.png')
        self.rect = self.image.get_rect()
        self.board = board
        self.tick = 0
        self.flag = True
        while True:
            self.rect.x, self.rect.y = x, y
            x = self.rect.x
            y = self.rect.y
            x1 = x + 16
            y1 = y + 16
            try:
                if board.get_cell(x, y).im in safe_types and board.get_cell(x1, y).im in safe_types \
                        and board.get_cell(x, y1).im in safe_types and board.get_cell(x1, y1).im in safe_types:
                    break
            except:
                pass

    def update(self, *args, **kwargs):
        self.tick += 1
        if self.tick % 50 == 0:
            if WHEAT.get_value() >= 50:
                BREAD.add(10)
                WHEAT.decrease(50)
            self.image = load_image('mill_1.png')
        elif self.tick % 50 == 13:
            self.image = load_image('mill_2.png')
        elif self.tick % 50 == 25:
            self.image = load_image('mill_3.png')
        elif self.tick % 50 == 38:
            self.image = load_image('mill_4.png')


class Ferma(pygame.sprite.Sprite):
    def __init__(self, group, board, x, y):
        super().__init__(group)
        self.image = load_image('mill_1.png')
        self.rect = self.image.get_rect()
        self.board = board
        self.tick = 0
        self.flag = True
        while True:
            self.rect.x, self.rect.y = x, y
            x = self.rect.x
            y = self.rect.y
            x1 = x + 16
            y1 = y + 16
            try:
                if board.get_cell(x, y).im in safe_types and board.get_cell(x1, y).im in safe_types \
                        and board.get_cell(x, y1).im in safe_types and board.get_cell(x1, y1).im in safe_types:
                    break
            except:
                pass

    def update(self, *args, **kwargs):
        self.tick += 1
        if self.tick % 200 == 0:
            WHEAT.add(10)
            self.image = load_image('ferma_1.png')
        elif self.tick % 200 == 50:
            self.image = load_image('ferma_2.png')
        elif self.tick % 200 == 100:
            self.image = load_image('ferma_3.png')
        elif self.tick % 200 == 150:
            self.image = load_image('ferma_4.png')


class Sawmill(pygame.sprite.Sprite):
    def __init__(self, group, board, x, y):
        super().__init__(group)
        self.image = load_image(sawmill_types[random.randint(0, 1)])
        self.rect = self.image.get_rect()
        self.board = board
        self.tick = 0
        self.flag = True
        while True:
            self.rect.x, self.rect.y = x, y
            x = self.rect.x
            y = self.rect.y
            x1 = x + 16
            y1 = y + 16
            try:
                if board.get_cell(x, y).im in safe_types and board.get_cell(x1, y).im in safe_types \
                        and board.get_cell(x, y1).im in safe_types and board.get_cell(x1, y1).im in safe_types:
                    break
            except:
                pass

    def select(self, x, y):
        if self.rect.x <= x <= self.rect.x + 32 and self.rect.y <= y <= self.rect.y + 32:
            print('WIP')

    def update(self, *args, **kwargs):
        self.tick += 1
        if self.tick % 50 == 0:
            WOOD.add(20)


class FoundryIron(pygame.sprite.Sprite):
    def __init__(self, group, board, x, y):
        super().__init__(group)
        self.image = load_image('foundry.png')
        self.rect = self.image.get_rect()
        self.board = board
        self.tick = 0
        self.flag = True
        while True:
            self.rect.x, self.rect.y = x, y
            x = self.rect.x
            y = self.rect.y
            x1 = x + 16
            y1 = y + 16
            if board.get_cell(x, y).im in safe_types and board.get_cell(x1, y).im in safe_types \
                    and board.get_cell(x, y1).im in safe_types and board.get_cell(x1, y1).im in safe_types:
                break

    def select(self, x, y):
        if self.rect.x <= x <= self.rect.x + 32 and self.rect.y <= y <= self.rect.y + 32:
            print('WIP')

    def update(self, *args, **kwargs):
        self.tick += 1
        if self.tick % 100 == 0:
            if IRON_ORE.get_value() >= 10:
                IRON.add(50)
                IRON_ORE.decrease(10)


class FoundryGold(pygame.sprite.Sprite):
    def __init__(self, group, board, x, y):
        super().__init__(group)
        self.image = load_image('foundry.png')
        self.rect = self.image.get_rect()
        self.board = board
        self.tick = 0
        self.flag = True
        while True:
            self.rect.x, self.rect.y = x, y
            x = self.rect.x
            y = self.rect.y
            x1 = x + 16
            y1 = y + 16
            if board.get_cell(x, y).im in safe_types and board.get_cell(x1, y).im in safe_types \
                    and board.get_cell(x, y1).im in safe_types and board.get_cell(x1, y1).im in safe_types:
                break

    def select(self, x, y):
        if self.rect.x <= x <= self.rect.x + 32 and self.rect.y <= y <= self.rect.y + 32:
            print('WIP')

    def update(self, *args, **kwargs):
        self.tick += 1
        if self.tick % 100 == 0:
            if GOLD_ORE.get_value() >= 10:
                MONEY.add(50)
                GOLD_ORE.decrease(10)


class MineRock(pygame.sprite.Sprite):
    def __init__(self, group, board, x, y):
        super().__init__(group)
        self.image = load_image('malevich_square.png')
        self.rect = self.image.get_rect()
        self.board = board
        self.tick = 0
        self.flag = True
        while True:
            self.rect.x, self.rect.y = x, y
            x = self.rect.x
            y = self.rect.y
            try:
                if board.get_cell(x, y).im in rock_types:
                    break
            except:
                pass

    def select(self, x, y):
        if self.rect.x <= x <= self.rect.x + 32 and self.rect.y <= y <= self.rect.y + 32:
            print('WIP')

    def update(self, *args, **kwargs):
        self.tick += 1
        if self.tick % 50 == 0:
            STONE.add(10)


class MineGold(pygame.sprite.Sprite):
    def __init__(self, group, board, x, y):
        super().__init__(group)
        self.image = load_image('malevich_square.png')
        self.rect = self.image.get_rect()
        self.board = board
        self.tick = 0
        self.flag = True
        while True:
            self.rect.x, self.rect.y = x, y
            x = self.rect.x
            y = self.rect.y
            try:
                if board.get_cell(x, y).im == 'gold.png':
                    break
            except:
                pass

    def select(self, x, y):
        if self.rect.x <= x <= self.rect.x + 32 and self.rect.y <= y <= self.rect.y + 32:
            print('WIP')

    def update(self, *args, **kwargs):
        self.tick += 1
        if self.tick % 50 == 0:
            GOLD_ORE.add(5)


class MineIron(pygame.sprite.Sprite):
    def __init__(self, group, board, x, y):
        super().__init__(group)
        self.image = load_image('malevich_square.png')
        self.rect = self.image.get_rect()
        self.board = board
        self.tick = 0
        self.flag = True
        while True:
            self.rect.x, self.rect.y = x, y
            x = self.rect.x
            y = self.rect.y
            try:
                if board.get_cell(x, y).im == 'iron.png':
                    break
            except:
                pass

    def select(self, x, y):
        if self.rect.x <= x <= self.rect.x + 32 and self.rect.y <= y <= self.rect.y + 32:
            print('WIP')

    def update(self, *args, **kwargs):
        self.tick += 1
        if self.tick % 50 == 0:
            IRON_ORE.add(5)
