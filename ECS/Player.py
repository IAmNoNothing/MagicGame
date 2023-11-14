from ECS.Has.HasCollider import HasCollider
from ECS.Has.HasScreenRef import HasScreenRef
import pygame as pg


class Player(HasCollider, HasScreenRef):
    def __init__(self, app):
        HasScreenRef.__init__(self)
        self.app = app
        self.cfg = self.app.get_config('player')
        self.surf = pg.Surface(self.cfg['size'])
        self.rect_center = self.surf.get_rect(center=self.screen.get_rect().center)
        HasCollider.__init__(self, self.surf.get_rect())
        self.wands = []
        self.chosen_wand = None

    def update(self):
        pass

    def draw(self):
        self.screen.blit(self.surf, self.rect_center)

    def cast(self):
        pass
