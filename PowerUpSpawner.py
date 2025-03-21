import pygame
import random
from constants import POWER_UP_SPAWN_RATE, SCREEN_HEIGHT, SCREEN_WIDTH
from powerups import SpeedUp, FireRateUp

class PowerUpSpawner(pygame.sprite.Sprite):
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
    power_ups_list = [SpeedUp, FireRateUp]

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0

    def spawn(self, radius, position, rng):
        #powerup = self.power_ups_list[random.randint(0, len(self.power_ups_list))](position.x, position.y, radius)
        if rng == 1:
            powerup = SpeedUp(position.x, position.y, radius)
        #print(f"Spawning powerup at {powerup.position.x}, {powerup.position.y}")
        if rng == 2:
            powerup = FireRateUp(position.x, position.y, radius)
    def update(self, dt):
        #print("Spawning logic is running...")
        self.spawn_timer += dt
        if self.spawn_timer > POWER_UP_SPAWN_RATE:
            #print("Spawning a powerup!")
            self.spawn_timer = 0

            # spawn a new speedup at a random edge
            edge = random.choice(self.edges)
            x = random.randint(100, 1600)
            y = random.randint(100, 900)
            position = pygame.Vector2(x, y)
            rng = random.randint(1, 2)
            self.spawn(25, position, rng)