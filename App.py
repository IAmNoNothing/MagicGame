import pygame as pg

from ECS.GroundRenderer import GroundRenderer
from ECS.Has.HasSurface import HasSurface
import json

from engine.Camera import Camera


class App(HasSurface):

    def __init__(self):
        HasSurface.__init__(self, pg.display.set_mode((800, 600), pg.DOUBLEBUF))  # must be first!!!
        self.configs = {}  # all configs placed here
        self.config = self.get_config('config')  # after defining self.configs
        self.screen = self.surface  # from HasSurface component
        self.running = True
        self.clock = pg.time.Clock()
        
        self.delta = 0  # delta time
        self._camera = Camera(self)
        self.ground_renderer = GroundRenderer(self)

        self.keys = pg.key.get_pressed()
        self.m_pos = pg.mouse.get_pos()
        self.mouse = pg.mouse.get_pressed()

    def get_config(self, name):
        if name not in self.configs:
            with open(f'cfg/{name}.json') as f:
                self.configs[name] = json.load(f)
        return self.configs[name]

    @property
    def camera(self):
        return self._camera.position

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

    def run(self):
        while self.running:
            self.check_events()
            self.update()
            self.draw()

    def update(self):
        self.keys = pg.key.get_pressed()
        self.m_pos = pg.mouse.get_pos()
        self.mouse = pg.mouse.get_pressed()
        self.delta = self.clock.tick(self.config['fps'])
        self._camera.move()
        pg.display.flip()
        self.ground_renderer.update()
        pg.display.set_caption(f'FPS: {self.clock.get_fps():.2f}')

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.ground_renderer.draw()
