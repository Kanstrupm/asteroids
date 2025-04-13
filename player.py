import pygame
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, SHOT_RADIUS, PLAYER_SHOOT_COOLDOWN
from bullets import Shot

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, shots_group):
        super().__init__()
        self.shots = shots_group

        self.position = pygame.Vector2(x, y)
        self.rotation = 0
        self.radius = PLAYER_RADIUS

        self.shoot_timer = 0

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

        self.shoot_timer -= dt

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.shoot()    


    def move(self, dt):
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def collision(self, other_shape):
        distance = self.position.distance_to(other_shape.position)
        return distance <= (self.radius + other_shape.radius)
    
    def shoot(self):
        if self.shoot_timer > 0:
            return
        new_shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)

        direction = pygame.Vector2(0, -1)

        direction = direction.rotate(self.rotation)

        new_shot.velocity = direction * PLAYER_SHOOT_SPEED

        self.shoot_timer = PLAYER_SHOOT_COOLDOWN

        self.shots.add(new_shot)


