import sys

import pygame
from settings import APP_NAME


class Game:
    def __init__(self, image, settings) -> None:
        self.image = image

        # Initial configuration
        pygame.init()
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("arial", settings.font)
        self.screen = pygame.display.set_mode((self.image.width, self.image.height))
        pygame.display.set_caption(APP_NAME)

    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.image.draw(self.screen, self.font)

            pygame.display.update()
            self.clock.tick(60)
