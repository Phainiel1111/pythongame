import pygame, pygame_menu

pygame.init()
surface = pygame.display.set_mode((800, 600))

# Menu Music
pygame.mixer.init() 
pygame.mixer.music.load('menumusic.wav') 
pygame.mixer.music.play(-1, 0.0)

# Sound
click01 = pygame.mixer.Sound('click.wav')

# Title and Icon
pygame.display.set_caption("Game dua xe")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

def bat_dau():
    pass
    click01.play()


def main_game():
    menu.clear()
    menu.add_button('Trường đua số 1',map1_game)
    menu.add_button('Trường đua số 2',map2_game)
    menu.add_button('Trường đua số 3',map3_game)
    menu.add_button('Quay lại',load_game)
    click01.play()

def map1_game():
    menu.clear()
    menu.add_selector('Xe:', [(' số 1', 1), (' số 2', 2),(' số 3',3),(' số 4',4),(' số 5',5)], onchange=so_xe)
    menu.add_button('OK',bat_dau)
    menu.add_button('Quay lai',main_game)
    click01.play()

def map2_game():
    menu.clear()
    menu.add_selector('Xe:', [(' số 1', 1), (' số 2', 2),(' số 3',3),(' số 4',4),(' số 5',5)], onchange=so_xe)
    menu.add_button('OK',bat_dau)
    menu.add_button('Quay lai',main_game)
    click01.play()

def map3_game():
    menu.clear()
    menu.add_selector('Xe:', [(' số 1', 1), (' số 2', 2),(' số 3',3),(' số 4',4),(' số 5',5)], onchange=so_xe)
    menu.add_button('OK',bat_dau)
    menu.add_button('Quay lai',main_game)
    click01.play()

def nap_game():
    pass
    click01.play()

def so_xe(xe,value):
    pass
    click01.play()

def load_game():
    menu.clear()
    menu.add_button('Chọn trường đua',main_game)
    menu.add_button('Nap tien',nap_game)
    menu.add_button('Quay lại',main_menu)
    click01.play()

def start_the_game():
    menu.clear()
    menu.add_text_input('Tên người chơi :', default=' ')
    menu.add_button('Bắt đầu', load_game)
    menu.add_button('Quay lại', main_menu)
    click01.play()

def help_game():
    menu.clear()
    menu.add_button('Quay lại', main_menu)
    click01.play()

def main_menu():
    menu.clear()
    menu.add_button('Chơi mới', start_the_game)
    menu.add_button('Chơi tiếp', load_game)
    menu.add_button('Giúp đỡ', help_game)
    menu.add_button('Thoát', pygame_menu.events.EXIT)
    click01.play()

menu = pygame_menu.Menu(600, 800, 'Chào mừng đến với ??? ',
                       theme=pygame_menu.themes.THEME_ORANGE)
main_menu()


menu.mainloop(surface)
