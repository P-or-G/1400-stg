from settings import *
import random
from Win_and_lose import w_or_lose, Lose, Win


class Resource:
    def __init__(self, num):
        self.value = num

    def add(self, num):
        self.value += num

    def decrease(self, num, bl=False):
        if self.value - num >= 0 or bl:
            self.value -= num
        else:
            return False

    def set_zero(self):
        self.value = 0

    def get_value(self):
        return self.value


BREAD = Resource(start_bread)
WOOD = Resource(start_wood)
STONE = Resource(start_stone)
IRON = Resource(start_iron)
MONEY = Resource(start_money)
WHEAT = Resource(start_wheat)
IRON_ORE = Resource(start_iron_ore)
GOLD = Resource(start_gold)
GOLD_ORE = Resource(start_gold_ore)
people_limit = Resource(start_house_cap)


class Peoples:
    global people_limit

    def __init__(self, num):
        self.num = num
        self.cou = 0

    def update(self):
        self.cou += 1
        if self.cou % 3 == 0:
            self.cou = 0
            if people_limit.get_value() > self.num:
                x = round((BREAD.get_value() - random.randint(BREAD.get_value() // 10, BREAD.get_value())))
                self.num += x
                if people_limit.get_value() < self.num:
                    self.num = people_limit.get_value()
                BREAD.decrease(x)
            BREAD.decrease(self.num)
        if BREAD.get_value() == 0:
            Lose(w_or_lose)
            w_or_lose.draw(screen)
            if TICK.get_value() % 500 == 0:
                pygame.quit()

    def get_value(self):
        return self.num


peoples = Peoples(2)
