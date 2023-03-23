import pygame

from src.grid.grid import draw_grid, create_grid, draw_window, init_window, draw_next_shape, clear_rows, draw_text_middle
from src.pieces.shape import get_shape, convert_shape_format
from src.rules.game_rule import valid_space, check_lost, max_score


pygame.font.init()


def main_menu(win):
    running = True
    
    while running:
        win.fill((0, 0, 0))
        draw_text_middle(win, 'Press Any Key To Play', 60, (255, 255, 255))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                main(win)

def main(win):
    score = 0
    last_score = max_score()



    locked_positions = {}
    grid = create_grid(locked_positions)

    pygame.init()
    clock = pygame.time.Clock()


    change_piece = False
    running = True

    current_piece = get_shape()
    next_piece = get_shape()
    clock = pygame.time.Clock()

    fall_time = 0
    level_time =  0

    while running:
        level_time += clock.get_rawtime()

        if level_time / 1000 > 5:
            level_time = 0
            if level_time > 0.12:
                level_time -= 0.005


        fall_speed = 0.27

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

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if not valid_space(current_piece, grid):
                        current_piece.x += 1

                elif event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not valid_space(current_piece, grid):
                        current_piece.x -= 1
                
                elif event.key == pygame.K_UP: # Rotate shape
                    current_piece.rotation = current_piece.rotation + 1 % len(current_piece.shape)
                    if not valid_space(current_piece, grid):
                        current_piece.rotation = current_piece.rotation - 1 % len(current_piece.shape)

                elif event.key == pygame.K_DOWN: # Move down
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
            current_piece = next_piece
            next_piece = get_shape()
            change_piece = False
            score += clear_rows(grid, locked_positions) * 10

        draw_window(surface, grid, score, last_score)

        draw_next_shape(next_piece, win)
        pygame.display.update()

        # Check if user lost
        if check_lost(locked_positions):
            draw_text_middle(win, "YOU LOST !", 80, (255, 255, 255))
            pygame.display.update()
            pygame.time.delay(1500)
            running = False
            update_score(score)

if __name__ == "__main__":
    win = init_window()

    main_menu(win)
