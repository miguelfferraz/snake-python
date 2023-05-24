import random

import pygame as pg


class Food:
    def __init__(self, size: int, color: tuple, screen: pg.Surface):
        self.size = size
        self.color = color
        self.screen = screen

        self.pos = []

    def new_food_pos(self):
        screen_size = self.screen.get_size()
        self.pos = [
            random.randrange(1, (screen_size[0] // 10)) * 10,
            random.randrange(1, (screen_size[1] // 10)) * 10,
        ]

    def eat(self):
        self.pos = []

    def update(self):
        if not self.pos:
            self.new_food_pos()

        pg.draw.rect(
            self.screen,
            self.color,
            pg.Rect(self.pos[0], self.pos[1], self.size, self.size),
        )
