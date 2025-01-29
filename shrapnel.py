import pygame
import random
from circleshape import CircleShape
# from asteroidfield import AsteroidField
from constants import *

class Shrapnel(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "orange", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
