import tkinter as tk


class CheckBox(tk.Button):
    def __init__(self, master, *args, **kwargs):
        tk.Button.__init__(self, master, **kwargs)
        self.master = master

        self.checked = False
        self.bind("<Button-1>", lambda _: self.switch(_))

    def switch(self, event):
        if self.checked is False:
            self.checked = True
            self['text'] = u'\u2713'
        else:
            self.checked = False
            self['text'] = ''
