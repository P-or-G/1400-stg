import pygame
from buildings import *


class Berater:
    def __init__(self, x, y):
        fullname = os.path.join('assets', '3997-font.otf')
        self.font = pygame.font.Font(fullname, 16)
        self.x, self.y = x, y
        self.flags = [True, False, False, False, False, False, False]
        self.ev_count = 0
        self.flag_ret = True

    def change_flag(self, num, new_value):
        self.flags[num] = new_value

    def get_event_flag(self, num):
        return self.flags[num]

    def event(self):
        strings = []
        if self.flags[0]:
            strings.append(self.font.render('Добро пожаловать в ваш город, нажмите пробел, чтобы продолжить',
                                            True, (255, 255, 255)))

            cou = 0
            for i in strings:
                screen.blit(i, (self.x, self.y + 30 * cou))
                cou += 1

            strings = []

            return 0

        elif self.flags[1]:
            strings.append(self.font.render('Для начала разберёмся с интерфейсом. Слева от вас игровое поле.',
                                            True, (255, 255, 255)))
            strings.append(self.font.render('На него вы вольны размещать здания, кнопки для этого даны правее.',
                                            True, (255, 255, 255)))

            cou = 0
            for i in strings:
                screen.blit(i, (self.x, self.y + 30 * cou))
                cou += 1

            strings = []

            return 0

        elif self.flags[2]:
            strings.append(self.font.render('Одно здание уже находится в вашем распоряжении.', True,
                                            (255, 255, 255)))
            strings.append(self.font.render('Это Ратуша - основа вашей игры, вы можете улучшать её по нажатию,', True,
                                            (255, 255, 255)))
            strings.append(self.font.render('но за огромную плату.', True,
                                            (255, 255, 255)))
            strings.append(self.font.render('-----------------------------------------------------', True,
                                            (255, 255, 255)))
            strings.append(self.font.render('Первое улучшение:', True,
                                            (255, 255, 255)))
            strings.append(self.font.render(f'Железо - {first_upgrade_iron}', True,
                                            (255, 255, 255)))
            strings.append(self.font.render(f'Камень - {first_upgrade_stone}', True,
                                            (255, 255, 255)))
            strings.append(self.font.render(f'Дерево - {first_upgrade_wood}', True,
                                            (255, 255, 255)))
            strings.append(self.font.render(f'Люди - {first_upgrade_people}', True,
                                            (255, 255, 255)))
            strings.append(self.font.render('-----------------------------------------------------', True,
                                            (255, 255, 255)))
            strings.append(self.font.render('Второе улучшение:', True,
                                            (255, 255, 255)))
            strings.append(self.font.render(f'Железо - {second_upgrade_iron}', True,
                                            (255, 255, 255)))
            strings.append(self.font.render(f'Камень - {second_upgrade_stone}', True,
                                            (255, 255, 255)))
            strings.append(self.font.render(f'Дерево - {second_upgrade_wood}', True,
                                            (255, 255, 255)))
            strings.append(self.font.render(f'Люди - {second_upgrade_people}', True,
                                            (255, 255, 255)))
            strings.append(self.font.render(f'Золото - {second_upgrade_gold}', True,
                                            (255, 255, 255)))
            strings.append(self.font.render(f'Деньги - {second_upgrade_money}', True,
                                            (255, 255, 255)))

            cou = 0
            for i in strings:
                screen.blit(i, (self.x, self.y + 30 * cou))
                cou += 1

            strings = []

            return 0

        elif self.flags[3]:
            strings.append(self.font.render('Кстати о ресурсах, все они производятся зданиями.',
                                            True, (255, 255, 255)))
            strings.append(self.font.render('Такие, как еда тратят другой ресурс при производстве (пшеница)',
                                            True, (255, 255, 255)))
            strings.append(self.font.render('Здания, которые производят такие ресурсы (1 порядка) ставятся на ресурс',
                                            True, (255, 255, 255)))
            strings.append(self.font.render('Посмотрите на карту, там, на плодородной почве появилось поле пшеницы.',
                                            True, (255, 255, 255)))

            cou = 0
            for i in strings:
                screen.blit(i, (self.x, self.y + 30 * cou))
                cou += 1

            strings = []

            if self.flag_ret:
                self.flag_ret = False
                return 3
            return 0

        elif self.flags[4]:
            strings.append(self.font.render('Прошу заметить, хотя вы видите все кнопки со зданиями,',
                                            True, (255, 255, 255)))
            strings.append(self.font.render('Вы не можете ставить здания связанные с золотом до 2 ур ратуши',
                                            True, (255, 255, 255)))

            cou = 0
            for i in strings:
                screen.blit(i, (self.x, self.y + 30 * cou))
                cou += 1

            strings = []

            return 0

        elif self.flags[5]:
            strings.append(self.font.render('Также есть особый ресурс - люди,',
                                            True, (255, 255, 255)))
            strings.append(self.font.render('Они каждую секунду потребляют 1 единицу еды, каждый,',
                                            True, (255, 255, 255)))
            strings.append(self.font.render('А ещё постоянно приходят и рождаются, потребляя при этом 10 еды.',
                                            True, (255, 255, 255)))
            strings.append(self.font.render('Причём они могут прийти, съесть еду, но в домах не хватит места на всех',
                                            True, (255, 255, 255)))
            strings.append(self.font.render('Тогда лишние уйдут, а еду никто не вернёт :(',
                                            True, (255, 255, 255)))
            strings.append(self.font.render('А если еда кончится, то все люди покинут город, вы проиграете',
                                            True, (255, 255, 255)))

            cou = 0
            for i in strings:
                screen.blit(i, (self.x, self.y + 30 * cou))
                cou += 1

            strings = []

            return 0

        elif self.flags[6]:
            strings.append(self.font.render('А чтобы выиграть вы должны построить третью ратушу',
                                            True, (255, 255, 255)))
            strings.append(self.font.render('На этом рекомендации вашего советника кончаются, все они записаны',
                                            True, (255, 255, 255)))
            strings.append(self.font.render('Листать их можно на пробел',
                                            True, (255, 255, 255)))

            cou = 0
            for i in strings:
                screen.blit(i, (self.x, self.y + 30 * cou))
                cou += 1

            strings = []

            return 0