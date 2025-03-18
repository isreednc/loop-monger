from tkinter import *
from tkinter import ttk

def init_window():
    root = Tk()
    frame = ttk.Frame(root, padding=10)
    frame.grid()
    ttk.Label(frame, text="Loop Monger").grid(column=0, row=0)
    ttk.Button(frame, text="Quit", command=root.destroy).grid(column=1, row=0)
    root.mainloop()

if __name__ == "__main__":
    init_window()


