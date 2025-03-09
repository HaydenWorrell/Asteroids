import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0
        self.kind = 0
        self.position = pygame.Vector2(x, y)

    def draw(self, screen):
        pygame.draw.circle(screen, '#FFFFFF', self.position, self.radius, width=1)
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
        
        asteroid1.clip(asteroid2)

        asteroid1.velocity = random_vector1 * 1.2
        asteroid2.velocity = random_vector2 * 1.2

    def move(self, dt):
        forward = self.velocity.rotate(self.rotation)
        self.position += forward * dt

    def bounce(self, Asteroid, dt):
        #print(f'Asteroid collision detected. Asteroid base velocity: {self.velocity}')
        

        if abs(self.position.x - Asteroid.position.x) < abs(self.position.y - Asteroid.position.y):
            self.velocity.y *= -1
            Asteroid.velocity.y *= -1
        if abs(self.position.y - Asteroid.position.y) < abs(self.position.x - Asteroid.position.x):
            self.velocity.x *= -1
            Asteroid.velocity.x *= -1

        #print(f'Asteroid final velocity: {self.velocity}')