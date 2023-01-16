from cells import *
from resources import *
from resources import BREAD, WOOD, STONE, IRON, MONEY, WHEAT, IRON_ORE, GOLD_ORE
import random


class MainHallLvl:
    def __init__(self):
        self.value = 1

    def upgrade(self):
        if self.value < 3:
            self.value += 1

    def getvalue(self):
        return self.value


Mhl = MainHallLvl()


class MainHall(pygame.sprite.Sprite):
    def __init__(self, group, board):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно !!!
        super().__init__(group)
        self.image = load_image('main_hall_lvl1.png')
        self.rect = self.image.get_rect()
        self.board = board
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

    def update(self):
        if Mhl.getvalue() == 3:
            Win(w_or_lose)
            w_or_lose.draw(screen)
            pause.change()

    def select(self, x, y):
        if self.rect.x <= x <= self.rect.x + 64 and self.rect.y <= y <= self.rect.y + 64:
            if peoples.get_value() >= first_upgrade_people and Mhl.getvalue() == 1 \
               and WOOD.get_value() >= first_upgrade_wood and STONE.get_value() >= first_upgrade_stone \
               and IRON.get_value() >= first_upgrade_iron:

                WOOD.decrease(first_upgrade_wood)
                STONE.decrease(first_upgrade_stone)
                IRON.decrease(first_upgrade_iron)
                self.image = load_image('main_hall_lvl2.png')

                Mhl.upgrade()
            elif peoples.get_value() >= first_upgrade_people and Mhl.getvalue() == 2 \
                    and WOOD.get_value() >= second_upgrade_wood and STONE.get_value() >= second_upgrade_stone \
                    and IRON.get_value() >= second_upgrade_iron and GOLD.get_value() >= second_upgrade_gold \
                    and MONEY.get_value() >= second_upgrade_money:

                self.image = load_image('main_hall_lvl3.png')
                Mhl.upgrade()


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
        self.cou = 0
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
        self.cou += 1
        if WHEAT.get_value() >= 100:
            WHEAT.decrease(100)
            BREAD.add(5)
        if self.cou == 1:
            self.image = load_image('mill_1.png')
        elif self.cou == 2:
            self.image = load_image('mill_2.png')
        elif self.cou == 3:
            self.image = load_image('mill_3.png')
        elif self.cou == 4:
            self.image = load_image('mill_4.png')
            self.cou = 0


class Ferma(pygame.sprite.Sprite):
    def __init__(self, group, board, x, y):
        super().__init__(group)
        self.image = load_image('ferma_1.png')
        self.rect = self.image.get_rect()
        self.board = board
        self.flag = False
        self.rect.x = x
        self.rect.y = y
        self.prod_mod = 0
        self.cou = 1
        try:
            for i in range(0, 17, 16):
                for j in range(0, 17, 16):
                    if board.get_cell(x + i, y + j).im in fertile_soils and \
                            len(pygame.sprite.spritecollide(self, group, False)) <= 1:
                        cells = [board.get_cell(x + i, y + j)]
                        if self.prod_mod == 0:
                            self.prod_mod += 100
            if self.prod_mod == 0 or WOOD.get_value() < 100:
                self.kill()
            else:
                for cell in cells:
                    cell.type_change()
                WOOD.decrease(100)
                self.flag = True
        except:
            pass

    def update(self):
        WHEAT.add(50)
        if self.cou == 1:
            self.image = load_image('ferma_1.png')
        elif self.cou == 2:
            self.image = load_image('ferma_2.png')
        elif self.cou == 3:
            self.image = load_image('ferma_3.png')
        elif self.cou == 4:
            self.image = load_image('ferma_4.png')
            self.cou = 0
        self.cou += 1


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
        for i in range(0, 17, 16):
            for j in range(0, 17, 16):
                if board.get_cell(x + i, y + j).im == 'forest_3.png' and \
                   len(pygame.sprite.spritecollide(self, group, False)) <= 1:
                    cells = [board.get_cell(x + i, y + j)]
                    if self.prod_mod == 0:
                        self.prod_mod += 100
                    else:
                        self.prod_mod *= 1.5
        if self.prod_mod == 0 or WHEAT.get_value() <= 200:
            self.kill()
        else:
            for cell in cells:
                cell.type_change()
            WHEAT.decrease(200)
            self.prod_mod = round(self.prod_mod)

    def update(self, *args, **kwargs):
        WOOD.add(10)


class FoundryIron(pygame.sprite.Sprite):
    def __init__(self, group, board, x, y):
        super().__init__(group)
        self.image = load_image('foundry_iron_1.png')
        self.rect = self.image.get_rect()
        self.board = board
        self.flag = True
        self.rect.x = x
        self.rect.y = y
        self.prod_mod = 0
        for i in range(0, 17, 16):
            for j in range(0, 17, 16):
                if board.get_cell(x + i, y + j).im in safe_types and \
                        len(pygame.sprite.spritecollide(self, group, False)) <= 1:
                    self.prod_mod += 100
        if self.prod_mod != 400 or STONE.get_value() < 100 or WOOD.get_value() < 150 or WHEAT.get_value() < 100:
            self.kill()
        else:
            WOOD.decrease(150)
            STONE.decrease(100)
            WHEAT.decrease(100)
            self.prod_mod = round(self.prod_mod)

    def update(self, *args, **kwargs):
        if IRON_ORE.get_value() >= 10:
            IRON.add(10)
            IRON_ORE.decrease(10)


