import pygame
from randomvector import random_unit_vector

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def colliding(self, other_asteroid):
        if pygame.math.Vector2.distance_to(other_asteroid.position, self.position) <= self.radius + other_asteroid.radius:
            return True
        return False
    
    def clip(self, Asteroid):
        distance_magnitude = pygame.math.Vector2.distance_to(Asteroid.position, self.position)
        distance1 = Asteroid.position - self.position
        distance2 = -distance1
        goal_distance = self.radius + Asteroid.radius + 1

        if distance_magnitude != 0:

            self.position -= distance1 / distance_magnitude
            Asteroid.position -= distance2 / distance_magnitude

        else:
            vector = goal_distance * random_unit_vector()
            self.position += vector + (0.1, 0.1)


        
