import pygame
from random import randint
from settings import *
import os
import sys
from buildings import *


def load_image(name):
    fullname = os.path.join('assets', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


pygame.init()
screen = pygame.display.set_mode(SIZE)


class Cell(pygame.sprite.Sprite):
    def __init__(self, group, img, x, y):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно !!!
        super().__init__(group)
        self.image = load_image(img)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


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

        MainHall(a_spr, 160, 320)
        return a_spr


board = Board(CELL_HOR_NUM, CELL_VERT_NUM, CELL_SIDE)
all_sprites = board.render()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(pygame.Color('black'))

    all_sprites.draw(screen)

    pygame.display.flip()

pygame.quit()
