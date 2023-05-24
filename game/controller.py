import pygame as pg

import game.constants as consts
from game.snake import Snake, MOVEMENTS
from game.food import Food

CLOCK = pg.time.Clock()


class Controller:
    def __init__(self, caption: str = "Snake", size: tuple = (800, 600)):
        pg.init()
        pg.display.set_caption(caption)
        self.screen = pg.display.set_mode(size)

        self.score = 0
        self.game_over = False

        self.snake = Snake(
            starting_pos=[size[0] // 2, size[1] // 2],
            size=consts.ENTITIES_SIZE,
            color=consts.SNAKE_COLOR,
            screen=self.screen,
        )

        self.food = Food(size=consts.ENTITIES_SIZE, color=consts.FOOD_COLOR, screen=self.screen)

    def run(self):
        while not self.game_over:
            self.handle_events()
            self.update()

            pg.display.update()

            # Refresh rate
            CLOCK.tick(consts.TICK_RATE)

        pg.quit()

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.game_over = True
            elif event.type == pg.KEYDOWN:
                if event.key in MOVEMENTS.keys():
                    self.snake.change_direction(event.key)
                # Pressing 'Esc' key create an event to quit the game
                elif event.key == pg.K_ESCAPE:
                    pg.event.post(pg.event.Event(pg.QUIT))

    def update(self):
        self.screen.fill(consts.SCREEN_COLOR)

        if self.snake.head_pos == self.food.pos:
            self.snake.grow()
            self.food.eat()

            self.score += 1

        self.snake.update()
        self.food.update()
