from cells import *
from resources import *
from resources import BREAD, WOOD, STONE, IRON, MONEY, WHEAT, IRON_ORE, GOLD_ORE
import random


class MainHall(pygame.sprite.Sprite):
    def __init__(self, group, board):
        super().__init__(group)
        self.image = load_image('main_hall_lvl1.png')
        self.rect = self.image.get_rect()
        self.board = board
        self.flag = True
        while True:
            self.rect.x, self.rect.y = random.randrange(0, WIDTH + 448, 16), random.randrange(16, HEIGHT, 16)
            x = self.rect.x
            y = self.rect.y
            f1 = True
            f2 = True
            try:
                for i in range(0, 64, 16):
                    if board.get_cell(x + i, y).im in safe_types:
                        f1 = True
                    else:
                        f1 = False
                        break
                for i in range(0, 64, 16):
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


class Mill(pygame.sprite.Sprite):
    def __init__(self, group, board, x, y):
        super().__init__(group)
        self.image = load_image('mill_1.png')
        self.rect = self.image.get_rect()
        self.board = board
        self.flag = True
        self.rect.x, self.rect.y = x, y
        self.rect.x = x
        self.rect.y = y
        self.prod_mod = 0
        for i in range(0, 17, 16):
            for j in range(0, 17, 16):
                if board.get_cell(x + i, y + j).im in safe_types and \
                        len(pygame.sprite.spritecollide(self, group, False)) <= 1:
                    self.prod_mod += 100
        if self.prod_mod != 400 or WOOD.get_value() < 250 or WHEAT.get_value() < 100:
            self.kill()
        else:
            WOOD.decrease(250)
            WHEAT.decrease(100)
            self.prod_mod = round(self.prod_mod)

    def update(self, *args, **kwargs):
        if TICK.get_value() % 50 == 0:
            self.image = load_image('mill_1.png')
            if TICK.get_value() % 500 == 0:
                if WHEAT.get_value() >= 100:
                    WHEAT.decrease(100)
                    BREAD.add(5)
        elif TICK.get_value() % 50 == 13:
            self.image = load_image('mill_2.png')
        elif TICK.get_value() % 50 == 25:
            self.image = load_image('mill_3.png')
        elif TICK.get_value() % 50 == 38:
            self.image = load_image('mill_4.png')


class Ferma(pygame.sprite.Sprite):
    def __init__(self, group, board, x, y):
        super().__init__(group)
        self.image = load_image('ferma_1.png')
        self.rect = self.image.get_rect()
        self.board = board
        self.flag = True
        self.rect.x = x
        self.rect.y = y
        self.prod_mod = 0
        try:
            for i in range(0, 17, 16):
                for j in range(0, 17, 16):
                    if board.get_cell(x + i, y + j).im in fertile_soils and \
                            len(pygame.sprite.spritecollide(self, group, False)) <= 1:
                        board.get_cell(x + i, y + j).type_change()
                        if self.prod_mod == 0:
                            self.prod_mod += 100
                        else:
                            self.prod_mod *= 1.5
            if self.prod_mod == 0 or WOOD.get_value() < 100:
                self.kill()
            else:
                WOOD.decrease(100)
                self.prod_mod = round(self.prod_mod)
        except:
            pass

    def update(self, *args, **kwargs):
        if TICK.get_value() % 200 == 0:
            self.image = load_image('ferma_1.png')
        elif TICK.get_value() % 200 == 50:
            self.image = load_image('ferma_2.png')
        elif TICK.get_value() % 200 == 100:
            self.image = load_image('ferma_3.png')
        elif TICK.get_value() % 200 == 150:
            WHEAT.add(round(10 * self.prod_mod / 100))
            self.image = load_image('ferma_4.png')


class Sawmill(pygame.sprite.Sprite):
    def __init__(self, group, board, x, y):
        super().__init__(group)
        self.image = load_image(sawmill_types[random.randint(0, 1)])
        self.rect = self.image.get_rect()
        self.board = board
        self.flag = True
        self.rect.x = x
        self.rect.y = y
        self.prod_mod = 0
        try:
            for i in range(0, 17, 16):
                for j in range(0, 17, 16):
                    if board.get_cell(x + i, y + j).im == 'forest_3.png' and \
                       len(pygame.sprite.spritecollide(self, group, False)) <= 1:
                        board.get_cell(x + i, y + j).type_change()
                        if self.prod_mod == 0:
                            self.prod_mod += 100
                        else:
                            self.prod_mod *= 1.5
            if self.prod_mod == 0 or WHEAT.get_value() < 200:
                self.kill()
            else:
                WHEAT.decrease(200)
                self.prod_mod = round(self.prod_mod)
        except:
            pass

    def select(self, x, y):
        if self.rect.x <= x <= self.rect.x + 32 and self.rect.y <= y <= self.rect.y + 32:
            print('WIP')

    def update(self, *args, **kwargs):
        if TICK.get_value() % 50 == 0:
            WOOD.add(round(10 * self.prod_mod / 100))


