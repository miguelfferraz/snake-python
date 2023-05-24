import pygame as pg

UP = "u"
DOWN = "d"
RIGHT = "r"
LEFT = "l"

MV_UP_KEYS = [pg.K_w, pg.K_UP]
MV_DOWN_KEYS = [pg.K_s, pg.K_DOWN]
MV_RIGHT_KEYS = [pg.K_d, pg.K_RIGHT]
MV_LEFT_KEYS = [pg.K_a, pg.K_LEFT]

SNAKE_COLOR = (0, 255, 0)

HORIZONTAL = 0
VERTICAL = 1
SIZE = 10


class Snake:
    def __init__(self, starting_pos: list, screen: pg.Surface):
        self.screen = screen

        self.head_pos = starting_pos
        self.snake_body = [
            self.head_pos,
            # [self.pos[0] - self.size, self.pos[1]],
            # [self.pos[0] - 2 * self.size, self.pos[1]],
        ]

        self.direction = None

    def change_direction(self, key):
        # It is needed to prevent the snake from going in the opposite direction instantaneously
        if key in MV_UP_KEYS and self.direction != DOWN:
            self.direction = UP
        elif key in MV_DOWN_KEYS and self.direction != UP:
            self.direction = DOWN
        elif key in MV_RIGHT_KEYS and self.direction != LEFT:
            self.direction = RIGHT
        elif key in MV_LEFT_KEYS and self.direction != RIGHT:
            self.direction = LEFT

    def move(self):
        if self.direction is UP:
            self.head_pos[VERTICAL] -= SIZE
        elif self.direction is DOWN:
            self.head_pos[VERTICAL] += SIZE
        elif self.direction is RIGHT:
            self.head_pos[HORIZONTAL] += SIZE
        elif self.direction is LEFT:
            self.head_pos[HORIZONTAL] -= SIZE

    def update(self):
        self.move()

        for pos in self.snake_body:
            pg.draw.rect(
                self.screen,
                SNAKE_COLOR,
                pg.Rect(pos[HORIZONTAL], pos[VERTICAL], SIZE, SIZE),
            )
