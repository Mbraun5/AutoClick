import tkinter as tk


class OptionMenu(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, **kwargs)
        self.master = args[0]

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

        self.scrollbar = tk.Scrollbar(self, orient='vertical')
        # self.scrollbar.pack(fill='y', side='right', expand='false')
        self.canvas = tk.Canvas(self, bd=0, yscrollcommand=self.scrollbar.set, width=226, height=200,
                                highlightthickness=0)
        self.canvas.pack(fill='both', side='left', expand=True)
        self.scrollbar.config(command=self.canvas.yview)

        self.canvas.xview_moveto(0)
        self.canvas.yview_moveto(0)

        self.btnFrame = tk.Frame(self.canvas)
        self.btnFrameWindow = self.canvas.create_window(0, 0, window=self.btnFrame, anchor='nw')
        self.btnFrame.bind('<Configure>', self.configure_interior_window)
        self.canvas.bind('<Configure>', self.configure_canvas)

        self.command_list = []
        self.num_elements = 0
        self.activeIndex = None
        self.pixel = tk.PhotoImage(height=1, width=1)

    def configure_interior_window(self, event):
        size = (self.btnFrame.winfo_reqwidth(), self.btnFrame.winfo_reqheight())
        self.canvas.config(scrollregion='0 0 %s %s' % size)
        self.btnFrame.bind('<Configure>', self.configure_interior_window)

    def configure_canvas(self, event):
        if self.btnFrame.winfo_reqwidth() != self.canvas.winfo_reqwidth():
            self.canvas.itemconfigure(self.btnFrameWindow, width=self.canvas.winfo_width())
        self.canvas.bind('<Configure>', self.configure_canvas)

    def mouse_event(self, event):
        if self.winfo_reqheight() < self.canvas.winfo_reqheight():
            return
        delta = -1 * int(event.delta / 120)
        self.canvas.yview("scroll", delta, "units")

    def add_command(self, label):
        new_button = tk.Button(self.btnFrame, text=label, borderwidth=0, image=self.pixel, **self.passiveConfig,
                               justify='center', anchor='w', padx=5, width=226, height=19, compound='center',
                               command=lambda: self.master.newActionFrame.set_option_button(label))
        new_button.bind('<Enter>', lambda _: self.hover_on(new_button))
        new_button.bind('<Leave>', lambda _: self.hover_off())
        new_button.bind('<MouseWheel>', self.mouse_event)
        new_button.grid(row=self.num_elements, column=0, sticky='we')
        self.num_elements += 1
        self.command_list.append(new_button)

    def add_separator(self):
        new_button = tk.Button(self, text='-' * 100, state='disabled', borderwidth=0, **self.passiveConfig, anchor='w',
                               font="Helvetica 2", justify='left')
        new_button.grid(row=self.num_elements, column=0, sticky='we')
        self.num_elements += 1

    def post(self, padx, pady):
        if len(self.command_list) * 20 < 200:
            self.canvas.config(height=len(self.command_list) * 23)
        else:
            self.canvas.config(height=200)
        self.grid(row=1, column=0, sticky="nw", padx=padx, pady=pady, rowspan=2)
        self.canvas.xview_moveto(0)
        self.canvas.yview_moveto(0)
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

    def add_options(self):
        for btn in self.command_list:
            btn.grid_remove()
            btn.grid_forget()
        del self.command_list[:]
        self.num_elements = 0
        self.command_list = []
        if self.master.newActionFrame.optionsChoiceMenuValues == 'default':
            values = ['Left Click',
                      'Ctrl + Click',
                      'Shift + Click',
                      'Alt + Click',
                      'Ctrl + Alt + Click',
                      'Middle Click',
                      'Right Click',
                      'Ctrl + Right Click',
                      'Alt + Right Click',
                      'Ctrl + Alt + Right Click',
                      'Double Click',
                      'Double Right Click',
                      'Begin Dragging - Left Click Down',
                      'End Dragging - Left Click Up',
                      'Move Mouse',
                      'Move Mouse By Offset',
                      'Press Keyboard Key',
                      'Release Keyboard Key',
                      'Press Spacebar']
            for value in values:
                self.add_command(value)
        else:
            for value in self.master.newActionFrame.optionsChoiceMenuValues:
                self.add_command(value)
