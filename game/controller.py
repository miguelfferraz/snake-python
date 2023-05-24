import pygame as pg

from game.snake import Snake, MV_UP_KEYS, MV_DOWN_KEYS, MV_RIGHT_KEYS, MV_LEFT_KEYS

MOVEMENTS = MV_UP_KEYS + MV_DOWN_KEYS + MV_RIGHT_KEYS + MV_LEFT_KEYS

CLOCK = pg.time.Clock()

SCREEN_COLOR = (0, 0, 0)


class Controller:
    def __init__(self, caption: str = "Snake", size: tuple = (800, 600)):
        pg.init()
        pg.display.set_caption(caption)
        self.screen = pg.display.set_mode(size)

        self.game_over = False

        self.snake = Snake([size[0] // 2, size[1] // 2], self.screen)

    def run(self):
        while not self.game_over:
            self.handle_events()
            self.update()

            pg.display.update()

            # Refresh rate
            CLOCK.tick(25)

        pg.quit()

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.game_over = True
            elif event.type == pg.KEYDOWN:
                if event.key in MOVEMENTS:
                    self.snake.change_direction(event.key)
                # Pressing 'Esc' key create an event to quit the game
                elif event.key == pg.K_ESCAPE:
                    pg.event.post(pg.event.Event(pg.QUIT))

    def update(self):
        self.screen.fill(SCREEN_COLOR)
        self.snake.update()
