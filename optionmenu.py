import tkinter as tk


class OptionMenu(tk.Canvas):
    def __init__(self, *args, **kwargs):
        tk.Canvas.__init__(self, **kwargs)
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
        self.command_list = []
        self.num_elements = 0
        self.activeIndex = None
        self.config(height=190, width=226)
        self.pack_propagate(False)
        self.btnFrame = tk.Frame(self)
        self.create_window((0, 0), window=self.btnFrame, anchor='nw')
        self.scrllbar = tk.Scrollbar(self, orient='vertical')
        self.configure(yscrollcommand=self.scrllbar.set)
        self.bind('<Configure>', self.on_configure)
        self.pixel = tk.PhotoImage(height=1, width=1)

    def add_command(self, label=None, command=None):
        newButton = tk.Button(self.btnFrame, text=label, command=command, borderwidth=0, image=self.pixel,
                              **self.passiveConfig, justify='center', anchor='w', padx=5, width=219, height=19,
                              compound='center')
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
        self.yview("scroll", -120, "units")
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
        if len(self.command_list) < 9:
            return
        if self.master.newActionFrame.optionMenuActive:
            if event.keycode == 38:
                self.change_index("up")
                if self.scrllbar.get()[0] <= 0:
                    delta = 0
                else:
                    delta = -2
            elif event.keycode == 40:
                self.change_index("down")
                if self.scrllbar.get()[1] >= 1:
                    delta = 0
                else:
                    delta = 2
            else:
                if self.btnFrame.winfo_y() < ((8 - len(self.command_list)) * 21) and event.delta < 0:
                    return
                delta = -1 * int(event.delta / 120)
            self.yview("scroll", delta, "units")

    def on_configure(self, event):
        self.configure(scrollregion=self.bbox('all'))

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
                self.add_command(value, command=None)
        else:
            for value in self.master.newActionFrame.optionsChoiceMenuValues:
                self.add_command(value, command=None)
