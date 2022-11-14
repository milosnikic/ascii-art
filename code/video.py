import sys

import cv2
import imutils
import pygame
from image import Image
from PIL import Image as PImage
from settings import *


class Video:
    def __init__(self, settings) -> None:
        self.image = Image(settings)
        self.video = cv2.VideoCapture(0)
        pygame.init()
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("arial", settings.font)
        self.screen = pygame.display.set_mode((640, 480))
        self.settings = settings
        pygame.display.set_caption(APP_NAME)

    def play(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            ret, frame = self.video.read()
            frame = imutils.resize(frame, width=640, height=480)
            self.image.set_image(PImage.fromarray(frame))
            self.screen = pygame.display.set_mode((self.image.width, self.image.height))

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

            self.image.draw(self.screen, self.font)

            pygame.display.update()
            self.clock.tick(30)

        self.video.release()
        cv2.destroyAllWindows()
