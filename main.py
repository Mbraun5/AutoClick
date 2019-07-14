import pyautogui as pag
import tkinter as tk
import navbar as nav
import shortcutframe as scf
import footer as f
import newactionframe as naf
import scriptframe as sf
from PIL import ImageTk, Image

import pynput.keyboard as pk
import pynput.mouse as pm
import time
from functools import wraps
from timeit import default_timer as timer


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
        self.bind('<Control_L>c', self.script_frame.copy_event)
        self.bind('<Control_R>c', self.script_frame.copy_event)
        self.bind('<Control_L>v', self.script_frame.paste_event)
        self.bind('<Control_R>v', self.script_frame.paste_event)
        self.bind('<Control_L>a', self.script_frame.select_all_event)
        self.bind('<Control_R>a', self.script_frame.select_all_event)
        self.bind('<Delete>', self.script_frame.delete)

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
    events = []
    stopFlag = False

    start = timer()

    def time_difference(func):
        @wraps(func)
        def wrapper_inner(*args, **kwargs):
            global start
            end = timer()
            elapsed = end - start
            # print(elapsed)
            events.append(('sleep', elapsed))
            func(*args, **kwargs)
            start = timer()
        return wrapper_inner

    @time_difference
    def key_press(key):
        global stopFlag
        global k_listener
        global m_listener
        global a
        if key == pk.Key.f11:
            stopFlag = True
            k_listener.stop()
            m_listener.stop()
        events.append(('press', key))


    @time_difference
    def key_release(key):
        print('here')
        events.append(('release', key))

    @time_difference
    def on_move(x, y):
        events.append(('m_move', (x, y)))

    @time_difference
    def on_click(x, y, button, pressed):
        if pressed:
            events.append(('m_press', button))
        else:
            events.append(('m_release', button))

    @time_difference
    def on_scroll(x, y, dx, dy):
        events.append(('m_scroll', (dx, dy)))
        print(x, y, dx, dy)

    def k_listen():
        global k_listener
        k_listener = pk.Listener(
            on_press=key_press,
            on_release=key_release
        )
        k_listener.start()

    def m_listen():
        global m_listener
        m_listener = pm.Listener(
            on_move=on_move,
            on_click=on_click,
            on_scroll=on_scroll
        )
        m_listener.start()

    k = pk.Controller()
    m = pm.Controller()

    k_listen()
    m_listen()

    while not stopFlag:
        time.sleep(0.1)

    for i in range(len(events)):
        if events[i][0] == 'press':
            k.press(events[i][1])
        elif events[i][0] == 'release':
            k.release(events[i][1])
        elif events[i][0] == 'm_move':
            m.position = events[i][1]
        elif events[i][0] == 'm_press':
            m.press(events[i][1])
        elif events[i][0] == 'm_release':
            m.release(events[i][1])
        elif events[i][0] == 'm_scroll':
            m.scroll(events[i][1][0], events[i][1][1])
        else:
            time.sleep(events[i][1])

    root = Main()
    img = ImageTk.PhotoImage(Image.open('sprites/icon.png'))
    root.tk.call('wm', 'iconphoto', root.get_protected(), img)
    root.geometry('830x600+{}+{}'.format(int(pag.size()[0] / 2 - 500/2), int(pag.size()[1] / 2 - 350/2)))
    root.minsize(250, 0)
    root.title('Automation')
    root.mainloop()
