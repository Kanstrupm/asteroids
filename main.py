import pygame
from player import Player
from constants import * 
from asteroidfield import AsteroidField
from asteroid import Asteroid


def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)  

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) 

    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        dt = clock.tick(60) / 1000

        updatable.update(dt)

        screen.fill("black")

        try:
            drawable.draw(screen)
        except AttributeError:
            for sprite in drawable:
                if hasattr(sprite, "draw") and callable(sprite.draw):
                    sprite.draw(screen)
        pygame.display.flip()
    





if __name__ == "__main__":
    main()
