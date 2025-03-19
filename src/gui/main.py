from tkinter import *
from tkinter import ttk
import sys
import os

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

from sounds import get_sounds
from mixer import play_wav
from audio import AudioStream

#TODO: Add config to choose sound api and output device
SOUND_API = 'MME'
OUTPUT_DEVICE = 'CABLE Input (VB-Audio Virtual'

class MainWindow:
    def __init__(self):
        self.audio_stream = AudioStream()
        self.audio_stream.open_stream(SOUND_API, OUTPUT_DEVICE)
        self.root = Tk()
        self.frame = ttk.Frame(self.root, padding=10)
        self.frame.grid()
        ttk.Label(self.frame, text="Loop Monger").grid(column=0, row=0)
        ttk.Button(self.frame, text="Quit", command=self.root.destroy).grid(column=1, row=0)
        next_index = self.create_buttons()
        self.root.mainloop()
        self.audio_stream.close()

    def create_buttons(self):
        index = 0
        sounds = get_sounds()

        for sound in sounds:
            ttk.Button(self.frame, text=sound, command=lambda s=sound:
                       self.audio_stream.play_wav(s)).grid(column=int(index%5), row=int((index/5))+1)
            index += 1
        return index

if __name__ == "__main__":
    window = MainWindow()

