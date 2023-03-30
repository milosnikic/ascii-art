import sys

import pygame
from image import Image
from settings import APP_NAME


class Game:
    def __init__(self, settings) -> None:
        self.image = Image(settings)

        # Initial configuration
        pygame.init()
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("arial", settings.font)
        self.screen = pygame.display.set_mode((self.image.width, self.image.height))
        self.settings = settings
        pygame.display.set_caption(APP_NAME)

    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (
                    event.type == pygame.KEYDOWN and event.key == pygame.K_q
                ):
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        self.image.save(self.screen)

            if self.image:
                self.image.draw(self.screen, self.font)

            pygame.display.update()
            self.clock.tick(60)
