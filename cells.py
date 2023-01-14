import pygame
from buildings import *


class Cell(pygame.sprite.Sprite):
    def __init__(self, group, x, y):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно !!!
        super().__init__(group)
        type_key = random.randint(1, 1000)
        if type_key % 300 == 0:
            self.im = ass_cell_y_crds[5]
        elif type_key % 200 == 0:
            self.im = ass_cell_y_crds[4]
        else:
            self.im = ass_cell_y_crds[random.randint(0, 3)]
        self.image = load_image(self.im)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, *args, **kwargs):
        pass

    def get_im(self):
        return self.im


class Board:
    # создание поля
    def __init__(self, width, height, size):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 0
        self.top = 16
        self.cell_size = size

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self):
        self.a_spr = pygame.sprite.Group()

        for cell_y in range(self.height):
            for cell_x in range(self.width):
                x = self.left + self.cell_size * cell_x
                y = self.top + self.cell_size * cell_y
                Cell(self.a_spr, x, y)
        return self.a_spr

    def get_cell(self, x, y):
        cell_x = x // 16 * 16
        cell_y = y // 16 * 16
        cou = 0
        for i in self.a_spr:
            if i.rect.y == cell_y and i.rect.x == cell_x:
                return i
