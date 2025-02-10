# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

from constants import * 

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print ("Starting asteroids!")
    print (f"Screen width: {SCREEN_WIDTH}")
    print (f"Screen height: {SCREEN_HEIGHT}")
    game_clock = pygame.time.Clock()
    dt = 0
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updateable, drawable)
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    asteroidField = AsteroidField()
    
    current_player = Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updateable.update(dt)

        for asteroid in asteroids:
            if asteroid.collision(current_player):
                print("Game over!")
                sys.exit()
            for projectile in shots:
                if asteroid.collision(projectile):
                    asteroid.split()
                    projectile.kill()
        # replaced object update with group update current_player.update(dt)
        screen.fill("black")
        #current_player.draw(screen)
        #replaced object draw with looped group draw
        for draw_object in drawable:
            draw_object.draw(screen)
        pygame.display.flip()

        # Limit the frame rate
        dt = game_clock.tick(60) / 1000


if __name__ == "__main__":
    main()
