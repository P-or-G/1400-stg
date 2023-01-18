import pygame

from cells import Board
from interface import *
from Berater import Berater


board = Board(CELL_HOR_NUM, CELL_VERT_NUM, CELL_SIDE)

all_sprites = board.render()

all_sprites.draw(screen)
all_sprites.update()

buildings = pygame.sprite.Group()

mh = MainHall(buildings, board)

ber = Berater(1150, 100)

interface = inter()

time_count = 0
fl_btn_select = 0
running = True

tr_btn = ''
im_tr = ''
x_tr = ''
y_tr = ''
cou = 0
while running:
    if pause.value:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_p]:
                    pause.change()
    else:
        cou += 1
        image = load_image('berater_1.png')
        rect = image.get_rect()
        rect.x = 1024
        rect.y = 16
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_p:
                    pause.change()
                if event.key == pygame.K_SPACE:
                    for fl in range(len(ber.flags)):
                        if ber.get_event_flag(fl):
                            ber.change_flag(fl, False)
                            try:
                                ber.change_flag(fl + 1, True)
                            except:
                                ber.set_normal()
                            break
                if event.key == pygame.K_1:
                    queue.play_sound('sounds/1_slide.wav')
                if event.key == pygame.K_2:
                    queue.play_sound('sounds/2_slide.wav')
                if event.key == pygame.K_3:
                    queue.play_sound('sounds/3_slide.wav')
                if event.key == pygame.K_4:
                    queue.play_sound('sounds/4_slide_1.wav')
                if event.key == pygame.K_5:
                    queue.play_sound('sounds/4_slide_2.wav')
                if event.key == pygame.K_6:
                    queue.play_sound('sounds/5_slide.wav')
                if event.key == pygame.K_7:
                    queue.play_sound('sounds/6_slide.wav')
                if event.key == pygame.K_8:
                    queue.play_sound('sounds/slide_7_1.wav')
                if event.key == pygame.K_9:
                    queue.play_sound('sounds/slide_7_2.wav')

            if event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()

                if fl_btn_select == 0:

                    for btn in itr:
                        if btn.select(x, y):

                            x_tr = btn.rect.x
                            y_tr = btn.rect.y
                            im_tr = btn.type
                            tr_btn = btn
                            fl_btn_select = 1

                elif fl_btn_select == 1:
                    if pygame.mouse.get_pos()[0] < 1024 - 16:
                        fl_btn_select = 0
                        button_building_connect(buildings, board, pygame.mouse.get_pos()[0] // 16 * 16,
                                                pygame.mouse.get_pos()[1] // 16 * 16, im_tr)
                        tr_btn.kill()
                        Button(itr, im_tr, x_tr, y_tr)
                    else:
                        fl_btn_select = 0
                        tr_btn.kill()
                        Button(itr, im_tr, x_tr, y_tr)

                x, y = pygame.mouse.get_pos()
                mh.select(x, y)

        if fl_btn_select == 1:
            tr_btn.rect = (pygame.mouse.get_pos()[0] // 16 * 16, pygame.mouse.get_pos()[1] // 16 * 16)

        clock.tick(FPS)
        screen.fill(pygame.Color('black'))

        all_sprites.draw(screen)
        icn.draw(screen)
        itr.draw(screen)
        buildings.draw(screen)
        display([BREAD, WOOD, STONE, IRON, MONEY, WHEAT, IRON_ORE, GOLD_ORE, peoples], screen)
        w_or_lose.draw(screen)

        x = ber.event()
        if x != 0:
            if x == 3:
                prod_mod = 0
                while True:
                    x, y = random.randrange(0, WIDTH - 16, 16), random.randrange(0, HEIGHT - 16, 16)
                    if Ferma(buildings, board, x, y).flag:
                        WOOD.add(100)
                        Ferma(buildings, board, x, y)
                        break

        if cou >= clock.get_fps():
            all_sprites.update()
            itr.update()
            icn.update()
            peoples.update()
            buildings.update()

            cou = 0

        pygame.display.flip()

pygame.quit()
