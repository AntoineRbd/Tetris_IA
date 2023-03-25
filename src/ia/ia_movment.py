import pygame

from src.pieces.shape import convert_shape_format, S, Z, I, O, J, L, T

possible_positions = []
bests_moves = []

def generate_movment(grid, current_piece, next_piece, position_occuped):
    movment = None

    x_locked = []
    y_locked = []

    if len(position_occuped) > 0:
        for pos in position_occuped:
            x_locked.append(pos[0])
            y_locked.append(pos[1])

    shape = convert_shape_format(current_piece)
    x_current_piece = []
    y_current_piece = []

    for pos in shape:
        x_current_piece.append(pos[0])
        y_current_piece.append(pos[1])

#y_max_current_piece = 0
#   y_max_for_x_min = 0
#   y_max_for_x_max = 0
#
#   length_current_piece = 0
#   x_min_spawn = 0
#   x_max_spawn = 0

    if current_piece.shape == S:
#           y_max_current_piece = 2
#           y_max_for_x_min = 1
#           y_max_for_x_max = 2

#            length_current_piece = 3
#           x_min_spawn = 4
#           x_max_spawn = 6

        accepted_positions = [[(j, i) for j in range(10) if grid[i][j] == (0, 0, 0)] for i in range(20)]
        accepted_positions = [j for sub in accepted_positions for j in sub]

        get_possible_position(accepted_positions)


    if current_piece.shape == Z:
        accepted_positions = [[(j, i) for j in range(10) if grid[i][j] == (0, 0, 0)] for i in range(20)]
        accepted_positions = [j for sub in accepted_positions for j in sub]

        get_possible_position(accepted_positions)

    if current_piece.shape == I:
        accepted_positions = [[(j, i) for j in range(10) if grid[i][j] == (0, 0, 0)] for i in range(20)]
        accepted_positions = [j for sub in accepted_positions for j in sub]

        get_possible_position(accepted_positions)
    
    if current_piece.shape == O:
        accepted_positions = [[(j, i) for j in range(10) if grid[i][j] == (0, 0, 0)] for i in range(20)]
        accepted_positions = [j for sub in accepted_positions for j in sub]

        get_possible_position(accepted_positions)

    if current_piece.shape == J:
        accepted_positions = [[(j, i) for j in range(10) if grid[i][j] == (0, 0, 0)] for i in range(20)]
        accepted_positions = [j for sub in accepted_positions for j in sub]

        get_possible_position(accepted_positions)

    if current_piece.shape == L:
        accepted_positions = [[(j, i) for j in range(10) if grid[i][j] == (0, 0, 0)] for i in range(20)]
        accepted_positions = [j for sub in accepted_positions for j in sub]

        get_possible_position(accepted_positions)

    if current_piece.shape == T:
        accepted_positions = [[(j, i) for j in range(10) if grid[i][j] == (0, 0, 0)] for i in range(20)]
        accepted_positions = [j for sub in accepted_positions for j in sub]

        get_possible_position(accepted_positions, position_occuped)


    pygame.time.delay(100)

def get_possible_position(accepted_positions, position_occuped):
    x_0_list = []
    x_1_list = []
    x_2_list = []
    x_3_list = []
    x_4_list = []
    x_5_list = []
    x_6_list = []
    x_7_list = []
    x_8_list = []
    x_9_list = []

    piece_in_col = False

    for pos in accepted_positions:
        match pos[0]:
            case 0:
                x_0_list.append(pos)
            case 1:
                x_1_list.append(pos)
            case 2:
                x_2_list.append(pos)
            case 3:
                x_3_list.append(pos)
            case 4:
                x_4_list.append(pos)
            case 5:
                x_5_list.append(pos)
            case 6:
                x_6_list.append(pos)
            case 7:
                x_7_list.append(pos)
            case 8:
                x_8_list.append(pos)
            case 9:
                x_9_list.append(pos)




    print("max for x0: " + str(max(x_0_list,key=lambda item:item[1])))
    print("max for x1: " + str(max(x_1_list,key=lambda item:item[1])))
    print("max for x2: " + str(max(x_2_list,key=lambda item:item[1])))
    print("max for x3: " + str(max(x_3_list,key=lambda item:item[1])))
    print("max for x4: " + str(max(x_4_list,key=lambda item:item[1])))
    print("max for x5: " + str(max(x_5_list,key=lambda item:item[1])))
    print("max for x6: " + str(max(x_6_list,key=lambda item:item[1])))
    print("max for x7: " + str(max(x_7_list,key=lambda item:item[1])))
    print("max for x8: " + str(max(x_8_list,key=lambda item:item[1])))
    print("max for x9: " + str(max(x_9_list,key=lambda item:item[1])))





