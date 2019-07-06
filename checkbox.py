import tkinter as tk


class CheckBox(tk.Button):
    def __init__(self, master, *args, **kwargs):
        tk.Button.__init__(self, master, *args, **kwargs)
        self.master = master

        self.checked = False
        self.bind("<Button-1>", lambda _: self.switch())
        self.config(font=('Helvetica', '11', 'bold'), text='.', foreground='#FFFFFF')

    def switch(self):
        if not self.checked:
            self.config(font=('Helvetica', '7', 'bold'), text=u'\u2713', foreground='#000000')
            self.checked = True
        else:
            self.config(font=('Helvetica', '11', 'bold'), text='.', foreground='#FFFFFF')
            self.checked = False
