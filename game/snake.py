import pygame as pg

UP = "U"
DOWN = "D"
RIGHT = "R"
LEFT = "L"

MOVEMENTS = {
    # key: (new_direction, opposite_direction)
    pg.K_w: (UP, DOWN),
    pg.K_UP: (UP, DOWN),
    pg.K_s: (DOWN, UP),
    pg.K_DOWN: (DOWN, UP),
    pg.K_d: (RIGHT, LEFT),
    pg.K_RIGHT: (RIGHT, LEFT),
    pg.K_a: (LEFT, RIGHT),
    pg.K_LEFT: (LEFT, RIGHT),
}

HORIZONTAL_AXIS = 0
VERTICAL_AXIS = 1


class Snake:
    def __init__(self, starting_pos: list, size: int, color: tuple, screen: pg.Surface):
        self.head_pos = starting_pos
        self.size = size
        self.color = color
        self.screen = screen

        self.snake_body = [
            self.head_pos,
            # [self.pos[0] - self.size, self.pos[1]],
            # [self.pos[0] - 2 * self.size, self.pos[1]],
        ]

        self.direction = None

    def change_direction(self, key: int):
        # It is needed to prevent the snake from going in the opposite direction instantaneously
        new_direction, opposite_direction = MOVEMENTS[key]
        if self.direction != opposite_direction:
            self.direction = new_direction

    def move(self):
        if self.direction is UP:
            self.head_pos[VERTICAL_AXIS] -= self.size
        elif self.direction is DOWN:
            self.head_pos[VERTICAL_AXIS] += self.size
        elif self.direction is RIGHT:
            self.head_pos[HORIZONTAL_AXIS] += self.size
        elif self.direction is LEFT:
            self.head_pos[HORIZONTAL_AXIS] -= self.size

    def update(self):
        self.move()

        for pos in self.snake_body:
            pg.draw.rect(
                self.screen,
                self.color,
                pg.Rect(pos[HORIZONTAL_AXIS], pos[VERTICAL_AXIS], self.size, self.size),
            )
