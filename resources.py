import random

from settings import *
import pygame


class StoneVein(pygame.sprite.Sprite):
    def __init__(self):
        self.width =
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = random.randrange(0, WIDTH, 16)
        self.top = random.randrange(0, WIDTH, 16)
        self.cell_size = size
