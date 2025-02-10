import pygame
import random
import math

def random_unit_vector():
    angle = random.uniform(0, 2 * math.pi)
    x = math.cos(angle)
    y = math.sin(angle)
    return pygame.math.Vector2(x, y)