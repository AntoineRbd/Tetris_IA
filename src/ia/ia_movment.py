import pygame

from src.pieces.shape import convert_shape_format, Piece, S, Z, I, O, J, L, T
from src.rules.game_rule import valid_space

bests_moves = []

def generate_movment(grid, current_piece, next_piece, position_occuped, change_piece):
    movment = None

    if len(bests_moves) == 0 and change_piece == False:
        accepted_positions = [[(j, i) for j in range(10) if grid[i][j] == (0, 0, 0)] for i in range(20)]
        accepted_positions = [j for sub in accepted_positions for j in sub]

        possible_positions = get_possible_position(current_piece, accepted_positions, position_occuped, grid)

        best_position = define_best_position(possible_positions, current_piece)

#print("Best position is : " + str(convert_shape_format(Piece(best_position[0], best_position[1], current_piece.shape))))

        move_to_reach_best_position(current_piece, best_position)

    elif len(bests_moves) > 0:
#print(convert_shape_format(current_piece))
        move = bests_moves.pop(0)
        pygame.time.delay(100)
        return move

    pygame.time.delay(100)

def get_possible_position(current_piece, accepted_positions, position_occuped, grid):
    shape = current_piece.shape
    positions_valid = []
    #orientation = current_piece.shape[current_piece.rotation % len(current_piece.shape)]

    for x in range(10):
        y = 19

        # Piece(x_center, y_center, shape)
        test_schape = Piece(x, y, shape)

        while not valid_space(test_schape, grid):
            y -= 1
            test_schape = Piece(x, y, shape)

        is_valid_pos = True

        for pos in convert_shape_format(test_schape):
            if pos[0] < 0 or pos[1] < 0:
                is_valid_pos = False

        if is_valid_pos:
            positions_valid.append((x, y))

    print(positions_valid)

    return positions_valid

def define_best_position(possible_positions, current_piece):
    
#    min_total_y = 20
#    y_total_current_piece = 0
    best_position = possible_positions[0]


    for pos in possible_positions:
        if pos[1] > best_position[1]:
            best_position = pos



#        test_shape = Piece(pos[0], pos[1], current_piece.shape)
#        coord_piece = convert_shape_format(test_shape)

#        for p in coord_piece:
#            y_total_current_piece += 20 - p[1]
#
#        if y_total_current_piece < min_total_y:
#            min_total_y = y_total_current_piece
#            best_position = pos
#
#        y_total_current_piece = 0

    print(best_position)

    return best_position

def move_to_reach_best_position(current_piece, best_position):
    test_shape = Piece(current_piece.x, current_piece.y, current_piece.shape)

    x = current_piece.x

    if x > best_position[0]: # Need to go left
        while x != best_position[0]:
            print("current x: " + str(x))
            bests_moves.append(pygame.K_LEFT)
            x -= 1

    if x < best_position[0]: # Need to go right
        while x != best_position[0]:
            print("current x: " + str(x))
            bests_moves.append(pygame.K_RIGHT)
            x += 1


    for m in bests_moves:
        if m == pygame.K_LEFT:
            print("Gauche")
        if m == pygame.K_RIGHT:
            print("Droite")





