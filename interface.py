import pygame
from random import randint
from settings import *
from buildings import *


class Button(pygame.sprite.Sprite):
    def __init__(self, group, building):
        self