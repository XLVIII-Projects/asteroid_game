import pygame
from constants import *
from player import Player
from circleshape import CircleShape


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock() #create a clock object
    dt = 0
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        screen.fill((0, 0, 0))

        player.draw(screen)

        dt = clock.tick(60)/1000 #get the time in seconds since the last frame

        pygame.display.flip()

if __name__ == "__main__":
    main()