import pygame
import random
from asteroid import Asteroid
from constants import ASTEROID_SPAWN_RATE, ASTEROID_KINDS, ASTEROID_MAX_RADIUS, ASTEROID_MIN_RADIUS, SCREEN_HEIGHT, SCREEN_WIDTH



class AsteroidField(pygame.sprite.Sprite):
    edges = [
        [
            pygame.Vector2(1, 0),
            lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT),
        ],
        [
            pygame.Vector2(-1, 0),
            lambda y: pygame.Vector2(
                SCREEN_WIDTH + ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT
            ),
        ],
        [
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS),
        ],
        [
            pygame.Vector2(0, -1),
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH, SCREEN_HEIGHT + ASTEROID_MAX_RADIUS
            ),
        ],
    ]

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0
        self.world_level = 1
        
    def spawn(self, radius, position, velocity):
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity
        #print(f"Asteroid Radius: {asteroid.radius}")

    def update(self, dt):
        #print("Spawning logic is running...")
        self.spawn_timer += dt
        if self.spawn_timer > ASTEROID_SPAWN_RATE:
            #print("Spawning an asteroid!")
            self.spawn_timer = 0

            # spawn a new asteroid at a random edge
            edge = random.choice(self.edges)
            speed = random.randint(40, 100)
            velocity = edge[0] * speed
            velocity = velocity.rotate(random.randint(-30, 30))
            position = edge[1](random.uniform(0, 1))
            kind = random.randint(1, ASTEROID_KINDS)
            self.kind = kind
            
            if self.world_level == 1:
                self.spawn(ASTEROID_MIN_RADIUS * kind, position, velocity)
                #print(f"Spawning an asteroid! World level = {self.world_level}")
                
            if self.world_level > 1:
                self.spawn(ASTEROID_MIN_RADIUS * kind, position, (velocity * (self.world_level * 0.75)))
                #print(f"Spawning a level {self.world_level} asteroid!")