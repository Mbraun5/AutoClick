import pyautogui as pag
import tkinter as tk
from tkinter import messagebox
import optionmenu as om
import checkbox as cb
import optionschoicemenu as ocm
from config import Config


class NewActionFrame(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)

        self.configure(bg=Config.action_bg_color())
        self.titleFrame = tk.Frame(self, bg=Config.action_bg_color())
        self.addFrame = tk.Frame(self, bg=Config.action_bg_color())

        self.titleFrame.pack(side='top')
        self.addFrame.pack(side='left', fill='both', expand=True)
        self.addFrame.columnconfigure(5, weight=1)  # allows widgets from column 5+ to use sticky

        self.pixel = tk.PhotoImage(width=1, height=1)   # used for button widgets so they can use pixel padding
        vcmd = (self.register(self.callback))

        self.activeConfig = {'bg': Config.light_button_bg_color(),
                             'fg': Config.light_button_fg_color()
                             }
        self.passiveConfig = {'bg': Config.dark_button_bg_color(),
                              'fg': Config.light_text_color()
                              }

        config = Config.title_label()
        self.titleLabel = tk.Label(self.titleFrame, text="Add New Action", **config)
        self.titleLabel.pack()

        config = Config.std_label()
        self.xLabel = tk.Label(self.addFrame, text="X-Coordinate:", **config)
        self.yLabel = tk.Label(self.addFrame, text="Y-Coordinate:", **config)
        self.actionLabel = tk.Label(self.addFrame, text="Action Type:", **config)
        self.checkLabel = tk.Label(self.addFrame, text='Cursor back:', **config)
        self.delayLabel = tk.Label(self.addFrame, text='Delay before action:', **config)
        self.msLabel = tk.Label(self.addFrame, text='Milliseconds', **config)
        self.commentLabel = tk.Label(self.addFrame, text="Comment:", **config)
        self.randomLabel = tk.Label(self.addFrame, text="+ Random", **config)
        self.repeatLabel = tk.Label(self.addFrame, text="Repeat count:", **config)

        self.xLabel.grid(row=0, column=0, padx=5, pady=(2, 2), sticky='e')
        self.yLabel.grid(row=0, column=2, padx=5, pady=(2, 2), sticky='e')
        self.actionLabel.grid(row=1, column=0, padx=5, pady=(2, 2), sticky='e')
        self.checkLabel.grid(row=2, column=0, padx=5, pady=(2, 2), sticky='e')
        self.delayLabel.grid(row=2, column=2, padx=5, pady=(2, 2), sticky='w')
        self.msLabel.grid(row=2, column=4, padx=5, pady=(2, 2), sticky='w')
        self.commentLabel.grid(row=3, column=0, padx=5, pady=(2, 2), sticky='e')
        self.randomLabel.grid(row=2, column=5, padx="50 5", sticky='w')
        self.repeatLabel.grid(row=3, column=7, padx=5, pady=(0, 5), sticky='e')

        config = Config.entry_config()
        config['validatecommand'] = (vcmd, '%P')
        self.xEntry = tk.Entry(self.addFrame, **config)
        self.yEntry = tk.Entry(self.addFrame, **config)
        self.delayEntry = tk.Entry(self.addFrame, **config)
        self.randomEntry = tk.Entry(self.addFrame, **config)
        self.locationEntry = tk.Entry(self.addFrame, **config)
        self.repeatEntry = tk.Entry(self.addFrame, **config)
        self.commentEntry = tk.Entry(self.addFrame, font=Config.entry_font())

        self.xEntry.grid(row=0, column=1, padx=5, sticky='w')
        self.yEntry.grid(row=0, column=3, padx=5, sticky='e')
        self.delayEntry.grid(row=2, column=3, padx=5, sticky='w')
        self.repeatEntry.grid(row=3, column=8, padx=5, pady=(0, 5), sticky='w')
        self.randomEntry.grid(row=2, column=5, padx='0 20', sticky='w')
        self.locationEntry.grid(row=2, column=6, padx='0 20', pady='0 3', columnspan=2)
        self.commentEntry.grid(row=3, column=1, columnspan=5, padx=5, pady='0 5', sticky='we')

        self.xEntry.bind("<FocusOut>", lambda _: self.check_entry(self.xEntry, pag.size()[0]))
        self.yEntry.bind("<FocusOut>", lambda _: self.check_entry(self.yEntry, pag.size()[1]))
        self.delayEntry.bind("<FocusOut>", lambda _: self.check_entry(self.delayEntry, 999999))
        self.randomEntry.bind("<FocusOut>", lambda _: self.check_entry(self.randomEntry, 99999))
        self.locationEntry.bind("<FocusOut>", lambda _: self.check_entry(self.locationEntry,
                                                                         len(self.master.script_frame.actions)+1))
        self.repeatEntry.bind("<FocusOut>", lambda _: self.check_entry(self.repeatEntry, 999999))

        config = Config.xtra_small_button()
        config['image'] = self.pixel
        self.resetButton = tk.Button(self.addFrame, text='Reset', command=self.reset, **config)
        self.optionsChoiceButton = tk.Button(self.addFrame, text=' ... ', command=self.create_choice_menu, **config)

        config = Config.std_button()
        config['image'] = self.pixel
        self.addButtonOne = tk.Button(self.addFrame, text='Add to top', command=lambda: self.add_command('top'),
                                      **config)
        self.addButtonTwo = tk.Button(self.addFrame, text='Add to bottom', command=lambda: self.add_command('bottom'),
                                      **config)
        self.addButtonThree = tk.Button(self.addFrame, text='Add to location', **config,
                                        command=lambda: self.add_command(self.locationEntry.get()))

        config = Config.spc_button()
        config['image'] = self.pixel
        self.optionButton = tk.Button(self.addFrame, text="           -- select an action --          " + u"\u2b9f",
                                      width=219, height=13, command=self.post_option_menu, **config)
        self.clearButton = tk.Button(self.addFrame, text='C', height=13, command=self.clear, **config)

        self.resetButton.grid(row=0, column=4, padx=5, sticky='w')
        self.optionsChoiceButton.grid(row=1, column=4, padx=5, pady=(2, 2), sticky='w')
        self.optionButton.grid(row=1, column=1, columnspan=3, padx=5, pady=(2, 2), sticky='ew')
        self.clearButton.grid(row=3, column=6, padx=5, pady=(0, 5), sticky='w')
        self.addButtonOne.grid(row=0, column=7, padx=5, pady=(0, 5), sticky='e', columnspan=2)
        self.addButtonTwo.grid(row=1, column=7, padx=5, pady=(0, 5), sticky='e', columnspan=2)
        self.addButtonThree.grid(row=2, column=7, padx=5, pady=(0, 5), sticky='e', columnspan=2)

        self.checkBox = cb.CheckBox(self.addFrame, highlightthickness=0, text='', image=self.pixel, width=15, height=15,
                                    relief='sunken', borderwidth=1, compound='center',
                                    activebackground=Config.action_bg_color())
        self.checkBox.grid(row=2, column=1, padx=5, pady=(2, 2), sticky='w')

        self.optionMenu = om.OptionMenu(self.master)

        self.optionMenuActive = False
        self.ignoreEvent = False
        self.optionsChoiceMenuValues = 'default'

        self.entries = [self.xEntry,
                        self.yEntry,
                        self.delayEntry,
                        self.commentEntry,
                        self.repeatEntry,
                        self.locationEntry,
                        self.randomEntry]

    def add_command(self, location, execute=False):
        """
        Adds command to script frame based on local parameters.
        :param location: 'top', 'bottom', or int value - sets where to add commands to script frame
        :param execute: bool - flag variable to force tkinter to update entries before adding command
        :return: None
        """
        if not execute:         # Allows for entries to be checked prior to command being added.
            if location != 'top' and location != 'bottom':
                self.after(75, lambda: self.add_command(self.locationEntry.get(), True))
            else:
                self.after(75, lambda: self.add_command(location, True))
            return
        text = self.optionButton['text'] if self.optionButton['text'] != "           -- select an action --          "\
                                                                         + u"\u2b9f" else None
        args = [text, self.xEntry.get(), self.yEntry.get(), self.checkBox.checked,
                "{}+{}".format(self.delayEntry.get(), self.randomEntry.get()), self.repeatEntry.get(),
                self.commentEntry.get()]
        for i in range(len(args)-1):
            if args[i] is None or args[i] == '':
                messagebox.showinfo("Entry Error!",
                                    "Fill out all entry fields and select an action.\nThe comment entry and "
                                    + "cursor back checkbox are optional.\n\nIf you would like to have the action "
                                    + "performed once, set the repeat count entry to 1.")
                return
        if self.delayEntry.get() == '' or self.randomEntry.get() == '':
            messagebox.showinfo("Delay Error!",
                                "Please enter the delay amount you would like before the action is performed."
                                + "\n\nTo prevent detection by anticheat algorithms, add a value to the "
                                + "random field and a random delay value between 1 and that number will be "
                                + "chosen to add to the delay before it is performed.")
            return
        if location == '':
            messagebox.showinfo("Location Error!",
                                "To use the add to location, input in the entry box to the left of the add "
                                + "to location button the location that you would like the action to be "
                                + "placed.\n\nThe action currently at that spot will be pushed back one "
                                + "place, as will the rest of the proceeding actions.")
            return
        self.master.script_frame.add_script(location, *args)

    @staticmethod
    def callback(p):
        """
        Checks entry values as they are input
        :param p: string - one character at a time is input
        :return: None
        """
        if p == '' or str.isdigit(p):
            return True
        return False

    @staticmethod
    def check_entry(entry, value):
        """
        Checks entry values when entry loses focus
        :param entry: tk.Entry
        :param value: int - max entry value allowable
        :return: None
        """
        if entry.get() == '':
            return
        if int(entry.get()) <= 0:
            entry.delete(0, 'end')
            entry.insert(0, '1')
        elif int(entry.get()) > value:
            entry.delete(0, 'end')
            entry.insert(0, str(value))

    def button_event(self, event):
        """
        Event handler for left click releases
        :param event: tk.Event
        :return: None
        """
        widget = event.widget
        if self.optionMenuActive and widget != self.optionMenu and not self.ignoreEvent:
            self.optionMenu.unpost()
            self.optionMenuActive = False
        elif self.optionMenuActive and widget != self.optionMenu:
            self.ignoreEvent = False
        try:
            if widget.master == self.addFrame or widget.master == self.titleFrame:
                if not isinstance(widget, tk.Entry):
                    self.master.focus_set()
        except AttributeError:
            self.master.focus_set()
            return

    def key_event(self, event):
        """
        alt key event handler
        :param event: tk.Event
        :return: None
        """
        if event.keycode == 18:
            self.optionMenu.unpost()
            self.optionMenuActive = False

    def option_menu_command(self, label):
        """
        Sets option menu label
        :param label: string
        :return: None
        """
        self.optionButton.config(text=label)
        self.optionMenu.unpost()
        self.optionMenuActive = False
        
    def post_option_menu(self):
        """
        Button handler for option menu
        :return: None
        """
        if self.optionMenuActive:
            self.optionMenu.unpost()
            self.optionMenuActive = False
        else:
            self.optionButton.config(self.activeConfig)
            self.optionMenu.post(95, 74)
            self.optionMenuActive = True
            self.ignoreEvent = True

    def create_choice_menu(self):
        """
        Button handler for choice menu button. Creates the choice menu
        :return: None
        """
        x = self.master.winfo_x() + int(self.master.winfo_width() / 4)
        y = self.master.winfo_y() + int(self.master.winfo_height() / 4)
        options_choice_menu = ocm.OptionsChoiceMenu(self, x, y)

    def reset(self):
        """
        Button handler for reset button. Resets all entries (including checkbox) and sets the option button to default.
        :return: None
        """
        for entry in self.entries:
            entry.delete(0, 'end')
        self.optionButton.config(text="           -- select an action --          " + u"\u2b9f")
        if self.checkBox.checked:
            self.checkBox.switch()

    def reset_option_button(self):
        """
        Sets option button to default
        :return: None
        """
        self.optionButton.config(text="           -- select an action --          " + u"\u2b9f")

    def set_option_button(self, label):
        """
        Sets option button to label
        :param label: string
        :return: None
        """
        self.optionButton.config(text=label)

    def clear(self):
        """
        Button handler for clear button
        :return: None
        """
        self.commentEntry.delete(0, 'end')

    def set_current_xy(self):
        """
        Event handler for shortcut menu binding selected by user. Updates x, y labels with current x, y position
        :return: None
        """
        self.xEntry.delete(0, 'end')
        self.xEntry.insert('end', pag.position()[0])
        self.yEntry.delete(0, 'end')
        self.yEntry.insert('end', pag.position()[1])
