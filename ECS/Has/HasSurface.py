import pygame as pg


class HasSurface:
    def __init__(self, surface: pg.Surface = None):
        self._surface = pg.Surface((0, 0)) if surface is None else surface

    @property
    def surface(self):
        return self._surface

    @surface.setter
    def surface(self, surface):
        self._surface = surface
