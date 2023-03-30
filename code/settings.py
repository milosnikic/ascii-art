WIDTH = 1280
HEIGHT = 960
PIXEL_SIZE = 8
FONT_SIZE = 8
APP_NAME = "ASCII ART"
SYMBOLS = [".", "_", "^", "!", "*", "&", "$", "%", "@"]


class Settings:
    def __init__(self) -> None:
        self.image_path = None
        self.grayscale = True
        self.resize = False
        self.pixels = PIXEL_SIZE
        self.font = FONT_SIZE
        self.static = True

    def get_input(self):
        static_image = input(
            "Do you want static image or live preview from webcam? (s/w): "
        )
        if static_image.lower() != "s":
            self.static = False

        self.get_image_settings()

    def get_image_settings(self):
        image_path = input("Enter image path: ")
        if not image_path:
            raise Exception("You have to provide path")
        self.image_path = image_path

        grayscale = input("Grayscale (y/N): ")
        if grayscale and grayscale != "":
            self.grayscale = grayscale.lower() == "y"

        resize = input("Resize image (y/N): ")
        if resize and resize.lower() == "y":
            self.resize = resize.lower() == "y"

        pixels = input("Number of pixels(default 8): ")
        if pixels:
            self.pixels = int(pixels)

        font = input("Font size (default 8): ")
        if font:
            self.font = int(font)
