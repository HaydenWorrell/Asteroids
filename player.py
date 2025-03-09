import pygame
from constants import SHOT_RADIUS, PLAYER_RADIUS, PLAYER_BASE_XP, PLAYER_BASE_LEVEL, PLAYER_BASE_XP_REQ, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y, velocity, rotation):
        self.rotation = rotation
        self.radius = SHOT_RADIUS
        self.position = pygame.Vector2(x, y)
        self.x = x
        self.y = y
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocity


    def draw(self, screen):
        pygame.draw.circle(screen, "#FFFFFF", self.position, self.radius, width=1)

    def update(self, dt):
        self.position += (self.velocity * dt)
        self.move(dt)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.position += forward * dt
        
class Player(CircleShape):  
    def __init__(self, x, y):
        self.radius = PLAYER_RADIUS
        super().__init__(x, y, self.radius)

        self.high_score = 0
        self.score = 0
        self.experience = PLAYER_BASE_XP
        self.level = PLAYER_BASE_LEVEL
        self.xp_to_level = PLAYER_BASE_XP_REQ
        self.rotation = 0        
        self.speed = PLAYER_SPEED

        #powerup / ability base timers
        self.speedup_time = 0
        self.fireup_time = 0
        self.shot_cd = 0.2
        self.shot_timer = 0
        
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
        self.shot_timer -= dt
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed(num_buttons=3)

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

        if mouse[1]:
            self.shoot(dt)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * self.speed * dt

    def shoot(self, dt):
        if self.shot_timer > 0:
            return

        velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

        bullet = Shot(self.position.x, self.position.y, velocity, self.rotation)

        self.shot_timer = self.shot_cd



