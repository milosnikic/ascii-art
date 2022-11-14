from game import Game
from settings import *
from video import Video

if __name__ == "__main__":
    # Initialize settings
    settings = Settings()
    settings.get_input()

    # Check if user has selected static image
    # or webcam preview
    if settings.static:
        # Initialize game
        game = Game(settings)
        # Start game
        game.start()
    else:
        # Initialize video
        video = Video(settings)
        # Play video
        video.play()
