import pygame as pg


class Controller:
    def __init__(self, caption: str = "Snake", size: tuple = (800, 600)):
        pg.init()
        pg.display.set_caption(caption)
        self.screen = pg.display.set_mode(size)

        self.game_over = False

    def run(self):
        while not self.game_over:
            for event in pg.event.get():
                if event.type == pg.QUIT or (
                    event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE
                ):
                    self.game_over = True

            self.screen.fill((0, 0, 0))
            pg.display.flip()

        pg.quit()
