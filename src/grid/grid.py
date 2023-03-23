import pygame

window_height = 800
window_width = 700

max_height = 600
max_width = 300

block_size = 30

top_left_x = (window_width - max_width) // 2
top_left_y = window_height - max_height

surface = pygame.display.set_mode((max_width, max_height))
grid_background = (199, 0, 55)

white = (200, 200, 200)
black = (0, 0, 0)

pygame.font.init()

def create_grid(locked_positions={}):
    grid = [[(0, 0, 0) for i in range(10)] for j in range(20)]

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (i, j) in locked_positions:
                c = locked_positions[(i, j)]
                grid[i][j] = c

    return grid

def init_window():
    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption('Tetris')

    return window

def draw_window(grid):
    surface.fill(black)

    # Tetris Title
    font = pygame.font.SysFont('comicsans', 60)
    label = font.render('Tetris', 1, (99, 0, 155))

    surface.blit(label, (top_left_x + max_width / 2 - (label.get_width() / 2), 30))

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j], (top_left_x + j * 30, top_left_y + i * 30, 30, 30,), 0)

    draw_grid(surface, 20, 10)
    pygame.draw.rect(surface, grid_background, (top_left_x, top_left_y, max_width, max_height), 5)
    pygame.display.update()


def draw_grid(surface, row, col):
    sx = top_left_x
    sy = top_left_y

    for i in range(row):
        pygame.draw.line(surface, white, (sx, sy + i * 30), (sx + max_width, sy + i * 30))

        for j in range(col):
            pygame.draw.line(surface, white, (sx + j * 30, sy), (sx + j * 30, sy + max_height))
