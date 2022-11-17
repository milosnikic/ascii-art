from pathlib import Path

import pygame
from PIL import Image as PImage
from settings import *


class Image:
    def __init__(self, settings, image_name=None) -> None:
        self.settings = settings
        if image_name:
            self.image_extension = image_name.split(".")[1]
            self.image_name = image_name.split(".")[0]
            self.set_image(
                PImage.open(
                    Path(
                        f"../ascii-art/assets/images/{self.image_name}.{self.image_extension}"
                    )
                )
            )

    def set_image(self, image):
        self.original_image = image

        if self.settings.resize:
            self.original_image.thumbnail((1280, 960), Image.ANTIALIAS)

        self.width, self.height = self.original_image.size
        self.image = self.original_image.convert("L")
        self.symbol_image = self.get_symbol_image()

    def map_to_symbol(self, value):
        """Method used to map individual pixel value to symbol.
        We take total number of symbols and calculate step size.
        Starting from the brightest to the darkest symbol, checking
        the value of grayscaled pixel to determine, which symbol
        should that pixel be mapped to.

        Args:
            value (_type_): Grayscaled pixel 0 - 255

        Returns:
            (str): Character representation of pixel
        """
        max = 255
        number_of_symbols = len(SYMBOLS)
        step_size = max // (number_of_symbols - 1)
        index = value // step_size
        return SYMBOLS[index]

    def get_symbol_image(self):
        """Method used to transform grayscaled image pixel
        to nested array of symbols.

        Returns:
            _type_: Symbol represented image
        """
        pixels = []
        for row in range(self.width):
            row_pixels = []
            for col in range(self.height):
                symbol = self.map_to_symbol(self.image.getpixel((row, col)))
                if self.settings.grayscale:
                    row_pixels.append(symbol)
                else:
                    rgb = self.original_image.getpixel((row, col))
                    row_pixels.append((symbol, rgb))
            pixels.append(row_pixels)
        return pixels

    def draw(self, screen, font):
        """Method used to display each character on screen
        on desired position.

        Args:
            screen (Surface): Screen where image is going to be displayed
            font (Font): Font used for displaying image
        """

        for col in range(0, self.height, self.settings.pixels):
            for row in range(0, self.width, self.settings.pixels):
                if self.settings.grayscale:
                    character = self.symbol_image[row][col]
                    color = "white"
                else:
                    character = self.symbol_image[row][col][0]
                    color = self.symbol_image[row][col][1]
                font_surf = font.render(character, True, color)
                font_rect = font_surf.get_rect(topleft=(row, col))
                screen.blit(font_surf, font_rect)

    def save(self, screen):
        """Method used to save surface as an image

        Args:
            screen (_type_): Main surface of pygame window
        """
        path = (
            f"../ascii-art/assets/images/{self.image_name}_ascii.{self.image_extension}"
        )
        pygame.image.save(
            screen,
            path,
        )
        print(f"ASCII Image has been saved as image at following path: {path}")
