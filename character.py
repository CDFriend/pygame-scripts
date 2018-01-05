__author__ = "Charlie Friend <charles.d.friend@gmail.com>"

import pygame
import pygame.sprite
import pygame.image
from glob import glob
from animation import Animation
from utils import load_image

DIR_UP    = 0
DIR_LEFT  = 1
DIR_DOWN  = 2
DIR_RIGHT = 3

CHAR_ANIMATION_TPF = 3


class Character(pygame.sprite.Sprite):
    """ Main player character for the game. """
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.direction = DIR_DOWN

        # init sprites
        self.animations = {
            DIR_UP:    Animation(glob("assets/images/character/character_walk_up*.png"), CHAR_ANIMATION_TPF),
            DIR_DOWN:  Animation(glob("assets/images/character/character_walk_down*.png"), CHAR_ANIMATION_TPF),
            DIR_LEFT:  Animation(glob("assets/images/character/character_walk_left*.png"), CHAR_ANIMATION_TPF),
            DIR_RIGHT: Animation(glob("assets/images/character/character_walk_right*.png"), CHAR_ANIMATION_TPF)
        }

        self._update_image()
        self.pos = [50, 50]

    def update(self):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_UP]:
            self.pos[1] -= 2
            self.direction = DIR_UP
            self._update_image()
        if pressed[pygame.K_DOWN]:
            self.pos[1] += 2
            self.direction = DIR_DOWN
            self._update_image()
        if pressed[pygame.K_LEFT]:
            self.pos[0] -= 2
            self.direction = DIR_LEFT
            self._update_image()
        if pressed[pygame.K_RIGHT]:
            self.pos[0] += 2
            self.direction = DIR_RIGHT
            self._update_image()

    def _update_image(self):
        self.image, self.rect = self.animations[self.direction].next_frame()

        # always draw character in center of screen (camera moves)
        screen = pygame.display.get_surface()
        self.rect.center = (screen.get_width() / 2, screen.get_height() / 2)
