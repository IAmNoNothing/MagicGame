import pygame as pg


class HasScreenRef:
    screen = pg.display.get_surface()

    def __init__(self):
        self.screen = pg.display.get_surface()
