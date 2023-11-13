from ECS.Has.HasSurface import HasSurface


class GameObject(HasSurface):
    def __init__(self):
        HasSurface.__init__(self)

    def draw(self):
        pass

    def update(self, dt):
        pass
