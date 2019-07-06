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
        self.bind('<Alt_R>f', self.navbar.keyevent)
        self.bind('<Alt_R>e', self.navbar.keyevent)
        self.bind('<Alt_R>v', self.navbar.keyevent)
        self.bind('<KeyRelease>', self.key_release_event)
        self.bind('<ButtonRelease-1>', self.button_event)

    def button_event(self, event):
        self.navbar.button_event()
        self.shortcut_frame.button_event()
        self.newActionFrame.button_event()
        del event

    def key_release_event(self, event):
        self.navbar.altevent(event)
        self.newActionFrame.key_event(event)


if __name__ == "__main__":
    root = Main()
    root.geometry('600x400+{}+{}'.format(int(pag.size()[0] / 2 - 500/2), int(pag.size()[1] / 2 - 350/2)))
    root.minsize(250, 0)
    root.title('Automation')
    root.mainloop()



'''
import tkinter as tk


def on_configure(event):
    # update scrollregion after starting 'mainloop'
    # when all widgets are in canvas
    canvas.configure(scrollregion=canvas.bbox('all'))

def mouse_wheel(event):
    if event.num == 4:
        print("4")
        delta = 0.0005
    elif event.num == 5:
        print("5")
        delta = -0.0005
    else:
        delta = int(event.delta / 120)
    canvas.yview("scroll", delta, "units")
    return "break"

root = tk.Tk()

# --- create canvas with scrollbar ---

canvas = tk.Canvas(root)
canvas.pack(side=tk.LEFT)

scrollbar = tk.Scrollbar(root, command=canvas.yview)
scrollbar.pack(side=tk.LEFT, fill='y')

canvas.configure(yscrollcommand = scrollbar.set)

# update scrollregion after starting 'mainloop'
# when all widgets are in canvas
canvas.bind('<Configure>', on_configure)

# --- put frame in canvas ---

frame = tk.Frame(canvas)
canvas.create_window((0,0), window=frame, anchor='nw')

# --- add widgets in frame ---

l = tk.Label(frame, text="Hello", font="-size 50")
l.pack()
l.bind("<MouseWheel>", mouse_wheel)

l = tk.Label(frame, text="World", font="-size 50")
l.pack()
l.bind("<MouseWheel>", mouse_wheel)
l = tk.Label(frame, text="Test text 1\nTest text 2\nTest text 3\nTest text 4\nTest text 5\nTest text 6\nTest text 7\nTest text 8\nTest text 9", font="-size 20")
l.pack()
l.bind("<MouseWheel>", mouse_wheel)
frame.bind("<MouseWheel>", mouse_wheel)
canvas.bind("<MouseWheel>", mouse_wheel)

# --- start program ---

root.mainloop()


class ChatRoom:
    def __init__(self):
        self.tk = tk.Tk()
        self.tk.title("Secure Chat")
        self.tk.configure(background="#EFEFEF")
        self.tk.resizable(False, False)

        self.frame = None
        self.scroll = None
        self.listbox = None
        self.listbox_two = None
        self.entryframe = None
        self.entry = None

        self.screen()
        self.start_loop()

    def screen(self):
        self.frame = tk.Frame(self.tk)
        self.frame.pack(side='top', expand=True, fill='x')

        frame_one = tk.Frame(self.frame)
        frame_one.pack(side='left', expand=True, fill='x')
        frame_two = tk.Frame(self.frame)
        frame_two.pack(side='right', expand=True, fill='x')

        self.scroll = tk.Scrollbar(self.frame, bd=0, command=self.on_vsb, orient='vertical')
        #self.scroll.pack(side='left', fill='y', expand=True)

        self.listbox = tk.Listbox(frame_one, bg='#EFEFEF', bd=0, yscrollcommand=self.scroll.set, width=25, height=25)
        self.listbox.pack(expand=True, fill='x', side='left')

        self.listbox_two = tk.Listbox(frame_one, bg='#EFEFEF', bd=0, yscrollcommand=self.scroll.set, width=75, height=25)
        self.listbox_two.pack(expand=True, fill='x', side='right')

        self.listbox.bind("<MouseWheel>", self.mouse_wheel)
        self.listbox_two.bind("<MouseWheel>", self.mouse_wheel)
        self.listbox.bind("<Button-4>", self.mouse_wheel)
        self.listbox_two.bind("<Button-4>", self.mouse_wheel)
        self.listbox.bind("<Button-5>", self.mouse_wheel)
        self.listbox_two.bind("<Button-5>", self.mouse_wheel)

        for i in range(50):
            self.listbox.insert('end', "hi{}".format(i))

        # self.listbox.bind("<Button-1>", lambda x: self.left_click(self.listbox))
        # self.listbox_two.bind("<Button-1>", lambda x: self.left_click(self.listbox_two))

    def set_title(self, title):
        self.tk.title("{}".format(title))

    def send_info(self):
        return self.listbox, self.listbox_two, self.entry

    def left_click(self, box):
        if box == self.listbox:
            a = self.listbox.curselection()
            print(a)
            self.listbox_two.selection_clear(0, 'end')
            self.listbox_two.selection_set(a[0], a[1]-1)
        else:
            a = self.listbox_two.curselection()
            self.listbox.selection_clear(0, 'end')
            self.listbox.selection_set(a[0], a[1])

    def start_loop(self):
        self.tk.mainloop()

    def on_vsb(self, *args):
        self.listbox.yview(*args)
        self.listbox_two.yview(*args)

    def mouse_wheel(self, event):
        if event.num == 4:
            delta = -1
        elif event.num == 5:
            delta = 1
        else:
            delta = int(event.delta/120)
        self.listbox.yview("scroll", delta, "units")
        self.listbox_two.yview("scroll", delta, "units")
        return "break"
'''