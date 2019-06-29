import pyautogui as pag
import tkinter as tk
import time as t
import navbar as nav
import shortcutframe as sf
import footer as f
import newactionframe as naf
import keyboard


class Main(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.configure(background='#465362')
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

        self.navbar = nav.NavBar(self)
        self.navbar.grid(row=0, column=0, sticky='new')

        self.newActionFrame = naf.NewActionFrame(self)
        self.newActionFrame.grid(row=1, column=0, sticky='new')

        self.shortcut_frame = sf.ShortcutFrame(self)
        self.shortcut_frame.grid(row=2, column=0, sticky='sew')

        self.footer = f.Footer(self)
        self.footer.grid(row=3, column=0, sticky='sew')

        self.bind('<Alt_L>f', self.navbar.keyevent)
        self.bind('<Alt_L>e', self.navbar.keyevent)
        self.bind('<Alt_L>v', self.navbar.keyevent)
        self.bind('<KeyRelease>', self.navbar.altevent)
        self.bind('<ButtonRelease-1>', self.button_event)

    def button_event(self, event):
        self.navbar.button_event()
        self.shortcut_frame.button_event()
        del event


if __name__ == "__main__":
    root = Main()
    root.geometry('600x400+{}+{}'.format(int(pag.size()[0] / 2 - 500/2), int(pag.size()[1] / 2 - 350/2)))
    root.minsize(250, 0)
    root.title('Automation')
    root.mainloop()
