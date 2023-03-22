import pygame

max_height = 800
max_width = 400

screen = pygame.display.set_mode((max_width, max_height))
grid_backgound = (70,130,180)

white = (200, 200, 200)
black = (0, 0, 0)

def draw_grid():
    block_size = 40

    screen.fill(grid_backgound)
    pygame.display.set_caption('Tetris')

    icon = pygame.image.load('assets/logo.png')
    pygame.display.set_icon(icon)

    for i in range(0, max_width, block_size):
        for j in range(0, max_height, block_size):
            rect = pygame.Rect(i, j, block_size, block_size)
            pygame.draw.rect(screen, black, rect, 1)
