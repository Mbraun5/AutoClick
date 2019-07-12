import pyautogui as pag
import tkinter as tk
import navbar as nav
import shortcutframe as scf
import footer as f
import newactionframe as naf
import scriptframe as sf
from PIL import ImageTk, Image


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
        self.newActionFrame.optionMenu.add_options()

        self.script_frame = sf.ScriptFrame(self)
        self.script_frame.grid(row=2, column=0, sticky='news', padx=20, pady=20)

        self.shortcut_frame = scf.ShortcutFrame(self)
        self.shortcut_frame.grid(row=3, column=0, sticky='sew')

        self.footer = f.Footer(self)
        self.footer.grid(row=4, column=0, sticky='sew')

        '''
        self.om = om.OptionMenu(self, '#000F08', '#F4FFFD', '#092327', '#86E7B8')
        self.om.grid(row=1, column=0, sticky="nw", padx=98, pady=74)
        tk.Misc.lift(self.om, aboveThis=None)
        
        buttons = []
        for i in range(24):
            buttons.append(tk.Button(self.om.btnFrame, text='haha' + str(i)))
            buttons[-1].pack(fill='x')
            buttons[-1].bind('<MouseWheel>', self.om.mouse_event)
        '''

        self.bind('<Alt_L>f', self.navbar.keyevent)
        self.bind('<Alt_L>e', self.navbar.keyevent)
        self.bind('<Alt_L>v', self.navbar.keyevent)
        self.bind('<Alt_R>f', self.navbar.keyevent)
        self.bind('<Alt_R>e', self.navbar.keyevent)
        self.bind('<Alt_R>v', self.navbar.keyevent)
        self.bind('<KeyRelease>', self.key_release_event)
        self.bind('<ButtonRelease-1>', self.button_release_event)
        self.bind('<Button-1>', self.button_click_event)
        self.bind('<Shift-Button-1>', self.shift_event)

    def button_release_event(self, event):
        self.navbar.button_event(event)
        self.shortcut_frame.button_event()
        self.newActionFrame.button_event()
        del event

    def key_release_event(self, event):
        self.navbar.altevent(event)
        self.newActionFrame.key_event(event)

    def button_click_event(self, event):
        self.script_frame.button_event(event)

    def shift_event(self, event):
        self.script_frame.shift_click_event(event)

    def get_protected(self):
        return self._w


if __name__ == "__main__":
    root = Main()
    img = ImageTk.PhotoImage(Image.open('sprites/icon.png'))
    root.tk.call('wm', 'iconphoto', root.get_protected(), img)
    root.geometry('830x600+{}+{}'.format(int(pag.size()[0] / 2 - 500/2), int(pag.size()[1] / 2 - 350/2)))
    root.minsize(250, 0)
    root.title('Automation')
    root.mainloop()

    '''
    Image Editing
    pic = Image.open('sprites/icon_orig.png').convert('RGB')
    for i in range(48):
        for j in range(48):
            try:
                r, g, b = pic.getpixel((i, j))
            except:
                print(i, j)
                exit()
            print(r, g, b)
            if (r, g, b) != (71, 112, 76):
                pic.putpixel((i, j), (56, 78, 50))
                #pic.putpixel((i, j), (0, 0, 0))
            else:
                pic.putpixel((i, j), (255, 255, 255))
    pic.save('sprites/icon.png')
    '''