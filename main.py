import pygame

if __name__ == '__main__':
    pygame.init()
    size = width, height = 300, 200
    screen = pygame.display.set_mode(size)
    y1, y2, y3, y4 = 0, 15, 15, 0
    pygame.draw.polygon(screen, pygame.Color("white"), [(0, 0), (0, 200), (300, 200), (300, 0)])
    for i in range((200 // 17) + 1):
        if i % 2 == 0:
            x1, x2, x3, x4 = 0, 0, 30, 30
        else:
            x1, x2, x3, x4 = -15, -15, 15, 15
        for j in range((300 // 32) + 1):
            pygame.draw.polygon(screen, pygame.Color("red"), [(x1, y1), (x2, y2), (x3, y3), (x4, y4)])
            x1 += 32
            x2 += 32
            x3 += 32
            x4 += 32
        y1 += 17
        y2 += 17
        y3 += 17
        y4 += 17
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
