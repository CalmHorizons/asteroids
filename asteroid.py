import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        #Check if this is the minimum size
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        #Split into two.
        random_angle = random.uniform(20, 50)
        vector1 = self.velocity.rotate(random_angle)
        vector2 = self.velocity.rotate(-random_angle)

        smaller_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_one = Asteroid(self.position.x, self.position.y, smaller_asteroid_radius)
        asteroid_two = Asteroid(self.position.x, self.position.y, smaller_asteroid_radius)
        asteroid_one.velocity = vector1 * 1.2
        asteroid_two.velocity = vector2 * 1.2


