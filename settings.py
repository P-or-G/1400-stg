import os
import sys
import pygame
import random

# - Window options
SIZE = WIDTH, HEIGHT = 512, 512
CELL_SIDE = 16
CELL_VERT_NUM = HEIGHT // CELL_SIDE
CELL_HOR_NUM = WIDTH // CELL_SIDE
FPS = 60

# - Sprites options
ass_cell_y_crds = ['grass_1.png', 'grass_2.png', 'grass_3.png', 'grass_4.png']
hall_crds = random.randrange(0, WIDTH, 16), random.randrange(0, HEIGHT, 16)

# - Gameplay options
start_money = 100
start_wood = 50
start_stone = 25
start_iron = 10

# - Useful functions
def load_image(name, colorkey=None):
    fullname = os.path.join('assets', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image

