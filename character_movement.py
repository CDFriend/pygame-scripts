__author__ = "Charlie Friend <charles.d.friend@gmail.com>"

import sys
import pygame
from pygame.time import Clock
from character import Character


def main():
    pygame.init()
    screen = pygame.display.set_mode((320, 240))

    character = Character()

    clock = Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

        # render hero group
        g_character = pygame.sprite.RenderPlain(character)

        screen.fill((0, 0, 0))

        # draw hero group
        g_character.update()
        g_character.draw(screen)

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
