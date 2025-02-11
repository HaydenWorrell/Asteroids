import pygame
import random
from circleshape import *
from constants import *
from main import *


class SpeedUp(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.position = pygame.Vector2(x, y)
        self.radius = radius
            

    def draw(self, screen):
        pygame.draw.circle(screen, '#FFFF00', self.position, self.radius, width=10)
        #print(f"drawing speedup at {self.position.x}, {self.position.y}")

class FireRateUp(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.position = pygame.Vector2(x, y)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, '#0000FF', self.position, self.radius, width=10)
        #print(f"drawing fire rate up at {self.position.x}, {self.position.y}")
