from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    containers = []
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
        #print(f"{self.x} : {self.y}")

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius > ASTEROID_MIN_RADIUS:
            angle = random.uniform(20,50)
            a = self.velocity.rotate(angle)
            b = self.velocity.rotate(-angle)
            
            asteroid = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            asteroid.velocity = a * 1.2
            asteroid = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            asteroid.velocity = b * 1.2
            
            