class FoundryGold(pygame.sprite.Sprite):
    def __init__(self, group, board, x, y):
        super().__init__(group)
        self.image = load_image('foundry_gold_1.png')
        self.rect = self.image.get_rect()
        self.board = board
        self.flag = True
        self.rect.x = x
        self.rect.y = y
        self.prod_mod = 0
        for i in range(0, 17, 16):
            for j in range(0, 17, 16):
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

    def update(self, *args, **kwargs):
        if IRON_ORE.get_value() >= 10:
            IRON.add(10)
            IRON_ORE.decrease(10)


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
        for i in range(0, 17, 16):
            for j in range(0, 17, 16):
                if board.get_cell(x + i, y + j).im in rock_types and \
                   len(pygame.sprite.spritecollide(self, group, False)) <= 1:
                    cells = [board.get_cell(x + i, y + j)]
                    if self.prod_mod == 0:
                        self.prod_mod += 100
                    else:
                        self.prod_mod *= 1.5
        if self.prod_mod == 0 or WOOD.get_value() < 250 or WHEAT.get_value() < 150:
            self.kill()
        else:
            for cell in cells:
                cell.type_change()
            WHEAT.decrease(150)
            WOOD.decrease(250)
            self.prod_mod = round(self.prod_mod)

    def update(self, *args, **kwargs):
        STONE.add(20)


class MineGold(pygame.sprite.Sprite):
    def __init__(self, group, board, x, y):
        super().__init__(group)
        self.image = load_image('gold_mine.png')
        self.rect = self.image.get_rect()
        self.board = board
        self.flag = True
        self.rect.x = x
        self.rect.y = y
        self.prod_mod = 0
        for i in range(0, 17, 16):
            for j in range(0, 17, 16):
                if board.get_cell(x + i, y + j).im == 'gold_rock.png' and \
                   len(pygame.sprite.spritecollide(self, group, False)) <= 1:
                    cells = [board.get_cell(x + i, y + j)]
                    if self.prod_mod == 0:
                        self.prod_mod += 100
                    else:
                        self.prod_mod *= 1.5
        if self.prod_mod == 0 or WOOD.get_value() < 250 or WHEAT.get_value() < 150:
            self.kill()
        else:
            for cell in cells:
                cell.type_change()
            WHEAT.decrease(150)
            WOOD.decrease(250)
            self.prod_mod = round(self.prod_mod)

    def update(self):
        GOLD_ORE.add(20)


class MineIron(pygame.sprite.Sprite):
    def __init__(self, group, board, x, y):
        super().__init__(group)
        self.image = load_image('iron_mine.png')
        self.rect = self.image.get_rect()
        self.board = board
        self.flag = True
        self.rect.x = x
        self.rect.y = y
        self.prod_mod = 0
        for i in range(0, 17, 16):
            for j in range(0, 17, 16):
                if board.get_cell(x + i, y + j).im == 'iron.png' and \
                   len(pygame.sprite.spritecollide(self, group, False)) <= 1:
                    cells = [board.get_cell(x + i, y + j)]
                    if self.prod_mod == 0:
                        self.prod_mod += 100
                    else:
                        self.prod_mod *= 1.5
        if self.prod_mod == 0 or WOOD.get_value() < 250 or WHEAT.get_value() < 150:
            self.kill()
        else:
            for cell in cells:
                cell.type_change()
            WHEAT.decrease(150)
            WOOD.decrease(250)
            self.prod_mod = round(self.prod_mod)

    def update(self):
        IRON_ORE.add(20)


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
        for i in range(0, 17, 16):
            for j in range(0, 17, 16):
                print(i, j)
                if board.get_cell(x + i, y + j).im in safe_types and \
                        len(pygame.sprite.spritecollide(self, group, False)) <= 1:
                    self.prod_mod += 100
        if self.prod_mod != 400 or STONE.get_value() < 500 or WOOD.get_value() < 500 or BREAD.get_value() < 500:
            self.kill()
        else:
            WOOD.decrease(500)
            STONE.decrease(500)
            IRON.decrease(50)
            self.prod_mod = round(self.prod_mod)

    def update(self, *args, **kwargs):
        if GOLD.get_value() >= 10:
            MONEY.add(100)
            GOLD.decrease(10)


class House(pygame.sprite.Sprite):
    def __init__(self, group, board, x, y):
        super().__init__(group)
        self.image = load_image(house_types[random.randint(0, 2)])
        self.rect = self.image.get_rect()
        self.board = board
        self.flag = True
        self.rect.x = x
        self.rect.y = y
        self.prod_mod = 0
        for i in range(0, 17, 16):
            for j in range(0, 17, 16):
                if board.get_cell(x + i, y + j).im in safe_types and \
                   len(pygame.sprite.spritecollide(self, group, False)) <= 1:
                    self.prod_mod += 5
        if self.prod_mod != 20:
            self.kill()
        else:
            people_limit.add(self.prod_mod)


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
    elif btn == 'rock_mine.png':
        MineRock(group, board, x, y)
    elif btn == 'mint_frame.png':
        Mint(group, board, x, y)
    elif btn == 'house_btn.png':
        House(group, board, x, y)
    elif btn == 'gold_mine_btn.png':
        MineGold(group, board, x, y)
    elif btn == 'iron_mine_btn.png':
        MineIron(group, board, x, y)
