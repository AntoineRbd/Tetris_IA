import pygame

from src.grid.grid import draw_text_middle, init_window
from src.rules.game import main
from src.ia.ia import ia_play

pygame.font.init()


def main_menu(win):
    running = True
    
    while running:
        win.fill((0, 0, 0))
        draw_text_middle(win, 'Press Any Key To Play', 60, (255, 255, 255))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                main(win)

if __name__ == "__main__":
    win = init_window()

    # Play yourself
    main_menu(win)

    # Play IA
#ia_play(win)


