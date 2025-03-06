import pygame
import random
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *
from powerups import *
from PowerUpSpawner import *

def main():
    pygame.init()
    pygame.display.set_caption("Asteroids")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))    
    clock = pygame.time.Clock()
    font = pygame.font.Font('freesansbold.ttf', 32)
    
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    asteroids2 = pygame.sprite.Group()
    powerups = pygame.sprite.Group()
    speedups = pygame.sprite.Group()
    fireups = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, asteroids2, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    PowerUpSpawner.containers = (updatable)
    SpeedUp.containers = (drawable, speedups, powerups)
    FireRateUp.containers = (drawable, fireups, powerups)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    field = AsteroidField()
    powerup = PowerUpSpawner()

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #print(f"Number of drawable objects: {len(drawable)}")
        dt = clock.tick(60) / 1000
        screen.fill('#000000', rect=None, special_flags=0)

        #current score display
        score = font.render(f'Score: {player.score}', True, WHITE, BLACK)
        scoreRect = score.get_rect()
        scoreRect.center = (1500, 850)             
        screen.blit(score, scoreRect)

        updatable.update(dt)

        for asteroid in asteroids:
            if player.colliding(asteroid) == True:
                #print("Game over!")

                if player.score > player.high_score:
                    player.high_score = player.score
                    player.score = 0

                for powerup in powerups:
                    powerup.kill()

                for asteroid in asteroids2:
                    asteroid.kill()

                player.score = 0       
                player.position = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
                player.speed = PLAYER_SPEED
                player.speedup_time = 0
                player.shot_cd = PLAYER_SHOOT_COOLDOWN
                player.fireup_time = 0
                player.level = PLAYER_BASE_LEVEL
                player.xp_to_level = PLAYER_BASE_XP_REQ
                player.experience = PLAYER_BASE_XP

            for other_asteroid in asteroids2:
                if other_asteroid != asteroid:
                    if other_asteroid.colliding(asteroid):
                        asteroid.clip(other_asteroid)
                        asteroid.bounce(other_asteroid, dt)

            for shot in shots:
                if shot.colliding(asteroid) == True:
                    
                    shot.kill()
                    player.score += 1
                    xp_rng = random.randint(1, 3)
                    
                    if xp_rng == 1:
                        player.experience += 10
                        print(f"xp_rng = {xp_rng}, gained 10 xp Total xp = {player.experience} XP to level = {player.xp_to_level}")
                    
                    if xp_rng == 2:
                        player.experience += 20
                        print(f"xp_rng = {xp_rng}, gained 20 xp Total xp = {player.experience} XP to level = {player.xp_to_level}")
                    
                    if xp_rng == 3:
                        player.experience += 30
                        print(f"xp_rng = {xp_rng}, gained 30 xp. Total xp = {player.experience}. XP to level = {player.xp_to_level}")
                        
                    asteroid.split()
                    
        if player.experience >= player.xp_to_level:
            player.level += 1
            player.xp_to_level *= 2
            
        
        #displays high score in the top right
        high_score_display = font.render(f'High Score: {player.high_score}', True, WHITE, BLACK)
        highScoreRect = score.get_rect()
        highScoreRect.center = (1420, 50)
        screen.blit(high_score_display, highScoreRect)

        level_display = font.render(f'Level: {player.level}', True, WHITE, BLACK)
        level_display_rect = level_display.get_rect()
        level_display_rect.center = (800, 50)
        screen.blit(level_display, level_display_rect)

        #powerup pickups
        for speedup in speedups:

            if player.colliding(speedup) == True and player.speed == PLAYER_SPEED:
                player.speed *= 2
                speedup.kill()                    
                player.speedup_time = 0
                
        player.speedup_time += dt
        if player.speedup_time > SPEED_UP_DURATION:
            player.speed = PLAYER_SPEED
        
        for fireup in fireups:

            if player.colliding(fireup) == True and player.shot_cd == PLAYER_SHOOT_COOLDOWN:
                player.shot_cd = 0.05
                fireup.kill()
                player.fireup_time = 0
        
        player.fireup_time += dt
        if player.fireup_time > FIRE_UP_DURATION:
            player.shot_cd = PLAYER_SHOOT_COOLDOWN

        for object in drawable:
            object.draw(screen)
        
        #print(f"Fireups: {len(fireups)}")
        pygame.display.flip()
    
if __name__ == "__main__":
    main()