from settings import *
import random


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
TICK = Resource(0)

people_limit = Resource(10)


class Peoples:
    global people_limit

    def __init__(self, num):
        self.num = num

    def update(self):
        if TICK.get_value() % 200 == 0:
            if people_limit.get_value() > self.num:
                x = round((BREAD.get_value() - random.randint(BREAD.get_value() // 10, BREAD.get_value())))
                self.num += x
                if people_limit.get_value() < self.num:
                    self.num = people_limit.get_value()
                BREAD.decrease(x)

        if TICK.get_value() % 100 == 0:
            BREAD.decrease(self.num)
        if BREAD.get_value() == 0:
            print(x // 0)

    def get_value(self):
        return self.num


peoples = Peoples(2)
