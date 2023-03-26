import pygame

from src.pieces.shape import convert_shape_format, Piece, S, Z, I, O, J, L, T
from src.rules.game_rule import valid_space

bests_moves = []
shape_already_moved = False

def generate_movment(grid, current_piece, next_piece, position_occuped, change_piece):
    movment = None

    global shape_already_moved
    global bests_moves

    if len(bests_moves) == 0 and not change_piece and not shape_already_moved:
        accepted_positions = [[(j, i) for j in range(10) if grid[i][j] == (0, 0, 0)] for i in range(20)]
        accepted_positions = [j for sub in accepted_positions for j in sub]

        possible_positions = get_possible_position(current_piece, accepted_positions, position_occuped, grid)
        
        orientation_to_reach = 0

        orientation_to_reach, best_position = define_best_position(possible_positions, current_piece, orientation_to_reach)

        move_to_reach_best_position(current_piece, best_position, orientation_to_reach)



    elif len(bests_moves) == 0 and change_piece:
        shape_already_moved = False

    elif len(bests_moves) > 0 and not shape_already_moved:
        move = bests_moves.pop(0)
        if len(bests_moves) == 0:
            shape_already_moved = True
        pygame.time.delay(100)
        return move

    pygame.time.delay(100)

def get_possible_position(current_piece, accepted_positions, position_occuped, grid):
    shape = current_piece.shape
    positions_valid = []

    orientation = 0

    for i in range(4):
        for x in range(10):
            y = 19

            # Piece(x_center, y_center, shape)
            test_schape = Piece(x, y, shape)
            test_schape.rotation = orientation

            while not valid_space(test_schape, grid):
                y -= 1
                test_schape = Piece(x, y, shape)

            is_valid_pos = True

            for pos in convert_shape_format(test_schape):
                if pos[0] < 0 or pos[1] < 0:
                    is_valid_pos = False

            if is_valid_pos:
                positions_valid.append([(x, y), orientation % len(current_piece.shape)])

        orientation += 1
        test_schape.rotation = orientation % len(current_piece.shape)

#print(positions_valid)

    return positions_valid

def define_best_position(possible_positions, current_piece, orientation_to_reach):
    best_position = possible_positions[0][0]
    orientation_to_reach = possible_positions[0][1]

    y_sum_test_shape = 0
    y_sum_best_shape = 0


    for pos in possible_positions:
        test_shape = Piece(pos[0][0], pos[0][1], current_piece.shape)
        test_shape.rotation = pos[1]

        best_shape = Piece(best_position[0], best_position[1], current_piece.shape)
        best_shape.rotation = orientation_to_reach

        coo_test_shape = convert_shape_format(test_shape)
        coo_best_shape = convert_shape_format(best_shape)

        for coo in coo_test_shape:
            y_sum_test_shape += 20 - coo[1]

        for coo in coo_best_shape:
            y_sum_best_shape += 20 - coo[1]

        if y_sum_test_shape < y_sum_best_shape:
            best_position = pos[0]
            orientation_to_reach = pos[1]

    return orientation_to_reach, best_position

def move_to_reach_best_position(current_piece, best_position, orientation_to_reach):
    test_shape = Piece(current_piece.x, current_piece.y, current_piece.shape)

    x = current_piece.x

    if x > best_position[0]: # Need to go left
        while x != best_position[0]:
            bests_moves.append(pygame.K_LEFT)
            x -= 1

    if x < best_position[0]: # Need to go right
        while x != best_position[0]:
            bests_moves.append(pygame.K_RIGHT)
            x += 1


    for i in range(orientation_to_reach):
        bests_moves.append(pygame.K_UP)


