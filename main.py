import pygame
from settings import *


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

    def render(self, screen):
        for cell_y in range(self.height):
            for cell_x in range(self.width):
                x = self.left + self.cell_size * cell_x
                y = self.top + self.cell_size * cell_y
                if self.board[cell_y][cell_x]:
                    pygame.draw.rect(screen, pygame.Color('white'), (x, y, self.cell_size, self.cell_size), width=0)
                else:
                    pygame.draw.rect(screen, pygame.Color('white'), (x, y, self.cell_size, self.cell_size), width=1)


if __name__ == '__main__':
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
