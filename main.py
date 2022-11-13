import sys

import pygame
from PIL import Image

from settings import *


def draw_pixels(symbol_image, grayscale=True):
    """Method used to display each character on screen
    on desired position.

    Args:
        symbol_image (_type_): Symbol representation of image
    """
    for col in range(0, HEIGHT, PIXEL_SIZE):
        for row in range(0, WIDTH, PIXEL_SIZE):
            if grayscale:
                character = symbol_image[row][col]
                color = "white"
            else:
                character = symbol_image[row][col][0]
                color = symbol_image[row][col][1]
            font_surf = font.render(character, True, color)
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
    step_size = max // (number_of_symbols - 1)
    index = value // step_size
    return SYMBOLS[index]


def get_symbol_image(grayscale=True):
    """Method used to transform grayscaled image pixel
    to nested array of symbols.

    Returns:
        _type_: Symbol represented image
    """
    pixels = []
    for row in range(WIDTH):
        row_pixels = []
        for col in range(HEIGHT):
            symbol = map_to_symbol(im.getpixel((row, col)))
            if grayscale:
                row_pixels.append(symbol)
            else:
                rgb = im_original.getpixel((row, col))
                row_pixels.append((symbol, rgb))
        pixels.append(row_pixels)
    return pixels


def start(grayscale=False):
    # Main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        draw_pixels(symbol_image, grayscale=grayscale)

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    # Enter image path
    image_path = input("Enter image path: ")
    grayscale = input("Grayscale (y/N): ")

    # Import image
    image_extension = image_path.split(".")[1]
    image_name = image_path.split(".")[0]
    im_original = Image.open(f"{image_name}.{image_extension}")
    # im_original.thumbnail((1280, 960), Image.ANTIALIAS)
    im = im_original.convert("L")
    WIDTH, HEIGHT = im.size
    im.save(f"{image_name}_grayscale.{image_extension}")
    symbol_image = get_symbol_image(grayscale.lower() == "y")

    # Initial configuration
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(APP_NAME)

    # Font settings
    font = pygame.font.SysFont("arial", 8)

    # Start game
    start(grayscale.lower() == "y")
