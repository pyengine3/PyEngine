import pygame
from pyengine.Exceptions import NoObjectError

__all__ = ["MusicSystem"]


class MusicSystem:
    def __init__(self, state):
        self.queue = []
        self.ENDSOUND = 231
        self.loop = False
        pygame.mixer.music.set_endevent(self.ENDSOUND)

    def next_song(self):
        if len(self.queue):
            pygame.mixer.music.load(self.queue[0])
            pygame.mixer.music.play()
            if self.loop:
                self.queue.append(self.queue[0])
            del self.queue[0]

    def clear_queue(self):
        self.queue = []

    def set_loop(self, loop):
        self.loop = loop

    def play(self):
        if len(self.queue):
            pygame.mixer.music.load(self.queue[0])
            pygame.mixer.music.play()
            if self.loop:
                self.queue.append(self.queue[0])
            del self.queue[0]
        else:
            raise NoObjectError("MusicSystem have any music to play")

    def add(self, file):
        self.queue.append(file)

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

