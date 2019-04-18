import pygame

__all__ = ["MusicSystem"]


class MusicSystem:
    def __init__(self, world):
        self.world = world

    @staticmethod
    def play(file, loop=False):
        pygame.mixer.music.load(file)
        if loop:
            pygame.mixer.music.play(-1)
        else:
            pygame.mixer.music.play()

    @staticmethod
    def set_volume(volume):
        if volume < 0 or volume > 100:
            raise ValueError("Volume can't be lower than 0 and bigger than 100")
        pygame.mixer.music.set_volume(volume/100)

    @staticmethod
    def get_volume():
        return pygame.mixer.music.get_volume()

    @staticmethod
    def stop():
        pygame.mixer.music.stop()

    @staticmethod
    def pause():
        pygame.mixer.music.pause()

    @staticmethod
    def unpause():
        pygame.mixer.music.unpause()

