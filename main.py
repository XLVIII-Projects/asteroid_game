import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from circleshape import CircleShape
from asteroidfield import AsteroidField
from shot import Shot
from shrapnel import Shrapnel


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock() #create a clock object
    
    updatable = pygame.sprite.Group() #create a group for all updatable objects
    drawable = pygame.sprite.Group() #create a group for all drawable objects
    asteroids = pygame.sprite.Group() #create a group for all asteroids
    shots = pygame.sprite.Group() #create a group for all shots
    shrapnels = pygame.sprite.Group() #create a group for all shrapnels
    
    Asteroid.containers = (updatable, drawable, asteroids) #set the containers for the Asteroid class
    AsteroidField.containers = (updatable,) #set the containers for the AsteroidField class
    asteroidfield = AsteroidField() # create an instance/ asteroidfield-object of the AsteroidField class  

    Shot.containers = (updatable, drawable, shots) #set the containers for the Shot class

    Shrapnel.containers = (updatable, drawable, shrapnels) #set the containers for the Shrapnel class

    Player.containers = (updatable, drawable) 
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    dt = 0
    asteroids_hit = 0  
    lives = 3  
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(f"Game over due to manual exit! Score: {asteroids_hit}")
                pygame.quit()
                sys.exit()
        
        for updatable_object in updatable:
            updatable_object.update(dt)
        
        screen.fill((0, 0, 0))

        for drawable_object in drawable:
            drawable_object.draw(screen)

        for asteroid in asteroids:
            if asteroid.check_collision(player):
                if not player.is_invulnerable:
                    player.respawn()
                    lives -= 1
                    if lives == 0:
                        print(f"Game over! Score: {asteroids_hit}")
                        sys.exit()
            for shot in shots:
                if asteroid.check_collision(shot):
                    asteroid.split()
                    asteroids_hit += 1

        dt = clock.tick(60)/1000 #get the time in seconds since the last frame

        pygame.display.flip()

if __name__ == "__main__":
    main()