""" Loads a specified Tiled TMX map into pygame and draws it to the screen. """
__author__ = "Charlie Friend <charles.d.friend@gmail.com>"

import sys
import pygame
from world import World

def main():
    # init pygame
    pygame.init()
    screen = pygame.display.set_mode((640, 480))

    # load TMX file into pygame
    world = World(sys.argv[1])

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit(0)

        g_world = pygame.sprite.RenderPlain(world)
        g_world.update()
        g_world.draw(screen)

        pygame.display.flip()


if __name__ == "__main__":
    main()
