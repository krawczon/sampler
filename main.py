from kivy.app import App
from sampler import Sampler
from threading import Thread
from gui import Screen

class Sampler_GUI(App):
    def build(self):
        screen = Screen(sampler)
        return screen

if __name__ == '__main__':
    sampler = Sampler()
    thread = Thread(target = sampler.run)
    thread.start()
    sampler_gui = Sampler_GUI()
    sampler_gui.run()
