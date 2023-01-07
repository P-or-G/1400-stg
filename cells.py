import pygame
from random import randint
from settings import *
from buildings import *


class Cell(pygame.sprite.Sprite):
    def __init__(self, group, img, x, y):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно !!!
        super().__init__(group)
        self.image = load_image(img)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, *args, **kwargs):
        pass

class Board:
    # создание поля
    def __init__(self, width, height, size):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 0
        self.top = 0
        self.cell_size = size

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self):
        a_spr = pygame.sprite.Group()
        for cell_y in range(self.height):
            for cell_x in range(self.width):
                x = self.left + self.cell_size * cell_x
                y = self.top + self.cell_size * cell_y
                Cell(a_spr, ass_cell_y_crds[randint(0, 3)], x, y)

        return a_spr
