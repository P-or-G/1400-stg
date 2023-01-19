from buildings import *


# Ниже класс советника, он последовательно выводит на экран разные фразы для обучения, а также воспроизводит озвучку
class Berater:
    def __init__(self, x, y):
        fullname = os.path.join('assets', '3997-font.otf')
        self.font = pygame.font.Font(fullname, 16)
        self.x, self.y = x, y
        self.flags = [True, False, False, False, False, False, False, False]
        self.ev_count = 0
        self.flag_ret = True
        self.first_sound_play = [True, True, True, True, True, True, True, True, True, True]

    def change_flag(self, num, new_value):
        self.flags[num] = new_value

    def set_normal(self):
        self.flags = [True, False, False, False, False, False, False, False]

    def get_event_flag(self, num):
        return self.flags[num]

    def event(self):
        strings = []
        if self.flags[0]:
            if self.first_sound_play[0]:
                queue.play_sound('sounds/1_slide.wav')
                self.first_sound_play[0] = False
            strings.append(self.font.render('Добро пожаловать в ваш город, нажмите пробел, чтобы продолжить',
                                            True, (255, 255, 255)))

            cou = 0
            for i in strings:
                screen.blit(i, (self.x, self.y + 30 * cou))
                cou += 1

            strings = []

            return 0

        elif self.flags[1]:
            if self.first_sound_play[1]:
                queue.play_sound('sounds/2_slide.wav')
                self.first_sound_play[1] = False
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
            if self.first_sound_play[2]:
                queue.play_sound('sounds/3_slide.wav')
                self.first_sound_play[2] = False
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

            if self.first_sound_play[4]:
                delay = queue.play_sound('sounds/4_slide_1.wav')
                self.first_sound_play[4] = False
                pygame.time.delay(round(delay * 1000))
            if self.first_sound_play[5]:
                queue.play_sound('sounds/4_slide_2.wav')
                self.first_sound_play[5] = False

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
            if self.first_sound_play[6]:
                queue.play_sound('sounds/5_slide.wav')
                self.first_sound_play[6] = False
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
            if self.first_sound_play[7]:
                queue.play_sound('sounds/6_slide.wav')
                self.first_sound_play[7] = False
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
            if self.first_sound_play[8]:
                queue.play_sound('sounds/slide_7_1.wav')
                self.first_sound_play[8] = False
            if self.first_sound_play[9]:
                queue.play_sound('sounds/slide_7_2.wav')
                self.first_sound_play[9] = False
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

        elif self.flags[7]:
            strings.append(self.font.render('Далее приведена стоимость зданий',
                                            True, (255, 255, 255)))
            strings.append(self.font.render('Мельница:',
                                            True, (255, 255, 255)))
            strings.append(self.font.render('   Дерево - 250',
                                            True, (255, 255, 255)))
            strings.append(self.font.render('   Пшеница - 100',
                                            True, (255, 255, 255)))
            strings.append(self.font.render('Ферма:',
                                            True, (255, 255, 255)))
            strings.append(self.font.render('   Дерево - 100',
                                            True, (255, 255, 255)))
            strings.append(self.font.render('Лесопилка:',
                                            True, (255, 255, 255)))
            strings.append(self.font.render('   Пшеница - 200',
                                            True, (255, 255, 255)))
            strings.append(self.font.render('   Камень - 10',
                                            True, (255, 255, 255)))
            strings.append(self.font.render('Каменоломня:',
                                            True, (255, 255, 255)))
            strings.append(self.font.render('   Дерево - 250',
                                            True, (255, 255, 255)))
            strings.append(self.font.render('   Пшеница - 150',
                                            True, (255, 255, 255)))
            strings.append(self.font.render('Каменоломня = Железный рудник = Золотой Рудник:',
                                            True, (255, 255, 255)))
            strings.append(self.font.render('   Дерево - 250',
                                            True, (255, 255, 255)))
            strings.append(self.font.render('   Пшеница - 150',
                                            True, (255, 255, 255)))
            strings.append(self.font.render('Жилой дом:',
                                            True, (255, 255, 255)))
            strings.append(self.font.render('   Дерево - 50',
                                            True, (255, 255, 255)))
            strings.append(self.font.render('   Камень - 20 (Со второго уровня ратуши)',
                                            True, (255, 255, 255)))
            strings.append(self.font.render('Плавильня для железа:',
                                            True, (255, 255, 255)))
            strings.append(self.font.render('   Дерево - 200',
                                            True, (255, 255, 255)))
            strings.append(self.font.render('   Камень - 300',
                                            True, (255, 255, 255)))
            strings.append(self.font.render('   Пшеница - 100',
                                            True, (255, 255, 255)))
            strings.append(self.font.render('Плавильня для золота:',
                                            True, (255, 255, 255)))
            strings.append(self.font.render('   Дерево - 300',
                                            True, (255, 255, 255)))
            strings.append(self.font.render('   Камень - 500',
                                            True, (255, 255, 255)))
            strings.append(self.font.render('   Пшеница - 100',
                                            True, (255, 255, 255)))
            strings.append(self.font.render('Монетный двор:',
                                            True, (255, 255, 255)))
            strings.append(self.font.render('   Дерево - 500',
                                            True, (255, 255, 255)))
            strings.append(self.font.render('   Камень - 500',
                                            True, (255, 255, 255)))

            cou = 0
            for i in strings:
                screen.blit(i, (self.x, self.y + 30 * cou))
                cou += 1

            strings = []

            return 0


ber = Berater(1150, 100)
