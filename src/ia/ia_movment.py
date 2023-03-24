import pygame

from src.rules.game_rule import valid_space
from src.pieces.shape import convert_shape_format

def generate_movment(grid, current_piece, next_piece, position_occuped):
    movment = None

    x_locked = []
    y_locked = []


    shape = convert_shape_format(current_piece)
    x_curruent_piece = []
    y_curruent_piece = []

    for pos in shape:
        x_curruent_piece.append(pos[0])
        y_curruent_piece.append(pos[0])

    x_max_current_piece = max(x_curruent_piece) - min(x_curruent_piece)

    if len(position_occuped) > 0:
        for pos in position_occuped:
            x_locked.append(pos[0])
            y_locked.append(pos[1])

    if len(y_locked) > 0:
        max_y_locked = min(y_locked)
    else:
        max_y_locked = 20

    for x in x_curruent_piece:
        for pos in position_occuped:
            x_lock = pos[0]
            y_lock = pos[1]

            if x == x_lock and x_max_current_piece not in x_locked:
                movment = pygame.K_LEFT

                pygame.time.delay(100)
                return movment
                
            if x == x_lock and x_max_current_piece in x_locked:
                movment = pygame.K_RIGHT

                pygame.time.delay(100)
                return movment

            if y_lock == max_y_locked:
                movment = pygame.K_RIGHT

                pygame.time.delay(100)
                return movment

            

    pygame.time.delay(100)

    return movment
