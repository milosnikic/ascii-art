from game import Game
from image import Image
from settings import *

if __name__ == "__main__":
    # Initialize settings
    settings = Settings()
    settings.get_input()

    # Initialize image
    image = Image(settings, image_name=settings.image_name)

    # Draw game with image
    game = Game(image, settings)

    # Start game
    game.start()
