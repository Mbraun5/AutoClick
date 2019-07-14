import tkinter as tk
import pyautogui as pag
from config import Config


class Footer(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)

        bg_color = Config.nav_bg_color()
        self.config(bg=bg_color, height=20)

        config = {'height': 1,
                  'bg': bg_color,
                  'fg': Config.light_text_color(),
                  'font': Config.font_small()
                  }
        self.footer_text = tk.Label(self, config)
        self.screenInfo = tk.Label(self, config)

        self.footer_text.pack(side='left')
        self.screenInfo.pack(side='right')

        self.fill_footer()
        self.screenInfo.config(text='Screen Resolution: {}x{}'.format(pag.size()[0], pag.size()[1]))

    def fill_footer(self):
        self.footer_text.config(text='Mouse Cursor Location: X = {}, Y = {}'.format(pag.position()[0],
                                                                                    pag.position()[1]))
        self.after(75, self.fill_footer)
