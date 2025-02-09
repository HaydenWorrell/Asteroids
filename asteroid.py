import pygame
from main import *
from circleshape import *
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        super().__init__(self.x, self.y, self.radius)
        self.position = pygame.Vector2(x, y)

    def draw(self, screen):
        pygame.draw.circle(screen, '#FFFFFF', self.position, self.radius, width=2)
        #print(f"Drawing asteroid at position: ({self.x}, {self.y})")

    def update(self, dt):
        self.position += (self.velocity * dt)