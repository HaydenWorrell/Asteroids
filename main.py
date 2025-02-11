import pygame
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
    speedups = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, asteroids2, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    PowerUpSpawner.containers = (updatable)
    SpeedUp.containers = (drawable, speedups)

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

        text = font.render(f'Score: {player.score}', True, WHITE, BLACK)
        textRect = text.get_rect()
        textRect.center = (X, Y)        
        
        screen.blit(text, textRect)

        updatable.update(dt)
        for asteroid in asteroids:
            if player.colliding(asteroid) == True:
                #print("Game over!")
                player.score = 0
            for other_asteroid in asteroids2:
                if other_asteroid != asteroid:
                    if other_asteroid.colliding(asteroid):
                        asteroid.clip(other_asteroid)
                        asteroid.bounce(other_asteroid, dt)                   
            for shot in shots:
                if shot.colliding(asteroid) == True:
                    asteroid.split()
                    shot.kill()
                    player.score += 1
        for speedup in speedups:
            player.speedup_time += dt
            if player.colliding(speedup) == True and player.speed == PLAYER_SPEED:
                player.speed *= 1.5
                speedup.kill()                    
                player.speedup_time = 0
            if player.speedup_time > SPEED_UP_DURATION:
                player.speed = PLAYER_SPEED
                
            
        for object in drawable:
            object.draw(screen)
        
        print(f"Speedups: {len(speedups)}")
        pygame.display.flip()
    
if __name__ == "__main__":
    main()