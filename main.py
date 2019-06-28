import pyautogui as pag
import tkinter as tk
import time as t
import navbar as nav
import shortcutframe as sf
import keyboard


class Main(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.configure(background='#465362')
        self.grid_columnconfigure(0, weight=1)

        self.navbar = nav.NavBar(self)
        self.navbar.grid(row=0, column=0, sticky='ew')

        self.shortcut_frame = sf.ShortcutFrame(self)
        self.shortcut_frame.grid(row=1, column=0, sticky='n')

        self.bind('<Alt_L>f', self.navbar.keyevent)
        self.bind('<Alt_L>e', self.navbar.keyevent)
        self.bind('<Alt_L>v', self.navbar.keyevent)
        self.bind('<KeyRelease>', self.navbar.altevent)
        self.bind('<ButtonRelease-1>', self.navbar.buttonevent)


if __name__ == "__main__":
    root = Main()
    root.geometry('600x400+{}+{}'.format(int(pag.size()[0] / 2 - 500/2), int(pag.size()[1] / 2 - 350/2)))
    root.minsize(250, 0)
    root.title('Automation')
    root.mainloop()
