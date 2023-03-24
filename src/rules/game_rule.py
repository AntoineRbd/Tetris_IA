from src.pieces.shape import convert_shape_format
from src.grid.grid import draw_text_middle

def valid_space(shape, grid):
    accepted_positions = [[(j, i) for j in range(10) if grid[i][j] == (0, 0, 0)] for i in range(20)]
    accepted_positions = [j for sub in accepted_positions for j in sub]
    formatted = convert_shape_format(shape)

    for pos in formatted:
        if pos not in accepted_positions:
            if pos[1] > -1:
                return False

    return True

def check_lost(positions):
    for pos in positions:
        x, y = pos
        if y < 1:
            return True

    return False

def update_score(nscore):
    score = max_score()

    with open('scores.txt', 'w') as f:
        if int(score) > int(nscore):
            f.write(str(score))
        else:
            f.write(str(nscore))

def max_score():
    with open('scores.txt', 'r') as f:
        lines = f.readlines()
        score = lines[0].strip()

    return score
