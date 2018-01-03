__author__ = "Charlie Friend <charles.d.friend@gmail.com>"

import sys
import pygame


def main():
    pygame.init()

    display_size = (320, 240)
    screen = pygame.display.set_mode(display_size)

    BLACK = (0, 0, 0)

    pos_x, pos_y = 20, 20

    while True:
        for event in pygame.event.get():
            # We have to iterate through the event queue or bad stuff happens!
            if event.type == pygame.QUIT:
                sys.exit()

        # handle keys
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]: pos_x -= 3
        if pressed[pygame.K_RIGHT]: pos_x += 3
        if pressed[pygame.K_UP]: pos_y -= 3
        if pressed[pygame.K_DOWN]: pos_y += 3

        # draw frame
        screen.fill(BLACK)

        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(pos_x, pos_y, 25, 25))

        pygame.display.flip()


if __name__ == "__main__":
    main()
