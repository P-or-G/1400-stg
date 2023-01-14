import pygame
from random import randint
from settings import *
from buildings import *


class Button(pygame.sprite.Sprite):
    def __init__(self, group, im, x, y):
        super().__init__(group)
        self.type = im
        self.image = load_image(im)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def select(self, x, y):
        if self.rect.x <= x <= self.rect.x + 32 and self.rect.y <= y <= self.rect.y + 32:
            return True
        return False
