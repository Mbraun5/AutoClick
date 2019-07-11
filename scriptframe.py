import tkinter as tk
import scriptButtonFrame as sbf


class ScriptFrame(tk.Frame):
    def __init__(self, master, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)

        self.pixel = tk.PhotoImage(width=1, height=1)

        self.scrollbar = tk.Scrollbar(self, orient='vertical')
        self.scrollbar.pack(fill='y', side='right', expand=False, padx="0 82")

        self.titleFrame = tk.Frame(self, bg='#FFFFFF', height=20)
        self.titleFrame.pack(anchor='n', fill='x')

        titles = ['#', 'Action', 'X-Coor', 'Y-Coor', 'Cursor Back?', 'Delay (ms)', 'Repeat', 'Comment']
        self.dimensions = [5, 15, 5, 5, 15, 10, 10, 10]
        self.title_labels = []
        for index, title in enumerate(titles):
            new_label = tk.Label(self.titleFrame, text=title, width=self.dimensions[index], font=('Helvetica', '9'),
                                 anchor='w')
            new_label.pack(side='left', padx=5)
            self.title_labels.append(new_label)
        self.title_labels[len(titles)-1].pack(side='left', fill='x', expand=True, padx="5 0")

        self.canvas = tk.Canvas(self, bd=0, yscrollcommand=self.scrollbar.set, highlightthickness=0, bg='#ffffff')
        self.canvas.pack(fill='both', expand=True)
        self.scrollbar.config(command=self.canvas.yview)

        self.canvas.xview_moveto(0)
        self.canvas.yview_moveto(0)

        self.commandsFrame = tk.Frame(self.canvas)
        self.commandsFrameWindow = self.canvas.create_window(0, 0, window=self.commandsFrame, anchor='nw')

        self.indexFrame = tk.Frame(self.commandsFrame)
        self.indexFrame.pack(side='left', anchor='w', fill='y', expand=False)
        self.valueFrame = tk.Frame(self.commandsFrame)
        self.valueFrame.pack(side='right', anchor='w', fill='both', expand=True)

        self.commandsFrame.bind('<Configure>', self.configure_interior_window)
        self.canvas.bind('<Configure>', self.configure_canvas)
        self.bind('<MouseWheel>', self.mouse_event)

        '''
        
        for i in range(10):
            label = tk.Label(self.commandsFrame, text='label {}'.format(i))
            label.pack(fill='both', expand=True)
            label.bind("<MouseWheel>", self.mouse_event)
        self.textFrame = tk.Frame(self.canvas, bg='#abcabc', height=20)
        self.textFrame.pack(anchor='n', fill='x')

        self.newbutton = tk.Button(self.canvas, text='HAHAsdfsdfsdfsdfsdf', anchor='w')
        self.newbutton.config(width=5)
        self.newbutton.pack(anchor='nw')
        '''

        self.cvrFrame = tk.Frame(self.master, width=103, bg='#465362')
        self.cvrFrame.grid(row=2, column=0, sticky='nse')

        self.btnFrame = tk.Frame(self.master, bg='#465362')
        self.btnFrame.grid(row=2, column=0, sticky='e')

        self.btnPaddingy = "0 10"
        self.btnPaddingx = "5 5"
        self.startButton = tk.Button(self.btnFrame, text='Start', font=('Helvetica', '9'), image=self.pixel, width=85,
                                     compound='center')
        self.startButton.pack(anchor='center', expand=True, fill='x', pady="10 10", padx=self.btnPaddingx,)
        self.upButton = tk.Button(self.btnFrame, text='Move Up', font=('Helvetica', '9'))
        self.upButton.pack(anchor='center', expand=True, fill='x', pady=self.btnPaddingy, padx=self.btnPaddingx)
        self.downButton = tk.Button(self.btnFrame, text='Move Down', font=('Helvetica', '9'))
        self.downButton.pack(anchor='center', expand=True, fill='x', pady=self.btnPaddingy, padx=self.btnPaddingx)
        self.deleteButton = tk.Button(self.btnFrame, text='Delete', font=('Helvetica', '9'))
        self.deleteButton.pack(anchor='center', expand=True, fill='x', pady=self.btnPaddingy, padx=self.btnPaddingx)
        self.deleteAllButton = tk.Button(self.btnFrame, text='Delete All', font=('Helvetica', '9'))
        self.deleteAllButton.pack(anchor='center', expand=True, fill='x', pady=self.btnPaddingy, padx=self.btnPaddingx)

        # self.test = sbf.ScriptButtonFrame(self.commandsFrame, self.dimensions, bg='#fdda33')
        # self.test.pack(fill='x', expand=True)

        self.config()
        self.actions = []

    def config(self):
        config = {'bg': '#000F08',
                  'fg': '#F4FFFD',
                  'borderwidth': 1,
                  'activebackground': '#092327',
                  'activeforeground': '#86E7B8'
                  }
        for button in self.btnFrame.winfo_children():
            button.config(config)

    def configure_interior_window(self, event):
        size = (self.commandsFrame.winfo_reqwidth(), self.commandsFrame.winfo_reqheight())
        self.canvas.config(scrollregion='0 0 %s %s' % size)
        self.commandsFrame.bind('<Configure>', self.configure_interior_window)

    def configure_canvas(self, event):
        if self.commandsFrame.winfo_reqwidth() != self.canvas.winfo_reqwidth():
            self.canvas.itemconfigure(self.commandsFrameWindow, width=self.canvas.winfo_width())
        self.canvas.bind('<Configure>', self.configure_canvas)

    def mouse_event(self, event):
        delta = -1 * int(event.delta / 120)
        self.canvas.yview("scroll", delta, "units")

    def add_script(self, location, *args):
        # new_script = sbf.ScriptButtonFrame(self.commandsFrame, self.dimensions, len(self.actions) + 1, args)
        # new_script.pack(anchor='w')
        num_btn = tk.Button(self.indexFrame, width=self.dimensions[0], text=len(self.actions) + 1, anchor='w', padx=6,
                            bg='#ffffff', borderwidth=0, relief='flat')
        num_btn.pack()
        new_script = sbf.ScriptButtonFrame(self.valueFrame, self.dimensions, args)
        if location == 'bottom':
            new_script.pack(anchor='w')
            self.actions.append(new_script)
        elif location == 'top':
            for elem in self.actions:
                elem.pack_forget()
            new_script.pack(anchor='w')
            for elem in self.actions:
                elem.pack(anchor='w')
            self.actions.insert(0, new_script)
        else:
            pass


''' Double click handler
from tkinter import *

def mouse_click(event):
    #  delay mouse action to allow for double click to occur
    aw.after(300, mouse_action, event)

def double_click(event):
    # set the double click status flag
    global double_click_flag
    double_click_flag = True

def mouse_action(event):
    global double_click_flag
    if double_click_flag:
        print('double mouse click event')
        double_click_flag = False
    else:
        print('single mouse click event')

root = Tk()
aw = Canvas(root, width=200, height=100, bg='grey')
aw.place(x=0, y=0)

double_click_flag = False
aw.bind('<Button-1>', mouse_click) # bind left mouse click
aw.bind('<Double-1>', double_click) # bind double left clicks
aw.mainloop()
'''