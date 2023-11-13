import pygame as pg

from ECS.Sprite import Sprite
from ECS.Has.HasScreenRef import HasScreenRef


class GroundRenderer(HasScreenRef):
    def __init__(self, app):
        HasScreenRef.__init__(self)
        self.ground_image = Sprite('assets/sprites/ground.png')
        self.surface = pg.Surface(self.screen.get_size())
        self.app = app
        self.camera = self.app.camera
        self.last_camera = self.camera.copy()
        self.remake_surface()

    def remake_surface(self):
        y_start = int(self.camera.y % self.ground_image.surface.get_height() - self.ground_image.surface.get_height())
        y_to = self.surface.get_height() - y_start
        y_step = self.ground_image.surface.get_height()

        x_start = int(self.camera.x % self.ground_image.surface.get_width() - self.ground_image.surface.get_width())
        x_to = self.surface.get_width() - x_start
        x_step = self.ground_image.surface.get_width()
        for y in range(y_start, y_to, y_step):
            for x in range(x_start, x_to, x_step):
                self.surface.blit(self.ground_image.surface, (x, y))

    def draw(self):
        self.screen.blit(self.surface, (0, 0))

    def update(self):
        if self.camera != self.last_camera:
            self.remake_surface()
            self.last_camera = self.camera.copy()