class FoundryIron(pygame.sprite.Sprite):
    def __init__(self, group, board, x, y):
        super().__init__(group)
        self.image = load_image('foundry.png')
        self.rect = self.image.get_rect()
        self.board = board
        self.flag = True
        self.rect.x = x
        self.rect.y = y
        self.prod_mod = 0
        try:
            for i in range(0, 17, 16):
                for j in range(0, 17, 16):
                    print(i, j)
                    if board.get_cell(x + i, y + j).im in safe_types and \
                            len(pygame.sprite.spritecollide(self, group, False)) <= 1:
                        board.get_cell(x + i, y + j).type_change()
                        self.prod_mod += 100
            if self.prod_mod != 400 or STONE.get_value() < 100 or WOOD.get_value() < 150 or WHEAT.get_value() < 100:
                self.kill()
            else:
                WOOD.decrease(150)
                STONE.decrease(100)
                WHEAT.decrease(100)
                self.prod_mod = round(self.prod_mod)
        except:
            pass

    def select(self, x, y):
        if self.rect.x <= x <= self.rect.x + 32 and self.rect.y <= y <= self.rect.y + 32:
            print('WIP')

    def update(self, *args, **kwargs):
        if TICK.get_value() % 100 == 0:
            if IRON_ORE.get_value() >= 10:
                IRON.add(10)
                IRON_ORE.decrease(10)
        if TICK.get_value() % 100 == 0:
            self.image = load_image('foundry_iron_1.png')
        elif TICK.get_value() % 100 == 50:
            self.image = load_image('foundry_iron_2.png')


class FoundryGold(pygame.sprite.Sprite):
    def __init__(self, group, board, x, y):
        super().__init__(group)
        self.image = load_image('foundry.png')
        self.rect = self.image.get_rect()
        self.board = board
        self.flag = True
        self.rect.x = x
        self.rect.y = y
        self.prod_mod = 0
        try:
            for i in range(0, 17, 16):
                for j in range(0, 17, 16):
                    print(i, j)
                    if board.get_cell(x + i, y + j).im in safe_types and \
                            len(pygame.sprite.spritecollide(self, group, False)) <= 1:
                        board.get_cell(x + i, y + j).type_change()
                        self.prod_mod += 100
            if self.prod_mod != 400 or STONE.get_value() < 100 or WOOD.get_value() < 150 or WHEAT.get_value() < 100:
                self.kill()
            else:
                WOOD.decrease(150)
                STONE.decrease(100)
                WHEAT.decrease(100)
                self.prod_mod = round(self.prod_mod)
        except:
            pass

    def select(self, x, y):
        if self.rect.x <= x <= self.rect.x + 32 and self.rect.y <= y <= self.rect.y + 32:
            print('WIP')

    def update(self, *args, **kwargs):
        if TICK.get_value() % 100 == 0:
            if IRON_ORE.get_value() >= 10:
                IRON.add(10)
                IRON_ORE.decrease(10)
        if TICK.get_value() % 100 == 0:
            self.image = load_image('foundry_gold_1.png')
        elif TICK.get_value() % 100 == 50:
            self.image = load_image('foundry_gold_2.png')


class MineRock(pygame.sprite.Sprite):
    def __init__(self, group, board, x, y):
        super().__init__(group)
        self.image = load_image('malevich_square.png')
        self.rect = self.image.get_rect()
        self.board = board
        self.flag = True
        self.rect.x = x
        self.rect.y = y
        self.prod_mod = 0
        try:
            for i in range(0, 17, 16):
                for j in range(0, 17, 16):
                    if board.get_cell(x + i, y + j).im == rock_types and \
                       len(pygame.sprite.spritecollide(self, group, False)) <= 1:
                        board.get_cell(x + i, y + j).type_change()
                        if self.prod_mod == 0:
                            self.prod_mod += 100
                        else:
                            self.prod_mod *= 1.5
            if self.prod_mod == 0 or WOOD.get_value() < 250 or WHEAT.get_value() < 150:
                self.kill()
            else:
                WHEAT.decrease(150)
                WOOD.decrease(250)
                self.prod_mod = round(self.prod_mod)
        except:
            pass

    def select(self, x, y):
        if self.rect.x <= x <= self.rect.x + 32 and self.rect.y <= y <= self.rect.y + 32:
            print('WIP')

    def update(self, *args, **kwargs):
        if TICK.get_value() % 50 == 0:
            STONE.add(10)


