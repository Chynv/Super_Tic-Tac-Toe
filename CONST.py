laterals = [0, 1, 2]
diagonals = [
    ((0, 0), (1, 1), (2, 2)),
    ((2, 0), (1, 1), (0, 2))
]
HEIGHT = WIDTH = 500
PADDING = 10
SPACING = 12
LINE_COLOUR = (1, 22, 39)
SELECTED_COLOUR = (132, 220, 207)
SQ_SIZE = (WIDTH - (PADDING + SPACING) * 2) // 3
SM_SQ_SIZE = SQ_SIZE//3
PARTS = [
    (PADDING, PADDING + SQ_SIZE),
    (PADDING + SQ_SIZE + SPACING, PADDING + 2 * SQ_SIZE + SPACING),
    (PADDING + 2 * SQ_SIZE + 2 * SPACING, PADDING + 3 * SQ_SIZE + 2 * SPACING),
]
PLAYER_PADDING = 5
