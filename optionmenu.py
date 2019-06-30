import tkinter as tk


class OptionMenu(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self)
        self.master = master