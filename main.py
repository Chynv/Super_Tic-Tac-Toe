from game import *
from CONST import *
import pygame as p

IMAGES = {}
for player in ["O", "X"]:
    IMAGES[player] = p.transform.smoothscale(p.image.load("images/New{}Logo.svg".format(player)),
                                                   (SM_SQ_SIZE - 2 * PLAYER_PADDING,
                                                    SM_SQ_SIZE - 2 * PLAYER_PADDING))
    IMAGES[player + "big"] = p.transform.smoothscale(p.image.load("images/New{}Logo.svg".format(player)),
                            (SQ_SIZE - 2 * PLAYER_PADDING,
                             SQ_SIZE - 2 * PLAYER_PADDING))

def main():
    p.init()
    p.font.init()
    p.display.set_caption("Super Tic-Tac-Toe!")
    p.display.set_icon(p.image.load("images/STTT_LOGO.png"))
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    current_game = Game()
    running = True
    hover_square = None
    hover_tiny_square = None
    result = False
    while running:
        screen.fill(p.Color("white"))
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEMOTION:
                pos = p.mouse.get_pos()
                square = [-1, -1]

                for i, D in enumerate(pos):
                    for j, (a, b) in enumerate(PARTS):
                        if a <= D < b:
                            square[i] = j
                            break

                if 0 <= square[0] < 3 and 0 <= square[1] < 3:
                    hover_square = square = (square[1], square[0])
                    y, x = pos[1] - PARTS[square[0]][0], pos[0] - PARTS[square[1]][0]
                    i_y, i_x = y // SM_SQ_SIZE, x // SM_SQ_SIZE
                    if i_y < 3 and i_x < 3:
                        hover_tiny_square = i_y, i_x
                else:
                    hover_square = None
                    hover_tiny_square = None
            elif e.type == p.MOUSEBUTTONDOWN:
                if not hover_square or not hover_tiny_square:
                    continue
                y, x = hover_square
                i_y, i_x = hover_tiny_square
                # if current_game.chosen_square == hover_square and \
                #         not current_game.board[y][x].completed and \
                #         not current_game.board[y][x].board[i_y][i_x].taken_by:
                #     result = current_game.make_move(y, x, i_y, i_x)
                if not current_game.board[y][x].completed and \
                    not current_game.board[y][x].board[i_y][i_x].taken_by and \
                        (not current_game.chosen_square or
                            current_game.chosen_square == hover_square):
                    result = current_game.make_move(y, x, i_y, i_x)
                if result:
                    print(result)
            elif e.type == p.KEYDOWN:
                if e.key == p.K_r:
                    current_game.undo()

        render_game(screen, current_game, hover_square, hover_tiny_square)
        p.display.flip()


def render_game(screen, game, hov_sq, hov_sm_sq):
    for y in range(3):
        for x in range(3):
            tl_x, tl_y = x * (SPACING + SQ_SIZE) + PADDING, y * (SPACING + SQ_SIZE) + PADDING
            render_square(screen, tl_x, tl_y, game.board[y][x].board, hov_sm_sq)
            p.draw.rect(screen, (255, 255, 255), p.Rect(tl_x, tl_y, SQ_SIZE, SQ_SIZE), width=4)
            if game.board[y][x].completed:
                screen.blit(IMAGES[game.board[y][x].taken_by + "big"],
                            p.Rect(tl_x + PLAYER_PADDING,
                                   tl_y + PLAYER_PADDING,
                                   SQ_SIZE - 2 * PLAYER_PADDING,
                                   SQ_SIZE - 2 * PLAYER_PADDING))
    if game.chosen_square or hov_sq:
        y, x = game.chosen_square or hov_sq
        if game.board[y][x].completed:
            return
        tl_x, tl_y = x * (SPACING + SQ_SIZE) + PADDING, y * (SPACING + SQ_SIZE) + PADDING
        p.draw.rect(screen, SELECTED_COLOUR, p.Rect(tl_x, tl_y, SQ_SIZE, SQ_SIZE), width=2)
    if hov_sq and hov_sm_sq:
        y, x = hov_sq
        i, j = hov_sm_sq
        if game.board[y][x].completed or game.board[y][x].board[i][j].taken_by or (game.chosen_square and \
                                        game.chosen_square != hov_sq):
            return
        tl_x, tl_y = x * (SPACING + SQ_SIZE) + PADDING, y * (SPACING + SQ_SIZE) + PADDING
        screen.blit(IMAGES[game.turn],
                    p.Rect(j * SM_SQ_SIZE + tl_x + PLAYER_PADDING,
                           i * SM_SQ_SIZE + tl_y + PLAYER_PADDING,
                           SM_SQ_SIZE - 2 * PLAYER_PADDING,
                           SM_SQ_SIZE - 2 * PLAYER_PADDING))
        # p.draw.rect(screen, (255, 255, 255, 0.5),
        #             p.Rect(j * SM_SQ_SIZE + s_x + PLAYER_PADDING,
        #                    i * SM_SQ_SIZE + s_y + PLAYER_PADDING,
        #                    SM_SQ_SIZE - 2 * PLAYER_PADDING,
        #                    SM_SQ_SIZE - 2 * PLAYER_PADDING))


def render_square(screen, s_x, s_y, board, hov_sm_sq):
    for i in range(3):
        for j in range(3):
            p.draw.rect(screen, LINE_COLOUR,
                        p.Rect(j * SM_SQ_SIZE + s_x, i * SM_SQ_SIZE + s_y,
                               SM_SQ_SIZE, SM_SQ_SIZE), width=1)
            if board[i][j].taken_by:
                screen.blit(IMAGES[board[i][j].taken_by],
                            p.Rect(j * SM_SQ_SIZE + s_x + PLAYER_PADDING,
                                   i * SM_SQ_SIZE + s_y + PLAYER_PADDING,
                                   SM_SQ_SIZE - 2 * PLAYER_PADDING,
                                   SM_SQ_SIZE - 2 * PLAYER_PADDING))


if __name__ == "__main__":
    main()
