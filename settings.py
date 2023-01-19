from useful_func import *

# Параметры окна
TRUE_SIZE = T_W, T_H = 1920, 1024
SIZE = WIDTH, HEIGHT = 1024, 1024
CELL_SIDE = 16
CELL_VERT_NUM = HEIGHT // CELL_SIDE
CELL_HOR_NUM = WIDTH // CELL_SIDE
FPS = 60

# - создание экрана
os.environ['SDL_VIDEO_WINDOW_POS'] = "0,0"
screen = pygame.display.set_mode(TRUE_SIZE, pygame.NOFRAME)

# Настройка картинок
ass_cell_y_crds = ['grass_1.png', 'grass_2.png', 'grass_3.png', 'grass_4.png',
                   'rock_1.png', 'rock_2.png', 'rock_3.png', 'iron.png', 'forest_3.png',
                   'f_s1.png', 'f_s2.png', 'gold_rock.png']

safe_types = ['grass_1.png', 'grass_2.png', 'grass_3.png', 'grass_4.png']

house_types = ['house_1.png', 'house_2.png', 'house_3.png']

sawmill_types = ['sawmill_1.png', 'sawmill_2.png']

rock_types = ['rock_1.png', 'rock_2.png', 'rock_3.png']

fertile_soils = ['f_s1.png', 'f_s2.png']

buttons_types = ['mill_btn.png', 'saw_btn.png', 'fou_btn.png', 'farm_btn.png',
                 'gfou_btn.png', 'house_btn.png', 'mint_frame.png', 'rock_mine.png',
                 'gold_mine_btn.png', 'iron_mine_btn.png']

resources_icons = ['food_icon.png', 'wood_icon.png', 'rock_icon.png', 'iron_icon.png',
                   'money_icon.png', 'wheat_icon.png', 'iron_ore_icon.png', 'gold_icon.png', 'human_icon.png']


# Настройка ресурсов, чит-коды не добавлены
start_money = 100
start_wood = 500
start_stone = 100
start_iron = 100
start_bread = 200
start_wheat = 500
start_iron_ore = 0
start_gold = 0
start_gold_ore = 0
start_house_cap = 10

# Настройка цен для ратуши
first_upgrade_wood = 3000
first_upgrade_stone = 5000
first_upgrade_iron = 300
first_upgrade_people = 1000

second_upgrade_wood = 1000
second_upgrade_stone = 15000
second_upgrade_iron = 2000
second_upgrade_gold = 1500
second_upgrade_money = 20000
second_upgrade_people = 5000
