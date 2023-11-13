import pygame as pg


class Collider(pg.Rect):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_surface(self, color=(0, 0, 0)):
        surf = pg.Surface((self.width, self.height))
        surf.fill(color)
        return surf


class HasCollider:

    def __init__(self, collider: Collider = None):
        self._collider = Collider((0, 0), (0, 0)) if collider is None else collider

    @property
    def collider(self):
        return self._collider

    @collider.setter
    def collider(self, collider):
        self._collider = collider

    @property
    def rect(self):
        return self.collider

    @rect.setter
    def rect(self, rect):
        self.collider = rect
