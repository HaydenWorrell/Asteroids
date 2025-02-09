import pygame
from main import *
from circleshape import *
from constants import *
import random


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

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        random_vector1 = self.velocity.rotate(random_angle)
        random_vector2 = self.velocity.rotate(-random_angle)
        self.radius -= ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(self.position.x, self.position.y, self.radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, self.radius)

        asteroid1.velocity = random_vector1 * 1.2
        asteroid2.velocity = random_vector2 * 1.2