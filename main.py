import pygame, sys
from pygame.locals import *

pygame.init()

def main():

    win = pygame.display.set_mode((800, 499))

    background = pygame.image.load('assets/images/mainscreen.jpg')
    screen = pygame.display.set_mode(background.get_size())
    screen.blit(background, (0, 0))
    pygame.display.set_caption("Miha's Day")

    while True:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                return
        pygame.display.flip()


if __name__ == "__main__":
    main()