from buildings import *
from menu import Button

itr = pygame.sprite.Group()
icn = pygame.sprite.Group()


# Класс Icon упрощает создание множества иконок
class Icon(pygame.sprite.Sprite):
    def __init__(self, group, im, x, y):
        super().__init__(group)
        self.group = group
        self.type = im
        self.image = load_image(im)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


# Выводит иконки и кол-во ресурсов
def display(resources, sc):
    cou = 0
    fullname = os.path.join('assets', 'ARCADECLASSIC.TTF')
    font = pygame.font.Font(fullname, 16)
    for res in resources:
        cou += 1
        y = 32 * cou
        Icon(icn, resources_icons[cou - 1], 1030, y)
        t = font.render(str(res.get_value()), True, (255, 255, 255))
        sc.blit(t, (1070, y))


# Создаёт сетку кнопок
def inter():
    cou = 0
    for i in range(2):
        for j in range(5):
            Button(itr, buttons_types[cou], 1024 + i * 37, 512 + j * 37)
            cou += 1

