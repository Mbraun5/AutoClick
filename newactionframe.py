import pyautogui as pag
import tkinter as tk
from tkinter import messagebox
import optionmenu as om
import checkbox as cb
import optionschoicemenu as ocm


class NewActionFrame(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self)
        self.master = master

        self.titleFrame = tk.Frame(self)
        self.titleFrame.pack(side='top')
        self.addFrame = tk.Frame(self)
        self.addFrame.pack(side='left', fill='both', expand=True)
        self.addFrame.columnconfigure(4, weight=1)

        self.pixel = tk.PhotoImage(width=1, height=1)

        self.titleLabel = tk.Label(self.titleFrame, text="Add New Action")
        self.titleLabel.pack()

        vcmd = (self.register(self.callback))
        self.xLabel = tk.Label(self.addFrame, text="X-Coordinate:")
        self.xLabel.grid(row=0, column=0, padx=5.5, sticky='e')

        self.xEntry = tk.Entry(self.addFrame, width=6, font=('Helvetica', '9', 'bold'), validate='all',
                               justify='center', validatecommand=(vcmd, '%P'))
        self.xEntry.grid(row=0, column=1, padx=5, sticky='ew')
        self.xEntry.bind("<FocusOut>", lambda _: self.check_entry(self.xEntry, pag.size()[0]))

        self.yLabel = tk.Label(self.addFrame, text="Y-Coordinate:")
        self.yLabel.grid(row=0, column=2, padx=5, sticky='e')

        self.yEntry = tk.Entry(self.addFrame, width=6, font=('Helvetica', '9', 'bold'), validate='all',
                               justify='center', validatecommand=(vcmd, '%P'))
        self.yEntry.grid(row=0, column=3, padx=5.5, sticky='e')
        self.yEntry.bind("<FocusOut>", lambda _: self.check_entry(self.yEntry, pag.size()[1]))

        self.resetButton = tk.Button(self.addFrame, text='Reset', font=('Helvetica', '7'), image=self.pixel,
                                     borderwidth=1, relief='flat', width=65, height=13, compound='center',
                                     command=self.reset)
        self.resetButton.grid(row=0, column=4, padx=5, sticky='w')

        self.actionLabel = tk.Label(self.addFrame, text="Action Type:")
        self.actionLabel.grid(row=1, column=0, padx=5, pady=(2, 2), sticky='e')

        self.activeConfig = {'bg': '#092327',
                             'fg': '#86E7B8'
                             }
        self.passiveConfig = {'bg': '#000F08',
                              'fg': '#F4FFFD'
                              }

        self.optionsChoiceButton = tk.Button(self.addFrame, text=' ... ', font=('Helvetica', '7'), image=self.pixel,
                                             borderwidth=1, relief='flat', width=65, height=13, compound='center',
                                             command=self.create_choice_menu)
        self.optionsChoiceButton.grid(row=1, column=4, padx=5, pady=(2, 2), sticky='w')
        self.optionsChoiceMenuValues = 'default'

        self.optionButton = tk.Button(self.addFrame, text="           -- select an action --          " + u"\u2b9f",
                                      font=('Helvetica', '9'), image=self.pixel, width=219, height=13,
                                      compound='center', command=self.post_option_menu, borderwidth=1, relief='flat')
        self.optionButton.grid(row=1, column=1, columnspan=3, padx=5, pady=(2, 2), sticky='ew')

        self.optionMenuActive = False
        self.ignoreEvent = False
        self.optionMenu = om.OptionMenu(self.master, '#000F08', '#F4FFFD', '#092327', '#86E7B8')

        self.checkLabel = tk.Label(self.addFrame, text='Cursor back:')
        self.checkLabel.grid(row=2, column=0, padx=5, pady=(2, 2), sticky='e')

        self.checkBox = cb.CheckBox(self.addFrame, highlightthickness=0, text='', image=self.pixel, width=15, height=15,
                                    relief='sunken', borderwidth=1, compound='center')
        self.checkBox.grid(row=2, column=1, padx=5, pady=(2, 2), sticky='w')

        self.delayLabel = tk.Label(self.addFrame, text='Delay before action:')
        self.delayLabel.grid(row=2, column=2, padx=5, pady=(0, 2), sticky='w')

        self.delayEntry = tk.Entry(self.addFrame, width=6, font=('Helvetica', '9', 'bold'), validate='all',
                                   justify='center', validatecommand=(vcmd, '%P'))
        self.delayEntry.grid(row=2, column=3, padx=5, sticky='ew')
        self.delayEntry.bind("<FocusOut>", lambda _: self.check_entry(self.delayEntry, 999999))

        self.msLabel = tk.Label(self.addFrame, text='Milliseconds')
        self.msLabel.grid(row=2, column=4, padx=5, pady=(0, 2), sticky='w')

        self.commentLabel = tk.Label(self.addFrame, text="Comment:")
        self.commentLabel.grid(row=3, column=0, padx=5, sticky='e')

        self.commentEntry = tk.Entry(self.addFrame, font=('Helvetica', '9', 'bold'))
        self.commentEntry.grid(row=3, column=1, columnspan=5, padx=5, pady=(0, 5), sticky='we')

        self.clearButton = tk.Button(self.addFrame, text='C', image=self.pixel, height=13, compound='center',
                                     font=('Helvetica', '9'), relief='flat', borderwidth=1, command=self.clear)
        self.clearButton.grid(row=3, column=6, padx=5, pady=(0, 5), sticky='w')

        self.addButtonOne = tk.Button(self.addFrame, text='Add to top', image=self.pixel, compound='center',
                                      font=('Helvetica', '9'), width=85, command=lambda: self.add_command('top'))
        self.addButtonOne.grid(row=0, column=7, padx=5, pady=(0, 5), sticky='e', columnspan=2)

        self.addButtonTwo = tk.Button(self.addFrame, text='Add to bottom', image=self.pixel, compound='center',
                                      font=('Helvetica', '9'), width=85, command=lambda: self.add_command('bottom'))
        self.addButtonTwo.grid(row=1, column=7, padx=5, pady=(0, 5), sticky='e', columnspan=2)

        self.addButtonThree = tk.Button(self.addFrame, text='Add to location', image=self.pixel, compound='center',
                                        font=('Helvetica', '9'), width=85, command=lambda: self.add_command('location'))
        self.addButtonThree.grid(row=2, column=7, padx=5, pady=(0, 5), sticky='e', columnspan=2)

        self.repeatLabel = tk.Label(self.addFrame, text="Repeat count:")
        self.repeatLabel.grid(row=3, column=7, padx=5, sticky='e')
        self.repeatEntry = tk.Entry(self.addFrame, width=6, font=('Helvetica', '9', 'bold'), validate='all',
                                    justify='center', validatecommand=(vcmd, '%P'))
        self.repeatEntry.grid(row=3, column=8, padx=5, sticky='w')
        self.repeatEntry.bind("<FocusOut>", lambda _: self.check_entry(self.repeatEntry, 999999))

        self.labels = [self.titleLabel,
                       self.xLabel,
                       self.yLabel,
                       self.commentLabel,
                       self.actionLabel,
                       self.delayLabel,
                       self.checkLabel,
                       self.msLabel,
                       self.repeatLabel]
        self.buttons = [self.addButtonOne,
                        self.addButtonTwo,
                        self.addButtonThree,
                        self.clearButton,
                        self.resetButton,
                        self.optionsChoiceButton,
                        self.optionButton]
        self.entries = [self.xEntry,
                        self.yEntry,
                        self.delayEntry,
                        self.commentEntry,
                        self.repeatEntry]

        self.config()

    def add_command(self, location, execute=False):
        if not execute:         # Allows for entries to be checked prior to command being added.
            self.after(75, lambda: self.add_command(location, True))
            return
        text = self.optionButton['text'] if self.optionButton['text'] != "           -- select an action --          " \
                                            + u"\u2b9f" else None
        args = [text, self.xEntry.get(), self.yEntry.get(), self.checkBox.checked,
                self.delayEntry.get(), self.repeatEntry.get(), self.commentEntry.get()]
        for i in range(len(args)-1):
            if args[i] is None or args[i] == '':
                messagebox.showinfo("Error!", "Fill out all entry fields and select an action.\nThe comment entry and "
                                    + "cursor back checkbox are optional.\n\nIf you would like to have the action "
                                    + "performed once, set the repeat count entry to 1.")
                return

        self.master.script_frame.add_script(location, *args)

    @staticmethod
    def callback(p):
        if p == '' or str.isdigit(p):
            return True
        return False

    @staticmethod
    def check_entry(entry, value):
        if entry.get() == '':
            return
        if int(entry.get()) > value:
            entry.delete(0, 'end')
            entry.insert(0, str(value))

    def config(self):
        self['bg'] = '#0E2B41'
        self.addFrame['bg'] = '#0E2B41'
        self.titleFrame['bg'] = '#0E2B41'

        config = {'bg': '#0E2B41',
                  'fg': '#F4FFFD',
                  'font': ('Helvetica', '9')
                  }
        for label in self.labels:
            label.config(config)
        self.titleLabel.config(font=('Helvetica', '11', 'bold'))

        config = {'bg': '#000F08',
                  'fg': '#F4FFFD',
                  'borderwidth': 1,
                  'activebackground': '#092327',
                  'activeforeground': '#86E7B8'
                  }
        for button in self.buttons:
            button.config(config)

        self.checkBox['bg'] = '#F4FFFD'
        self.checkBox['activebackground'] = '#0E2B41'
        self.checkBox['highlightbackground'] = '#0E2B41'
        self.checkBox['highlightcolor'] = '#0E2B41'

    def button_event(self):
        x, y = pag.position()
        widget = self.winfo_containing(x, y)
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
        if event.keycode == 18:
            self.optionMenu.unpost()
            self.optionMenuActive = False
        self.optionMenu.mouse_event(event)

    def option_menu_command(self, label):
        self.optionButton.config(text=label)
        self.optionMenu.unpost()
        self.optionMenuActive = False
        
    def post_option_menu(self):
        if self.optionMenuActive:
            self.optionMenu.unpost()
            self.optionMenuActive = False
        else:
            self.optionButton.config(self.activeConfig)
            self.optionMenu.post(98, 74)
            self.optionMenuActive = True
            self.ignoreEvent = True

    def create_choice_menu(self):
        x = self.master.winfo_x() + int(self.master.winfo_width() / 4)
        y = self.master.winfo_y() + int(self.master.winfo_height() / 4)
        options_choice_menu = ocm.OptionsChoiceMenu(self, x, y)

    def reset(self):
        for entry in self.entries:
            entry.delete(0, 'end')
        self.optionButton.config(text="           -- select an action --          " + u"\u2b9f")
        if self.checkBox.checked:
            self.checkBox.switch()

    def reset_option_button(self):
        self.optionButton.config(text="           -- select an action --          " + u"\u2b9f")

    def set_option_button(self, label):
        self.optionButton.config(text=label)

    def clear(self):
        self.commentEntry.delete(0, 'end')

    def set_current_xy(self):
        self.xEntry.delete(0, 'end')
        self.xEntry.insert('end', pag.position()[0])
        self.yEntry.delete(0, 'end')
        self.yEntry.insert('end', pag.position()[1])
