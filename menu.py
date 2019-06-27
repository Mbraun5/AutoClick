import tkinter as tk


class Menu(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, **kwargs)
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

    def add_command(self, label=None, command=None):
        newButton = tk.Button(self, text=label, command=command, borderwidth=0, **self.passiveConfig, justify='left',
                              anchor='w', padx=5)
        newButton.bind('<Enter>', lambda _: self.hover_on(newButton))
        newButton.bind('<Leave>', lambda _: self.hover_off(newButton))
        newButton.grid(row=self.num_elements, column=0, sticky='we')
        self.num_elements += 1
        self.command_list.append(newButton)

    def add_separator(self):
        newButton = tk.Button(self, text='-' * 100, state='disabled', borderwidth=0, **self.passiveConfig, anchor='w',
                              font="Helvetica 2", justify='left')
        newButton.grid(row=self.num_elements, column=0, sticky='we')
        self.num_elements += 1

    def post(self, pad):
        self.grid(row=1, column=0, sticky="w", padx=pad)
        self.activeIndex = -1

    def unpost(self):
        self.grid_remove()
        self.activeIndex = None

    def hover_on(self, button):
        button.config(**self.activeConfig)
        if self.activeIndex != -1:
            self.command_list[self.activeIndex].config(**self.passiveConfig)
        self.activeIndex = self.command_list.index(button)

    def hover_off(self, button):
        button.config(**self.passiveConfig)
        self.activeIndex = -1

    def change_index(self, direction):
        if direction == "up":
            if self.activeIndex != -1:
                self.command_list[self.activeIndex].config(**self.passiveConfig)
            else:
                self.activeIndex = 0
            self.activeIndex = (self.activeIndex + len(self.command_list) - 1) % len(self.command_list)
            self.command_list[self.activeIndex].config(**self.activeConfig)
        else:
            if self.activeIndex != -1:
                self.command_list[self.activeIndex].config(**self.passiveConfig)
            self.activeIndex = (self.activeIndex + 1) % len(self.command_list)
            self.command_list[self.activeIndex].config(**self.activeConfig)
