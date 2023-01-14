from settings import *


class Resource:
    def __init__(self, num):
        self.value = num

    def add(self, num):
        self.value += num

    def decrease(self, num):
        if self.value - num >= 0:
            self.value -= num
        else:
            return False

    def get_value(self):
        return self.value


BREAD = Resource(start_bread)
WOOD = Resource(start_wood)
STONE = Resource(start_stone)
IRON = Resource(start_iron)
MONEY = Resource(start_money)
WHEAT = Resource(0)
IRON_ORE = Resource(0)
GOLD_ORE = Resource(0)