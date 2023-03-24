import pygame

from src.grid.grid import draw_grid, create_grid, draw_window, init_window, draw_next_shape, clear_rows, draw_text_middle
from src.pieces.shape import get_shape, convert_shape_format, S, Z, I, O, J, L, T
from src.rules.game_rule import valid_space, check_lost, max_score, update_score

def generate_movment(grid, current_piece, next_piece, position_occuped, last_score, locked_position, clock, change_piece, fall_time, level_time, win, score):
    movment = None

    shape = convert_shape_format(current_piece)
    x_current_piece = []
    y_current_piece = []

    for pos in shape:
        x_current_piece.append(pos[0])
        y_current_piece.append(pos[1])

    y_max_current_piece = 0
    y_max_for_x_min = 0
    y_max_for_x_max = 0

    length_current_piece = 0
    x_min_spawn = 0
    x_max_spawn = 0

    if current_piece.shape == S:
            y_max_current_piece = 2
            y_max_for_x_min = 1
            y_max_for_x_max = 2

            length_current_piece = 3
            x_min_spawn = 4
            x_max_spawn = 6

    if current_piece.shape == Z:
            y_max_current_piece = 2
            y_max_for_x_min = 2
            y_max_for_x_max = 1

            length_current_piece = 3
            x_min_spawn = 4
            x_max_spawn = 6

    if current_piece.shape == I:
            y_max_current_piece = 4
            y_max_for_x_min = 4
            y_max_for_x_max = 4

            length_current_piece = 1
            x_min_spawn = 5
            x_max_spawn = 5

    if current_piece.shape == O:
            y_max_current_piece = 2
            y_max_for_x_min = 2
            y_max_for_x_max = 2

            length_current_piece = 2
            x_min_spawn = 4
            x_max_spawn = 5

    if current_piece.shape == J:
            y_max_current_piece = 2
            y_max_for_x_min = 1
            y_max_for_x_max = 2

            length_current_piece = 3
            x_min_spawn = 4
            x_max_spawn = 6

    if current_piece.shape == L:
            y_max_current_piece = 2
            y_max_for_x_min = 2
            y_max_for_x_max = 1

            length_current_piece = 3
            x_min_spawn = 4
            x_max_spawn = 6

    if current_piece.shape == T:
            y_max_current_piece = 2
            y_max_for_x_min = 1
            y_max_for_x_max = 1

            length_current_piece = 3
            x_min_spawn = 4
            x_max_spawn = 6


    x_locked = []
    y_locked = []

    if len(position_occuped) > 0:
        for pos in position_occuped:
            x_locked.append(pos[0])
            y_locked.append(pos[1])

    x_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    height_list = []
    for x in x_list:
        height_list.append(simulate_max_height(y_max_current_piece, 
                            x, 
                            x_locked, 
                            position_occuped, 
                            y_max_for_x_min, 
                            y_max_for_x_max, 
                            length_current_piece))

    min_h = max(height_list)

    while (min(x_current_piece) != min_h or max(x_current_piece) != min_h) and height_list.index(min_h) < 5: 
        shape = convert_shape_format(current_piece)
        x_current_piece = []

        for pos in shape:
            x_current_piece.append(pos[0])

        running = move_shape(grid, current_piece, next_piece, position_occuped, last_score, locked_position, clock, change_piece, fall_time, level_time, pygame.K_LEFT, win, score)
        pygame.time.delay(100)
        if not running:
            return

    while (min(x_current_piece) != min_h or max(x_current_piece) != min_h) and height_list.index(min_h) > 5: 
        shape = convert_shape_format(current_piece)
        x_current_piece = []

        for pos in shape:
            x_current_piece.append(pos[0])

        running = move_shape(grid, current_piece, next_piece, position_occuped, last_score, locked_position, clock, change_piece, fall_time, level_time, pygame.K_RIGHT, win, score)
        pygame.time.delay(100)
        if not running:
            return
    pygame.time.delay(100)

def simulate_max_height(y_max_current_piece, x, x_locked, position_occuped, y_max_for_x_min, y_max_for_x_max, length_current_piece):

    y_linked_to_x = []

    if x in x_locked:
        for pos in position_occuped:
            if pos[0] == x:
                y_linked_to_x.append(pos[1])

        y_max = min(y_linked_to_x)

        match x:
            case 0:
                return y_max - y_max_for_x_min
            
            case 9:
                return y_max - y_max_for_x_max

            case _:
                return y_max - y_max_current_piece
                
    else:
        match x:
            case 0:
                return 20 - y_max_for_x_min
            
            case 9:
                return 20 - y_max_for_x_max

            case _:
                return 20 - y_max_current_piece


def move_shape(grid, current_piece, next_piece, position_occuped, last_score, locked_positions, clock, change_piece, fall_time, level_time, movment, win, score):
    level_time += clock.get_rawtime()

    running = True

    if level_time / 1000 > 5:
        level_time = 0
        if level_time > 0.12:
            level_time -= 0.005


    fall_speed = 0.05

    grid = create_grid(locked_positions)
    fall_time += clock.get_rawtime()
    clock.tick()


    # Piece falling
    if fall_time / 1000 >= fall_speed:
        fall_time = 0
        current_piece.y += 1
        if not (valid_space(current_piece, grid)) and current_piece.y > 0:
            current_piece.y -= 1
            change_piece = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.display.quit()
            quit()

    if movment != None:
        if movment == pygame.K_LEFT:
            current_piece.x -= 1
            if not valid_space(current_piece, grid):
                current_piece.x += 1

        elif movment == pygame.K_RIGHT:
            current_piece.x += 1
            if not valid_space(current_piece, grid):
                current_piece.x -= 1
        
        elif movment == pygame.K_UP: # Rotate shape
            current_piece.rotation = current_piece.rotation + 1 % len(current_piece.shape)
            if not valid_space(current_piece, grid):
                current_piece.rotation = current_piece.rotation - 1 % len(current_piece.shape)

        elif movment == pygame.K_DOWN: # Move down
            current_piece.y += 1
            if not valid_space(current_piece, grid):
                current_piece.y -= 1

    shape_pos = convert_shape_format(current_piece)

    for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1:
                grid[y][x] = current_piece.color

    # If piece hit the ground
    if change_piece:
        for pos in shape_pos:
            p = (pos[0], pos[1])
            locked_positions[p] = current_piece.color
            position_occuped.append(p)
        current_piece = next_piece
        next_piece = get_shape()
        change_piece = False
        score += clear_rows(grid, locked_positions) * 10

    draw_window(win, grid, score, last_score)

    draw_next_shape(next_piece, win)
    pygame.display.update()

    # Check if user lost
    if check_lost(locked_positions):
        draw_text_middle(win, "YOU LOST !", 80, (0, 127, 255))
        pygame.display.update()
        pygame.time.delay(1500)
        running = False
        update_score(score)


    return running




