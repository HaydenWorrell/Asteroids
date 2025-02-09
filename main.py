import pygame
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))    
    clock = pygame.time.Clock()

    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)


    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    field = AsteroidField()

    

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
        
        updatable.update(dt)
        for asteroid in asteroids:
            if player.colliding(asteroid) == True:
                print("Game over!")
                return
            for shot in shots:
                if shot.colliding(asteroid) == True:
                    asteroid.split()
                    shot.kill()                    

        for object in drawable:
            object.draw(screen)
        
        pygame.display.flip()
    

if __name__ == "__main__":
    main()