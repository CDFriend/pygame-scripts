"""
Class for creating a pygame sprite from a Tiled TMX file. Uses the PyTMX
library.
"""

__author__ = "Charlie Friend <charles.d.friend@gmail.com>"

import pygame
from pytmx.util_pygame import load_pygame


class World(pygame.sprite.Sprite):
    def __init__(self, tmx_path, init_pos=(0,0), character=None):
        """ Initialize a pygame sprite from a tmx world. """
        pygame.sprite.Sprite.__init__(self)

        tiled_map = load_pygame(tmx_path)
        self.image, self.rect = self._make_map_image(tiled_map)

        self.set_camera_pos(init_pos)

        self._character = character

    def update(self):
        if self._character:
            self.set_camera_pos(self._character.pos)

    def set_camera_pos(self, pos):
        """ Set the camera's center position to (pos[0], pos[1]). """
        screen = pygame.display.get_surface()
        self.rect.topleft = [-pos[0] + screen.get_width() / 2,
                             -pos[1] + screen.get_height() / 2]

    def _make_map_image(self, tiledmap):
        """ Get image and rect from pytmx tiled map. """
        img_width = tiledmap.tilewidth * tiledmap.width
        img_height = tiledmap.tileheight * tiledmap.height

        map_rect = pygame.Rect(0, 0, img_width, img_height)
        map_image = pygame.Surface((img_width, img_height))

        for layer_num in tiledmap.visible_tile_layers:
            layer = tiledmap.layers[layer_num]

            # draw tiles in layer
            for x, y, image in layer.tiles():
                tilerect = pygame.Rect(x * tiledmap.tilewidth, y * tiledmap.tileheight,
                                       tiledmap.tilewidth, tiledmap.tileheight)
                map_image.blit(image, tilerect)

        return map_image, map_rect
