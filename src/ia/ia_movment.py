import pygame

from src.rules.game_rule import valid_space
from src.pieces.shape import convert_shape_format

def get_y_for_x_min(x_current_piece, y_current_piece, shape):
    y_for_x_min = []

    for pos in shape:
        if pos[0] == min(x_current_piece):
            y_for_x_min.append(pos[1])

    max_y_for_x_min = min(y_for_x_min)

    return max(y_current_piece) - max_y_for_x_min + 1

def get_y_for_x_max(x_current_piece, y_current_piece, shape):
    y_for_x_max = []

    for pos in shape:
        if pos[0] == max(x_current_piece):
            y_for_x_max.append(pos[1])

    max_y_for_x_max = min(y_for_x_max)

    return max(y_current_piece) - max_y_for_x_max + 1
        

def generate_movment(grid, current_piece, next_piece, position_occuped):
    movment = None

    shape = convert_shape_format(current_piece)
    x_current_piece = []
    y_current_piece = []

    for pos in shape:
        x_current_piece.append(pos[0])
        y_current_piece.append(pos[1])

    y_max_current_piece = max(y_current_piece) - min(y_current_piece) + 1
    y_max_for_x_min = get_y_for_x_min(x_current_piece, y_current_piece, shape)
    y_max_for_x_max = get_y_for_x_max(x_current_piece, y_current_piece, shape)

    length_current_piece = max(x_current_piece) - min(x_current_piece) + 1

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

    print(height_list)

    pygame.time.delay(100)


    return movment

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
            
            case 1:
                if length_current_piece > x:
                    return y_max - y_max_for_x_min

            case 2:
                if length_current_piece > x:
                    return y_max - y_max_for_x_min

            case 3:
                if length_current_piece > x:
                    return y_max - y_max_for_x_min
                    
            case 4:
                if length_current_piece > x:
                    return y_max - y_max_for_x_min

            case 5:
                if 9 - length_current_piece < x:
                    return y_max - y_max_for_x_max

            case 6:
                if 9 - length_current_piece < x:
                    return y_max - y_max_for_x_max

            case 7:
                if 9 - length_current_piece < x:
                    return y_max - y_max_for_x_max

            case 8:
                if 9 - length_current_piece < x:
                    return y_max - y_max_for_x_max

            case 9:
                return y_max - y_max_for_x_max

            case _:
                return y_max - y_max_current_piece
                
    else:
        match x:
            case 0:
                return 20 - y_max_for_x_min
            
            case 1:
                if length_current_piece > x:
                    return 20 - y_max_for_x_min

            case 2:
                if length_current_piece > x:
                    return 20 - y_max_for_x_min

            case 3:
                if length_current_piece > x:
                    return 20 - y_max_for_x_min
                    
            case 4:
                if length_current_piece > x:
                    return 20 - y_max_for_x_min

            case 5:
                if 9 - length_current_piece < x:
                    return 20 - y_max_for_x_max

            case 6:
                if 9 - length_current_piece < x:
                    return 20 - y_max_for_x_max

            case 7:
                if 9 - length_current_piece < x:
                    return 20 - y_max_for_x_max

            case 8:
                if 9 - length_current_piece < x:
                    return 20 - y_max_for_x_max

            case 9:
                return 20 - y_max_for_x_max

            case _:
                return 20 - y_max_current_piece













