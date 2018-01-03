""" Loads a specified Tiled TMX map into pygame and draws it to the screen. """
__author__ = "Charlie Friend <charles.d.friend@gmail.com>"

import sys
import pygame
from pytmx.util_pygame import load_pygame


def main():
    # init pygame
    pygame.init()
    screen = pygame.display.set_mode((640, 480))

    # load TMX file into pygame
    tmxdata = load_pygame(sys.argv[1])

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit(0)

        for layer_num in tmxdata.visible_tile_layers:
            layer = tmxdata.layers[layer_num]

            # draw tiles in layer
            for x, y, image in layer.tiles():
                tilerect = pygame.Rect(x * tmxdata.tilewidth, y * tmxdata.tileheight,
                                       tmxdata.tilewidth, tmxdata.tileheight)
                screen.blit(image, tilerect)

        pygame.display.flip()


if __name__ == "__main__":
    main()
