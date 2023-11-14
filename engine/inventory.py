import pygame as pg

from ECS.Sprite import Sprite


class Inventory:
    def __init__(self, app, default=None):
        self.opened = False
        self.app = app
        self.cfg = self.app.get_config('inventory')
        self.size = self.cfg['size']
        self.inv = [[default for _ in range(self.size[0])] for _ in range(self.size[1])]
        self.cell = Sprite('assets/sprites/cell.png')
        self.cell.surface.set_at((0, 0), pg.Color(0, 0, 0, 0))
        self.bg_surface = self._create_surface()

    def draw(self):
        self.app.screen.blit(self.bg_surface, self.cfg['pos'])

    def _create_surface(self):
        cell_size = self.cell.surface.get_size()
        surf = pg.Surface((self.size[0] * (cell_size[0] + 0), self.size[1] * (cell_size[1] + 0)))

        for y in range(self.size[1]):
            for x in range(self.size[0]):
                surf.blit(self.cell.surface, (x * (cell_size[0] + 0), y * (cell_size[1] + 0)))

        return surf
