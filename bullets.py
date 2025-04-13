from constants import *
from circleshape import CircleShape
import pygame

class Shot(CircleShape):
    def draw(self, surface):
        pygame.draw.circle(surface, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, 2)


    def update(self, dt):
        self.position += self.velocity * dt
