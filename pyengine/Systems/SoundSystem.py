import pygame

__all__ = ["SoundSystem"]


class SoundSystem:
    def __init__(self):
        self.volume = 100

    @staticmethod
    def get_number_sound():
        return pygame.mixer.get_num_channels()

    @staticmethod
    def set_number_sound(nb):
        pygame.mixer.set_num_channels(nb)

    def play(self, file):
        sound = pygame.mixer.Sound(file)
        sound.set_volume(self.volume/100)
        sound.play()

    def set_volume(self, volume):
        if volume < 0 or volume > 100:
            raise ValueError("Volume can't be lower than 0 and bigger than 100")
        self.volume = volume

    def get_volume(self):
        return self.volume
