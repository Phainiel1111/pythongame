import pygame,pygame_menu

pygame.init()
surface = pygame.display.set_mode((800, 600)) #designer

def main_game():
    pass


def load_game():
    pass

def start_the_game():
    menu.clear()
    menu.add_text_input('Tên người chơi :', default='Player')
    menu.add_button('OK', main_game)
    menu.add_button('Return', main_menu)


def help_game():
    menu.clear()
    menu.add_button('Return', main_menu)


def main_menu():
    menu.clear()
    menu.add_button('Play', start_the_game)
    menu.add_button('Load', load_game)
    menu.add_button('Help', help_game)
    menu.add_button('Quit', pygame_menu.events.EXIT)

menu = pygame_menu.Menu(600, 800, 'Welcome',
                       theme=pygame_menu.themes.THEME_ORANGE) #designer
main_menu()


menu.mainloop(surface)
