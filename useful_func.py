import pygame
import os
import sys
import random


# Инициализация проходит тут для корректной работы всех функций
# Также из этого файла во всю программу подгружаются библиотеки

pygame.init()
clock = pygame.time.Clock()
pygame.font.init()


class SoundQueue:   # Класс создан для приостановки предыдущего звука при использовании play_sound
    def __init__(self):
        self.sound = pygame.mixer.Sound('sounds/1_slide.wav')

    def play_sound(self, name):
        self.sound.stop()
        self.sound = pygame.mixer.Sound(name)
        self.sound.play()
        return self.sound.get_length()


def load_image(name, colorkey=None):    # Функция взята из урока, загружает изображение из папки assets по названию
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


class Pause:    # Класс реализован для простой работы с паузой в игре
    def __init__(self):
        self.value = False

    def change(self):
        if self.value:
            self.value = False
        else:
            self.value = True


queue = SoundQueue()
pause = Pause()     # - Сразу создаём переменные с классами для дальнейшего использования
