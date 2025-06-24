# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, ASTEROID_KINDS, ASTEROID_MAX_RADIUS, ASTEROID_MIN_RADIUS, ASTEROID_SPAWN_RATE

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    timeclock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.fill((0,0,0))
        pygame.display.flip()
        dt = timeclock.tick(60) / 1000


if __name__ == "__main__":
    main()