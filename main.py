import pygame
import sys
from constants import *
from player import *
from circleshape import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    gameclock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()
    dt = 0

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)
        for a in asteroids:
            if a.collision(player):
                print("Game over!")
                sys.exit(0)
            for b in shots:
                if a.collision(b):
                    b.kill()
                    a.split()

        

        screen.fill("black")
        
        for d in drawable:
            d.draw(screen)
        pygame.display.flip()
        dt = gameclock.tick(60) / 1000
        
if __name__ == "__main__":
    main()