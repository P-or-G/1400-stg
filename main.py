from cells import Board
from interface import *

pygame.init()

os.environ['SDL_VIDEO_WINDOW_POS'] = "0,0"
screen = pygame.display.set_mode(TRUE_SIZE, pygame.NOFRAME)

board = Board(CELL_HOR_NUM, CELL_VERT_NUM, CELL_SIDE)

all_sprites = board.render()

all_sprites.draw(screen)
all_sprites.update()


buildings = pygame.sprite.Group()

mh = MainHall(buildings, board)


interface = inter()

clock = pygame.time.Clock()

time_count = 0
fl_btn_select = 0
running = True

tr_btn = ''
im_tr = ''
x_tr = ''
y_tr = ''

while running:
    TICK.add(1)
    image = load_image('berater_1.png')
    rect = image.get_rect()
    rect.x = 1024
    rect.y = 16
    if TICK.get_value() == 1000:
        TICK.decrease(999)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
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

    if fl_btn_select == 1:
        tr_btn.rect = (pygame.mouse.get_pos()[0] // 16 * 16, pygame.mouse.get_pos()[1] // 16 * 16)

    clock.tick(FPS)
    screen.fill(pygame.Color('black'))

    all_sprites.draw(screen)
    all_sprites.update()

    buildings.draw(screen)
    buildings.update()

    itr.draw(screen)
    itr.update()

    icn.draw(screen)
    icn.update()

    display([BREAD, WOOD, STONE, IRON, MONEY, WHEAT, IRON_ORE, GOLD_ORE], screen)

    pygame.display.flip()

pygame.quit()
