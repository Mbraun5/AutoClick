import tkinter as tk
from config import Config


class OptionMenu(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)

        self.passiveConfig = {'bg': Config.dark_button_bg_color(),
                              'fg': Config.light_text_color(),
                              'activebackground': Config.dark_button_bg_color(),
                              'activeforeground': Config.light_text_color()
                              }
        self.activeConfig = {'bg': Config.light_button_bg_color(),
                             'fg': Config.light_button_fg_color(),
                             'activebackground': Config.light_button_bg_color(),
                             'activeforeground': Config.light_button_fg_color()
                             }

        self.config(bg=Config.dark_button_bg_color(), highlightbackground=Config.highlight_grey(), highlightthickness=1)

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
        '''
        Sets scroll region for canvas based on widget size
        :param event: tk.Event
        :return: None
        '''
        size = (self.btnFrame.winfo_reqwidth(), self.btnFrame.winfo_reqheight())
        self.canvas.config(scrollregion='0 0 %s %s' % size)
        self.btnFrame.bind('<Configure>', self.configure_interior_window)

    def configure_canvas(self, event):
        '''
        Configures button window to size of canvas
        :param event: tk.Event
        :return: None
        '''
        if self.btnFrame.winfo_reqwidth() != self.canvas.winfo_reqwidth():
            self.canvas.itemconfigure(self.btnFrameWindow, width=self.canvas.winfo_width())
        self.canvas.bind('<Configure>', self.configure_canvas)

    def mouse_event(self, event):
        '''
        Event handler for mouse wheel over buttons
        :param event: tk.Event
        :return: None
        '''
        if self.winfo_reqheight() < self.canvas.winfo_reqheight():
            return
        delta = -1 * int(event.delta / 120)
        self.canvas.yview("scroll", delta, "units")

    def add_command(self, label):
        '''
        Adds command to option menu
        :param label: string - button label
        :return: None
        '''
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
        '''
        Adds separator to menu for aesthetic purposes
        :return: None
        '''
        new_button = tk.Button(self, text='-' * 100, state='disabled', borderwidth=0, **self.passiveConfig, anchor='w',
                               font="Helvetica 2", justify='left')
        new_button.grid(row=self.num_elements, column=0, sticky='we')
        self.num_elements += 1

    def post(self, padx, pady):
        '''
        Posts option menu to main frame. Size of window depends on number of buttons in command list
        :param padx: int - x padding
        :param pady: int - y padding
        :return: None
        '''
        if len(self.command_list) * 20 < 200:
            self.canvas.config(height=len(self.command_list) * 23)
        else:
            self.canvas.config(height=200)
        self.grid(row=1, column=0, sticky="nw", padx=padx, pady=pady, rowspan=4)
        self.canvas.xview_moveto(0)
        self.canvas.yview_moveto(0)
        tk.Misc.lift(self, aboveThis=None)
        self.activeIndex = -1

    def unpost(self):
        '''
        Removes optionmenu from main window.
        :return: None
        '''
        if not self.activeIndex:
            return
        self.grid_remove()
        self.command_list[self.activeIndex].config(self.passiveConfig)
        self.activeIndex = None
        self.master.newActionFrame.optionButton.config(self.master.newActionFrame.passiveConfig)

    def hover_on(self, button):
        '''
        Event handler for hovering over buttons
        :param button: tk.Button
        :return: None
        '''
        button.config(**self.activeConfig)
        if self.activeIndex != -1:
            try:
                self.command_list[self.activeIndex].config(**self.passiveConfig)
            except TypeError:
                return
        self.activeIndex = self.command_list.index(button)

    def hover_off(self):
        '''
        Event handler for hovering off buttons
        :return: None
        '''
        if self.activeIndex != -1 and self.activeIndex is not None:
            self.command_list[self.activeIndex].config(**self.passiveConfig)
            self.activeIndex = -1

    def change_index(self, direction):
        '''
        Event handler for users pressing up and down arrow keys while menu has focus. Allows keyboard control
        :param direction: string - 'up' or 'down'
        :return: None
        '''
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
        '''
        Adds list of options to menu based on user selections from optionsChoiceMenuValues menu.
        :return: None
        '''
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
