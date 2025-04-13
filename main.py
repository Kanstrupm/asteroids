import pygame
from player import Player
from constants import * 
from asteroidfield import AsteroidField
from asteroid import Asteroid
from circleshape import CircleShape
from bullets import Shot
import math

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
    shots = pygame.sprite.Group()


    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable) 
    Shot.containers = (shots, updatable, drawable) 

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, shots) 

    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()

    

    def circles_collide(circle1, circle2):
        distance = circle1.position.distance_to(circle2.position)
        
        return distance <= (circle1.radius + circle2.radius)




    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        dt = clock.tick(60) / 1000

        updatable.update(dt)

        screen.fill("black")

        for asteroid in asteroids:
            for shot in shots:
                if circles_collide(asteroid, shot):
                    asteroid.split()
                    shot.kill()

        try:
            drawable.draw(screen)
        except AttributeError:
            for sprite in drawable:
                if hasattr(sprite, "draw") and callable(sprite.draw):
                    sprite.draw(screen)
        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game over!")
                import sys
                sys.exit()

        pygame.display.flip()
    





if __name__ == "__main__":
    main()
