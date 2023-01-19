import pygame
from buildings import *
from settings import *
import random


class Cell(pygame.sprite.Sprite):
    def __init__(self, group, x, y):
        super().__init__(group)
        type_key = random.randint(1, 1200)
        if type_key % 250 == 0:
            self.im = ass_cell_y_crds[11]
        elif type_key % 200 == 0:
            self.im = ass_cell_y_crds[7]
        elif type_key % 180 == 0:
            self.im = ass_cell_y_crds[random.randint(4, 6)]
        elif type_key % 128 == 0:
            self.im = ass_cell_y_crds[8]
        elif type_key % 38 == 0:
            self.im = ass_cell_y_crds[random.randint(9, 10)]
        else:
            self.im = ass_cell_y_crds[random.randint(0, 3)]
        #   Случайно выбираем ресурсы на клетке и генерируем мир
        self.image = load_image(self.im)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x = x
        self.y = y

    def get_im(self):   # Получение типа клетки
        return self.im

    def type_change(self):  # Смена клетки на клетку без ресурсов
        if self.im not in safe_types:
            self.im = ass_cell_y_crds[random.randint(0, 3)]
            self.image = load_image(self.im)


class Board:
    # создание поля
    def __init__(self, width, height, size):
        self.width = width
        self.height = height
        # значения по умолчанию
        self.left = 0
        self.top = 0
        self.cell_size = size
        self.a_spr = pygame.sprite.Group()

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self):   # Отрисовка поля по клеткам
        for cell_y in range(self.height):
            for cell_x in range(self.width):
                x = self.left + self.cell_size * cell_x
                y = self.top + self.cell_size * cell_y
                Cell(self.a_spr, x, y)
        return self.a_spr

    def get_cell(self, x, y):   # Возможность получить клетку на выбраных координатах
        cell_x = (x // 16) * 16
        cell_y = (y // 16) * 16
        for i in self.a_spr:
            if i.rect.y == cell_y and i.rect.x == cell_x:
                return i

