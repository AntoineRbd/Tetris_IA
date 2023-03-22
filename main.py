import pygame

from src.grid.grid import draw_grid

if __name__ == "__main__":
    pygame.init()
    clock = pygame.time.Clock()


    while True:
        draw_grid()

        pygame.display.update()
