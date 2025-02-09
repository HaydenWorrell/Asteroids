import pygame
from constants import *
from circleshape import *
from main import *

class Player(CircleShape):
    

    def __init__(self, x, y):
        self.rotation = 0
        self.radius = PLAYER_RADIUS
        self.x = x
        self.y = y
        super().__init__(self.x, self.y, self.radius)
    
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, '#FFFFFF', self.triangle(), width=2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)

        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.move(dt)
        
        if keys[pygame.K_s]:
            self.move(-dt)

        if keys[pygame.K_SPACE]:
            self.shoot(dt)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self, dt):

        velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

        bullet = Shot(self.position.x, self.position.y, velocity, self.rotation)







class Shot(CircleShape):

    def __init__(self, x, y, velocity, rotation):
        super().__init__(x, y, SHOT_RADIUS)
        self.rotation = rotation
        self.radius = SHOT_RADIUS
        self.position = pygame.Vector2(x, y)
        self.x = x
        self.y = y
        self.velocity = velocity


    def draw(self, screen):
        pygame.draw.circle(screen, "#FFFFFF", self.position, self.radius, width=1)

    def update(self, dt):
        self.position += (self.velocity * dt)
        self.move(dt)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.position += forward * dt
