import pyaudio
import wave
import time
from threading import Thread
from settings import Settings
import numpy as np

class Player(pyaudio.PyAudio):
    def __init__(self, settings, filename, rate, volume):
        super().__init__()

        self.s = settings
        self.volume = volume
        self.rate = rate
        self.filename = filename
        self.wf = wave.open(self.filename, 'rb')   # dtype = 'float32'
        self.trigger = True
        self.is_playing = False
        self.status = None
        
        self.stream = self.open(
                format = self.get_format_from_width(self.wf.getsampwidth()),
                channels = self.wf.getnchannels(),
                rate = self.rate,
                frames_per_buffer = self.s.buffer_size,
                start = False,
                output = True,
                stream_callback = self.callback)

    def callback(self, in_data, frame_count, time_info, status):
        data = self.wf.readframes(frame_count)
        data_int16 = np.frombuffer(data, dtype=np.int16)//self.volume
        new_data = data_int16.tobytes()

        return (new_data, pyaudio.paContinue)
    
    def init_stream(self):
#        self.stream.start = True
        self.stream.start_stream()
        while self.stream.is_active():
            time.sleep(0.1)
            if self.trigger == False:
                break
        self.status = 'done'
#        self.wf.rewind()
#        self.stream.stop_stream()
        self.stream.close()
        self.wf.close()

    def play(self):
        self.is_playing = True
        self.trigger = True
        thread = Thread(target = self.init_stream)
        thread.start()

    def stop(self):
        self.trigger = False

