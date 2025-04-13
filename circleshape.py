import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def update(self, dt):
        self.position += self.velocity * dt

    def collision(self, other_shape):
        distance = self.position.distance_to(other_shape.position)
        return distance <= (self.radius + other_shape.radius)