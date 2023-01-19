from useful_func import *


class Button(pygame.sprite.Sprite):
    def __init__(self, group, im, x, y, name='name'):
        super().__init__(group)
        self.name = name
        self.type = im
        self.image = load_image(im)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def select(self, x, y):     # Проверяет то, что координаты лежат внутри точки
        if self.rect.x <= x <= self.rect.x + self.image.get_width() and \
                self.rect.y <= y <= self.rect.y + self.image.get_height():
            return True
        return False


# Сделана, чтобы не нагружать main кодом
def menu_init(image, screen_num):
    button_group = pygame.sprite.Group()
    if screen_num == 0:
        Button(button_group, 'easy_btn.png', 832, 500, name='easy')
        Button(button_group, 'hard_btn.png', 832, 580, name='hard')
    else:
        Button(button_group, 'start_game_button.png', 832, 500)

    menu_group = pygame.sprite.Group()
    menu = pygame.sprite.Sprite()
    menu.image = load_image(image)
    menu.rect = (0, 0)
    menu_group.add(menu)
    return menu_group, button_group
