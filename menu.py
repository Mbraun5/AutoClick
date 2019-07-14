import tkinter as tk
from config import Config


class Menu(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.activeConfig = Config.nav_active_config()
        self.passiveConfig = Config.nav_passive_config()

        self.command_list = []
        self.num_elements = 0
        self.activeIndex = None

    def add_command(self, label=None, command=None):
        '''
        Adds command to the menu.
        :param label: tk.Label - title of object
        :param command: function - function called when button is pressed
        :return: None
        '''
        new_button = tk.Button(self, text=label, command=command, borderwidth=0, justify='left', anchor='w', padx=5,
                               **self.passiveConfig)
        new_button.grid(row=self.num_elements, column=0, sticky='we')
        new_button.bind('<Enter>', lambda _: self.hover_on(new_button))
        new_button.bind('<Leave>', lambda _: self.hover_off())
        self.num_elements += 1
        self.command_list.append(new_button)

    def add_separator(self):
        '''
        Adds separator for aesthetic look.
        :return: None
        '''
        new_button = tk.Button(self, text='-' * 100, state='disabled', borderwidth=0, anchor='w', font="Helvetica 2",
                               justify='left', **self.passiveConfig)
        new_button.grid(row=self.num_elements, column=0, sticky='we')
        self.num_elements += 1

    def post(self, padx, pady):
        '''
        Posts menu and raises it above every other frame to mimic an actual menu.
        :param padx: int - external padding to shift frame so many units to the right
        :param pady: int - external padding to shift frame so many units down
        :return: None
        '''
        self.grid(row=1, column=0, sticky="nw", padx=padx, pady=pady)
        self.tkraise()
        self.activeIndex = -1

    def unpost(self):
        '''
        Hides menu from root frame.
        :return: None
        '''
        self.grid_remove()
        self.activeIndex = None

    def hover_on(self, button):
        '''
        Called when child button is hovered on. Changes the hover button to active state.
        :param button: tk.Button - button being hovered on
        :return: None
        '''
        button.config(**self.activeConfig)
        if self.activeIndex != -1:
            try:
                self.command_list[self.activeIndex].config(**self.passiveConfig)
            except TypeError:
                for btn in self.command_list:
                    btn.config(**self.passiveConfig)
        self.activeIndex = self.command_list.index(button)

    def hover_off(self):
        '''
        Called when child button is hovered off of. Sets preiously active button to passive state.
        :return: None
        '''
        if self.activeIndex != -1 and self.activeIndex is not None:
            self.command_list[self.activeIndex].config(**self.passiveConfig)
            self.activeIndex = -1

    def change_index(self, direction):
        '''
        Provides functionality for users to navigate navbar using keyboard presses only.
        Up and down arrows change the menu button selection.
        This function is only called if there is an active button.
        :param direction: str - 'up' or 'down'
        :return: None
        '''
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
