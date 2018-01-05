__author__ = "Charlie Friend <charles.d.friend@gmail.com>"

import sys
import pygame
from pygame.time import Clock
from character import Character
from world import World


def main():
    pygame.init()
    screen = pygame.display.set_mode((320, 240))

    character = Character()
    world = World("assets/maps/house.tmx", character=character)

    clock = Clock()

    # create sprite groups
    g_world = pygame.sprite.RenderPlain(world)
    g_character = pygame.sprite.RenderPlain(character)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

        screen.fill((0, 0, 0))

        # update layers
        g_character.update()
        g_world.update()

        # render layers
        g_world.draw(screen)
        g_character.draw(screen)

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
