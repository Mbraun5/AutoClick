import tkinter as tk
import menu as m


'''
class OptionMenu(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master

        self.scrollbar = tk.Scrollbar(self, command=self.on_vsb, orient='vertical')
        self.scrollbar.pack(side='right', expand=True, fill='y')
        self.listbox = tk.Listbox(self, yscrollcommand=self.scrollbar.set, width=35)
        self.listbox.pack(side='left')

        self.listbox.bind("<MouseWheel>", self.mouse_wheel)

        self.add_parameters()
        self.config()

    def on_vsb(self, *args):
        self.listbox.yview(*args)

    def mouse_wheel(self, event):
        if event.keycode == 38:
            delta = -1
        elif event.keycode == 40:
            delta = 1
        else:
            delta = int(event.delta / 120)
        self.listbox.yview("scroll", delta, "units")

    def config(self):
        config = {'background': '#000F08',
                  'foreground': '#F4FFFD',
                  'font': ('Helvetica', '9'),
                  'borderwidth': 0,
                  }
        self.listbox.config(config)

    def post(self, x, y):
        self.grid(row=1, column=0, sticky='nw', padx=x, pady=y)

    def unpost(self):
        self.grid_remove()

    def add_parameters(self):
        for i in range(20):
            self.listbox.insert('end', 'haha{}'.format(i))
    '''


class OptionMenu(tk.Canvas):
    def __init__(self, *args, **kwargs):
        tk.Canvas.__init__(self)
        self.passiveConfig = {'bg': args[1],
                              'fg': args[2],
                              'activebackground': args[1],
                              'activeforeground': args[2]
                              }
        self.activeConfig = {'bg': args[3],
                             'fg': args[4],
                             'activebackground': args[3],
                             'activeforeground': args[4]
                             }
        self['bg'] = self.passiveConfig['bg']
        self['highlightbackground'] = '#404040'
        self['highlightthickness'] = 1
        self.command_list = []
        self.num_elements = 0
        self.activeIndex = None
        self.config(height=100, width=226)
        self.pack_propagate(False)
        self.btnFrame = tk.Frame(self)
        self.create_window((0, 0), window=self.btnFrame, anchor='nw')
        self.scrllbar = tk.Scrollbar(self, orient='vertical')
        self.bind('<Configure>', self.on_configure)
        self.pixel = tk.PhotoImage(height=1, width=1)
        self.add_options()

    def add_command(self, label=None, command=None):
        newButton = tk.Button(self.btnFrame, text=label, command=command, borderwidth=0, image=self.pixel, **self.passiveConfig, justify='center',
                              anchor='w', padx=5, width=219, height=20, compound='center')
        newButton.bind('<Enter>', lambda _: self.hover_on(newButton))
        newButton.bind('<Leave>', lambda _: self.hover_off())
        newButton.bind('<MouseWheel>', self.mouse_wheel)
        newButton.grid(row=self.num_elements, column=0, sticky='we')
        self.num_elements += 1
        self.command_list.append(newButton)

    def add_separator(self):
        newButton = tk.Button(self, text='-' * 100, state='disabled', borderwidth=0, **self.passiveConfig, anchor='w',
                              font="Helvetica 2", justify='left')
        newButton.grid(row=self.num_elements, column=0, sticky='we')
        self.num_elements += 1

    def post(self, padx, pady):
        self.grid(row=1, column=0, sticky="nw", padx=padx, pady=pady)
        tk.Misc.lift(self, aboveThis=None)
        self.activeIndex = -1

    def unpost(self):
        self.grid_remove()
        self.activeIndex = None
        self.master.newActionFrame.optionButton.config(self.master.newActionFrame.passiveConfig)

    def hover_on(self, button):
        button.config(**self.activeConfig)
        if self.activeIndex != -1:
            try:
                self.command_list[self.activeIndex].config(**self.passiveConfig)
            except TypeError:
                return
        self.activeIndex = self.command_list.index(button)

    def hover_off(self):
        if self.activeIndex != -1 and self.activeIndex is not None:
            self.command_list[self.activeIndex].config(**self.passiveConfig)
            self.activeIndex = -1

    def change_index(self, direction):
        if direction == "up":
            if self.activeIndex == 0:
                return
            if self.activeIndex != -1:
                self.command_list[self.activeIndex].config(**self.passiveConfig)
            else:
                self.activeIndex = 0
            self.activeIndex = (self.activeIndex + len(self.command_list) - 1) % len(self.command_list)
            self.command_list[self.activeIndex].config(**self.activeConfig)
        else:
            if self.activeIndex == len(self.command_list) - 1:
                return
            if self.activeIndex != -1:
                self.command_list[self.activeIndex].config(**self.passiveConfig)
            self.activeIndex = (self.activeIndex + 1) % len(self.command_list)
            self.command_list[self.activeIndex].config(**self.activeConfig)

    def mouse_wheel(self, event):
        if self.master.newActionFrame.optionMenuActive:
            if event.keycode == 38:
                self.change_index("up")
                delta = -2
            elif event.keycode == 40:
                self.change_index("down")
                delta = 2
            else:
                delta = -1 * int(event.delta / 120)
            self.yview("scroll", delta, "units")

    def on_configure(self, event):
        self.configure(scrollregion=self.bbox('all'))

    def add_options(self):
        pass
