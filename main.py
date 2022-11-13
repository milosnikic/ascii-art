import sys

import pygame
from PIL import Image

from debug import debug
from settings import *


def draw_pixels(symbol_image):
    """Method used to display each character on screen
    on desired position.

    Args:
        symbol_image (_type_): Symbol representation of image
    """
    for col in range(0, HEIGHT, PIXEL_SIZE):
        for row in range(0, WIDTH, PIXEL_SIZE):
            font_surf = font.render(symbol_image[row][col], True, "white")
            font_rect = font_surf.get_rect(topleft=(row, col))
            screen.blit(font_surf, font_rect)


def map_to_symbol(value):
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
    step_size = max // number_of_symbols

    steps = [step for step in range(step_size, max, step_size)]

    for index, step in enumerate(steps):
        if value <= step:
            return SYMBOLS[index]
    return SYMBOLS[number_of_symbols - 1]


def get_symbol_image():
    """Method used to transform grayscaled image pixel
    to nested array of symbols.

    Returns:
        _type_: Symbol represented image
    """
    pixels = []
    for row in range(WIDTH):
        row_pixels = []
        for col in range(HEIGHT):
            row_pixels.append(map_to_symbol(im.getpixel((row, col))))
        pixels.append(row_pixels)
    return pixels


# Import image
image_extension = "jpeg"
image_name = "kscerato"
im = Image.open(f"{image_name}.{image_extension}").convert("L")
WIDTH, HEIGHT = im.size
im.save(f"{image_name}_grayscale.{image_extension}")
symbol_image = get_symbol_image()

# Initial configuration
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(APP_NAME)

# Font settings
font = pygame.font.SysFont("arial", 8)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    draw_pixels(symbol_image)

    pygame.display.update()
    clock.tick(60)
