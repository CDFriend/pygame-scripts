__author__ = "Charlie Friend <charles.d.friend@gmail.com>"

import os
import pygame.image


def load_image(filename, colorkey=None):
    """
    Try to load an image, exiting gracefully if necessary.
    Adapted from pygame docs: https://www.pygame.org/docs/tut/ChimpLineByLine.html
    """
    try:
        image = pygame.image.load(filename)
    except pygame.error, message:
        raise SystemExit("Could not load image: " + message)

    # copy image, convert color format to match display
    image = image.convert()

    # set colorkey, if specified
    if colorkey is not None:
        image.set_colorkey(colorkey)

    # return Surface and collider rectangle
    return image, image.get_rect()

