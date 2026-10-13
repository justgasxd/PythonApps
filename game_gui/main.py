# main.py
import tkinter as tk

from gui import GuessGameApp

if __name__ == '__main__':
    root = tk.Tk()
    app = GuessGameApp(root)
    root.mainloop()