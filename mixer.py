import pygame

class Mixer:
    def __init__(self, game):
        self.game = game
        self.volume = 1

    def play(self, circulate=True):
        pygame.mixer.music.set_volume(self.volume)
        if circulate:
            if pygame.mixer.music.get_busy() == False:
                pygame.mixer.music.play()
        else:
            pygame.mixer.music.play()

    def reload(self, path=None):
        if not path == None:
            pygame.mixer.music.unload()
            pygame.mixer.music.load(path)

    def pause(self):
        pygame.mixer.music.pause()

    def unpause(self):
        pygame.mixer.music.unpause()

    def get_pos(self):
        return pygame.mixer.music.get_pos()

    def set_pos(self, pos=0):
        pygame.mixer.music.set_pos(pos)

    def stop(self):
        pygame.mixer.music.stop()