class MineGold(pygame.sprite.Sprite):
    def __init__(self, group, board, x, y):
        super().__init__(group)
        self.image = load_image('malevich_square.png')
        self.rect = self.image.get_rect()
        self.board = board
        self.flag = True
        self.rect.x = x
        self.rect.y = y
        self.prod_mod = 0
        try:
            for i in range(0, 17, 16):
                for j in range(0, 17, 16):
                    if board.get_cell(x + i, y + j).im == 'gold_rock.png' and \
                       len(pygame.sprite.spritecollide(self, group, False)) <= 1:
                        board.get_cell(x + i, y + j).type_change()
                        if self.prod_mod == 0:
                            self.prod_mod += 100
                        else:
                            self.prod_mod *= 1.5
            if self.prod_mod == 0 or WOOD.get_value() < 250 or WHEAT.get_value() < 150:
                self.kill()
            else:
                WHEAT.decrease(150)
                WOOD.decrease(250)
                self.prod_mod = round(self.prod_mod)
        except:
            pass

    def select(self, x, y):
        if self.rect.x <= x <= self.rect.x + 32 and self.rect.y <= y <= self.rect.y + 32:
            print('WIP')

    def update(self, *args, **kwargs):
        if TICK.get_value() % 50 == 0:
            GOLD_ORE.add(round(10 * self.prod_mod / 100))


class MineIron(pygame.sprite.Sprite):
    def __init__(self, group, board, x, y):
        super().__init__(group)
        self.image = load_image('malevich_square.png')
        self.rect = self.image.get_rect()
        self.board = board
        self.flag = True
        self.rect.x = x
        self.rect.y = y
        self.prod_mod = 0
        try:
            for i in range(0, 17, 16):
                for j in range(0, 17, 16):
                    if board.get_cell(x + i, y + j).im == 'iron.png' and \
                       len(pygame.sprite.spritecollide(self, group, False)) <= 1:
                        board.get_cell(x + i, y + j).type_change()
                        if self.prod_mod == 0:
                            self.prod_mod += 100
                        else:
                            self.prod_mod *= 1.5
            if self.prod_mod == 0 or WOOD.get_value() < 250 or WHEAT.get_value() < 150:
                self.kill()
            else:
                WHEAT.decrease(150)
                WOOD.decrease(250)
                self.prod_mod = round(self.prod_mod)
        except:
            pass

    def select(self, x, y):
        if self.rect.x <= x <= self.rect.x + 32 and self.rect.y <= y <= self.rect.y + 32:
            print('WIP')

    def update(self, *args, **kwargs):
        if TICK.get_value() % 50 == 0:
            IRON_ORE.add(round(10 * self.prod_mod / 100))


class Mint(pygame.sprite.Sprite):
    def __init__(self, group, board, x, y):
        super().__init__(group)
        self.image = load_image('mint.png')
        self.rect = self.image.get_rect()
        self.board = board
        self.flag = True
        self.rect.x = x
        self.rect.y = y
        self.prod_mod = 0
        try:
            for i in range(0, 17, 16):
                for j in range(0, 17, 16):
                    print(i, j)
                    if board.get_cell(x + i, y + j).im in safe_types and \
                            len(pygame.sprite.spritecollide(self, group, False)) <= 1:
                        board.get_cell(x + i, y + j).type_change()
                        self.prod_mod += 100
            if self.prod_mod != 400 or STONE.get_value() < 500 or WOOD.get_value() < 500 or BREAD.get_value() < 500:
                self.kill()
            else:
                WOOD.decrease(500)
                STONE.decrease(500)
                BREAD.decrease(500)
                self.prod_mod = round(self.prod_mod)
        except:
            pass

    def select(self, x, y):
        if self.rect.x <= x <= self.rect.x + 32 and self.rect.y <= y <= self.rect.y + 32:
            print('WIP')

    def update(self, *args, **kwargs):
        if TICK.get_value() % 100 == 0:
            if GOLD.get_value() >= 10:
                MONEY.add(100)
                GOLD.decrease(10)


def button_building_connect(group, board, x, y, btn):
    if btn == 'mill_btn.png':
        Mill(group, board, x, y)
    elif btn == 'fou_btn.png':
        FoundryIron(group, board, x, y)
    elif btn == 'saw_btn.png':
        Sawmill(group, board, x, y)
    elif btn == 'farm_btn.png':
        Ferma(group, board, x, y)
    elif btn == 'gfou_btn.png':
        FoundryGold(group, board, x, y)
