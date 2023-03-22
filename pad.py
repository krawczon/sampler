from player import Player
from settings import Settings

class Pad():
    def __init__(self, settings, filename):
        
        self.s = settings
        self.filename = filename
        self.rate = 44100
        self.volume = 1
        self.samples = []
        for i in range(2):
            sample = Player(self.s, self.filename, self.rate, self.volume)
            self.samples.append(sample)

    def play(self):
        if self.samples[0].is_playing == False:
            self.samples[1].stop()
            self.samples[0].play()
            sample = Player(self.s, self.filename, self.rate, self.volume)
            self.samples[1] = sample
        else:
            self.samples[0].stop()
            self.samples[1].play()
            sample = Player(self.s, self.filename, self.rate, self.volume)
            self.samples[0] = sample

    def stop(self):
        self.samples[0].stop()
        self.samples[1].stop()

    def update(self):

        sample = Player(self.s, self.filename, self.rate, self.volume)
        self.samples[0] = sample
        self.samples[1] = sample
