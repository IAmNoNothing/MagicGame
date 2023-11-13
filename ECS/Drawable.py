from ECS.Has.HasCollider import HasCollider
from ECS.Has.HasScreenRef import HasScreenRef
from ECS.Has.HasSurface import HasSurface


class Drawable(HasScreenRef, HasCollider, HasSurface):
    def draw(self):
        self.screen.blit(self.surface, self.rect)
