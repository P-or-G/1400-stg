import pygame

if __name__ == '__main__':
    pygame.init()
    size = width, height = 300, 200
    screen = pygame.display.set_mode(size)
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
