from tkinter import *


class Lines(Frame):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        canvas.create_line(15, 100, 980, 100)
        canvas.create_line(15, 600, 980, 600)

        canvas.pack(fill=BOTH, expand=1)
