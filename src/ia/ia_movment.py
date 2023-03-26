import pygame

from src.pieces.shape import convert_shape_format, Piece, S, Z, I, O, J, L, T
from src.rules.game_rule import valid_space

possible_positions = []
bests_moves = []

def generate_movment(grid, current_piece, next_piece, position_occuped):
    movment = None

    accepted_positions = [[(j, i) for j in range(10) if grid[i][j] == (0, 0, 0)] for i in range(20)]
    accepted_positions = [j for sub in accepted_positions for j in sub]

    possible_positions = get_possible_position(current_piece, accepted_positions, position_occuped, grid)

#print(possible_positions)


    pygame.time.delay(100)

def get_possible_position(current_piece, accepted_positions, position_occuped, grid):
    shape = current_piece.shape
    positions_valid = []
    #orientation = current_piece.shape[current_piece.rotation % len(current_piece.shape)]

    for x in range(10):
        y = 19

        test_schape = Piece(x, y, shape)

        while not valid_space(test_schape, grid):
            y -= 1
            test_schape = Piece(x, y, shape)

        print(convert_shape_format(test_schape))
        print('------------')
        positions_valid.append((x, y))

    return positions_valid
