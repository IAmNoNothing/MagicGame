import pygame as pg
from engine.utils.umath import clamp


class Camera:
    def __init__(self, app):
        self.app = app
        self.position = pg.Vector2()
        self.velocity = pg.Vector2()
        self.cfg = self.app.get_config('camera')

    def move(self):
        if self.app.keys[pg.K_w]:
            self.velocity.y += 1
        elif self.app.keys[pg.K_s]:
            self.velocity.y -= 1

        if self.app.keys[pg.K_a]:
            self.velocity.x += 1
        elif self.app.keys[pg.K_d]:
            self.velocity.x -= 1

        self.velocity.x = clamp(self.velocity.x, -self.cfg['speed'], self.cfg['speed'])
        self.velocity.y = clamp(self.velocity.y, -self.cfg['speed'], self.cfg['speed'])
        self.position.x += self.velocity.x * self.app.delta
        self.position.y += self.velocity.y * self.app.delta
        self.velocity.y *= self.cfg['sub']
        self.velocity.x *= self.cfg['sub']
