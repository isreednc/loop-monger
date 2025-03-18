from tkinter import *
from tkinter import ttk
import sys
import os

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

from sounds import get_sounds
from mixer import play_wav



def init_window():
    root = Tk()
    frame = ttk.Frame(root, padding=10)
    frame.grid()
    ttk.Label(frame, text="Loop Monger").grid(column=0, row=0)
    ttk.Button(frame, text="Quit", command=root.destroy).grid(column=1, row=0)
    create_buttons(ttk, frame)
    root.mainloop()

def create_buttons(tk, frame):
    index = 0
    sounds = get_sounds()

    #TODO: Refactor play_wav to only take the wav file.
    for sound in sounds:
        tk.Button(frame, text=sound, command=play_wav(sound, )).grid(column=index%5, row=(index/5)+1)
        index += 1
    return index


if __name__ == "__main__":
    init_window()


