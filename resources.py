from settings import *
import random
from Win_and_lose import w_or_lose, Lose, Win


# Все ресурсы, кроме людей, работают одинаково
class Resource:
    def __init__(self, num):    # Создаём объект с n ресурсов
        self.value = num

    def add(self, num):     # Добавляем n ресурсов
        self.value += num

    def decrease(self, num, bl=False):
        # Убираем n ресурсов, bl - принимает True / False для игнорирования отрицательных чисел
        if self.value - num >= 0 or bl:
            self.value -= num
        else:
            return False

    def set_zero(self):     # Ставим кол-во ресурсов на 0
        self.value = 0

    def get_value(self):    # Получаем кол-во ресурсов
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
#   Создаём ресурсы, используя настройку в settings.py


class Peoples:
    global people_limit

    def __init__(self, num):
        self.num = num
        self.cou = 0

    def update(self):
        self.cou += 1
        if self.cou % 3 == 0:
            self.cou = 0
            if people_limit.get_value() > self.num:     # Приход новых людей
                x = round((BREAD.get_value() - random.randint(BREAD.get_value() // 10, BREAD.get_value())))
                self.num += (x // 10) + 1
                if people_limit.get_value() < self.num:
                    self.num = people_limit.get_value()
                BREAD.decrease(x)
            if difficulty.dif == 'easy':    # Постоянное потребление еды в зависимости от сложности
                BREAD.decrease(self.num)
            else:
                BREAD.decrease(self.num * 2)
        if BREAD.get_value() == 0:  # Проверка на поражение
            Lose(w_or_lose)
            w_or_lose.draw(screen)
            pause.change()

    def get_value(self):
        return self.num


peoples = Peoples(2)
