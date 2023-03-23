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
    grid = [[(0, 0, 0) for x in range(10)] for x in range(20)]

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j, i) in locked_positions:
                c = locked_positions[(j, i)]
                grid[i][j] = c

    return grid

def init_window():
    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption('Tetris')

    return window

def draw_window(surface, grid, score = 0, last_score = 0):
    surface.fill(black)

    # Tetris Title
    font = pygame.font.SysFont('comicsans', 60)
    label = font.render('Tetris', 1, (99, 0, 155))

    surface.blit(label, (top_left_x + max_width / 2 - (label.get_width() / 2), 30))

    font = pygame.font.SysFont('comicsans', 30)
    label = font.render('Score: ' + str(score), 1, (255, 170, 0))

    sx = top_left_x + max_width + 50
    sy = top_left_y + max_height / 2 - 100

    surface.blit(label, (sx + 20, sy + 160))

    # Last score
    label = font.render('Hight Score: ' + str(last_score), 1, (255, 246, 0))
    sx = top_left_x - 200
    sy = top_left_y + 200

    surface.blit(label, (sx + 20, sy + 160))


    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j], (top_left_x + j * 30, top_left_y + i * 30, 30, 30,), 0)

    pygame.draw.rect(surface, grid_background, (top_left_x, top_left_y, max_width, max_height), 5)
    draw_grid(surface, 20, 10)
#pygame.display.update()


def draw_grid(surface, row, col):
    sx = top_left_x
    sy = top_left_y

    for i in range(row):
        pygame.draw.line(surface, white, (sx, sy + i * 30), (sx + max_width, sy + i * 30))

        for j in range(col):
            pygame.draw.line(surface, white, (sx + j * 30, sy), (sx + j * 30, sy + max_height))

def draw_text_middle(surface, text, size, color):
    font = pygame.font.SysFont('comicsans', size, bold=True)
    label = font.render(text, 1, color)

    surface.blit(label, (top_left_x + max_width / 2 - (label.get_width() / 2), top_left_y + max_height / 2 - label.get_height() / 2))

def clear_rows(grid, locked):
    inc = 0

    for i in range(len(grid) -1, -1, -1):
        row = grid[i]
        if (0, 0, 0) not in row:
            inc += 1
            ind = i
            for j in range(len(row)):
                try:
                    del locked[(j, i)]
                except:
                    continue
    if inc > 0:
        for key in sorted(list(locked), key = lambda x: x[1])[::-1]:
            x, y = key
            if y < ind:
                newKey = (x, y + inc)
                locked[newKey] = locked.pop(key)

    return inc # For score


def draw_next_shape(shape, surface):
    font = pygame.font.SysFont('comicsans', 30)
    label = font.render('Next Shape', 1, white)

    sx = top_left_x + max_width + 50
    sy = top_left_y + max_height / 2 - 100

    format = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                pygame.draw.rect(surface, shape.color, (sx + j * 30, sy + i * 30, 30, 30), 0)

    surface.blit(label, (sx + 10, sy - 30))

