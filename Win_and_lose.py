import pygame
from settings import load_image


w_or_lose = pygame.sprite.Group()


class Lose(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.image = load_image('lose_screen.png')
        self.rect = self.image.get_rect()
        self.rect.x = 791
        self.rect.y = 0


class Win(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.image = load_image('win_screen.png')
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
