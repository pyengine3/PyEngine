import pygame

__all__ = ["SoundSystem"]


class SoundSystem:
    def __init__(self):
        self.volume = 100

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, volume):
        if volume < 0 or volume > 100:
            raise ValueError("Volume can't be lower than 0 and bigger than 100")
        self.__volume = volume

    @property
    def number_channel(self):
        return pygame.mixer.get_num_channels()

    @number_channel.setter
    def number_channel(self, nb):
        pygame.mixer.set_num_channels(nb)

    def play(self, file):
        sound = pygame.mixer.Sound(file)
        sound.set_volume(self.volume/100)
        sound.play()
