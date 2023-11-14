import pygame as pg
from ECS.Has.HasSurface import HasSurface
from ECS.Has.HasCollider import HasCollider
from ECS.Has.HasScreenRef import HasScreenRef


class Sprite(HasSurface, HasCollider, HasScreenRef):
    def __init__(self, path: str, scale: float = 1.0):
        HasSurface.__init__(self, pg.transform.scale_by(pg.image.load(path).convert_alpha(), scale))
        HasCollider.__init__(self, self.surface.get_rect())

    def __repr__(self):
        return self.surface

    def draw(self):
        self.screen.blit(self.surface, self.rect)
