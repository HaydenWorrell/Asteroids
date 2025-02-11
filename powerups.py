import pygame
import random
from circleshape import *
from constants import *
from main import *


class SpeedUp(CircleShape):
    edges = [
        [
            pygame.Vector2(1, 0),
            lambda y: pygame.Vector2(-25, y * SCREEN_HEIGHT),
        ],
        [
            pygame.Vector2(-1, 0),
            lambda y: pygame.Vector2(
                SCREEN_WIDTH + 25, y * SCREEN_HEIGHT
            ),
        ],
        [
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -25),
        ],
        [
            pygame.Vector2(0, -1),
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH, SCREEN_HEIGHT + 25
            ),
        ],
    ]

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.position = pygame.Vector2(x, y)
        self.radius = radius
            

    def draw(self, screen):
        pygame.draw.circle(screen, '#FFFF00', self.position, self.radius, width=10)
        print(f"drawing speedup at {self.position.x}, {self.position.y}")