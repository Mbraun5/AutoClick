import tkinter as tk
import pyautogui as pag


class Footer(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self)
        self.configure(background='#011936', height=20)
        self.master = master

        self.footer_text = tk.Label(self, height=1, bg='#011936', fg='#F4FFFD', font=('Helvetica', '8'))
        self.footer_text.pack(side='left')

        self.screenInfo = tk.Label(self, height=1, bg='#011936', fg='#F4FFFD', font=('Helvetica', '8'))
        self.screenInfo.pack(side='right')
        self.screenInfo.config(text='Screen Resolution: {}x{}'.format(pag.size()[0], pag.size()[1]))

        self.fill_footer()

    def fill_footer(self):
        self.footer_text.config(text='Mouse Cursor Location: X = {}, Y = {}'.format(pag.position()[0],
                                                                                    pag.position()[1]))
        self.after(75, self.fill_footer)
