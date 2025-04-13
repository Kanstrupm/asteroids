import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.position = pygame.Vector2(x, y)
        self.rotation = 0
        self.radius = PLAYER_RADIUS

        surface_size = int(self.radius * 2.2)
        self.image = pygame.Surface((surface_size, surface_size), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(x, y))

        if hasattr(self.__class__, "containers"):
            for group in self.__class__.containers:
                group.add(self)

    def triangle(self):
        center = pygame.Vector2(self.image.get_width() // 2, self.image.get_height()// 2)
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        right = pygame.Vector2(1, 0).rotate(self.rotation) * self.radius / 1.5
        a = center + forward * self.radius
        b = center - forward * self.radius / 2 - right
        c = center - forward * self.radius / 2 + right

        return [a, b, c]
    

    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(dt * -1)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(dt * -1)

        self.rect.center = self.position

        self.image.fill((0, 0, 0, 0))
        pygame.draw.polygon(self.image, "white", self.triangle(), 2)


    def move(self, dt):
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def collision(self, other_shape):
        distance = self.position.distance_to(other_shape.position)
        return distance <= (self.radius + other_shape.radius)

