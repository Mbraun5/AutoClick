import tkinter as tk
from tkinter import messagebox
import pyautogui as pag
import checkbox as c


class OptionsChoiceMenu(tk.Toplevel):
    def __init__(self, master, x, y):
        tk.Toplevel.__init__(self)
        self.master = master
        self.wm_title("Options")
        self.geometry('685x450+{}+{}'.format(x, y))
        self.resizable(False, False)
        self.overrideredirect(True)
        b = tk.Button(self, text="Ok", command=self.destroy)

        self.bind("<ButtonPress-1>", self.check_event)

        self.grab_set()
        self.pixel = tk.PhotoImage(height=1, width=1)

        self.commands = []
        self.descriptions = []
        self.checkboxes = []
        self.list_boxes = [tk.Listbox(self), tk.Listbox(self)]
        self.scrollbar = tk.Scrollbar(self, orient='vertical')
        self.check_box_frame = tk.Frame(self)
        self.check_box_frame.grid(row=0, column=0, sticky='n')

        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=10)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.list_boxes[0].grid(row=0, column=1, sticky='news')
        self.list_boxes[1].grid(row=0, column=2, sticky='news')

        self.set_commands()
        self.set_descriptions()
        self.set_checkboxes()

        self.button_frame = tk.Frame(self)
        self.button_frame.grid(row=1, column=0, columnspan=3, sticky='nsew')

        self.check_all_label = tk.Label(self.button_frame, text='Check/Uncheck All', font=('Helvetica', '11'))
        self.check_all_label.pack(anchor='center')
        self.check_all_button = tk.Button(self.button_frame, text="Check", command=lambda: self.check_all())
        self.check_all_button.pack(anchor='center')
        self.save_and_quit = tk.Label(self.button_frame, text='Save and Quit', font=('Helvetica', '11'))
        self.save_and_quit.pack(anchor='center')
        self.save_button = tk.Button(self.button_frame, text='Save', command=lambda: self.save_quit())
        self.save_button.pack(anchor='center')

    def check_event(self, event):
        self.focus_set()
        for item in self.list_boxes:
            item.select_clear(0, 'end')
        widget = event.widget
        try:
            if not isinstance(widget, OptionsChoiceMenu) and not isinstance(widget.master, OptionsChoiceMenu) and \
                    not isinstance(widget.master.master, OptionsChoiceMenu):
                self.bell()
        except AttributeError:
            self.bell()

    def set_commands(self):
        self.commands = ['Left Click',
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

        for command in self.commands:
            self.list_boxes[0].insert('end', command)

    def set_descriptions(self):
        self.descriptions = ['Press left click at x, y position.',
                             'Press Ctrl + Left click at x, y position.',
                             'Press Shift + Left Click at x, y position.',
                             'Press Alt + Left Click at x, y position.',
                             'Press Ctrl + Alt + Left Click at x, y position.',
                             'Press Middle Click at x, y position.',
                             'Press Right Click at x, y position.',
                             'Press Ctrl + Right Click at x, y position.',
                             'Press Alt + Right Click at x, y position.',
                             'Press Ctrl + Alt + Right Click at x, y position.',
                             'Double Left Click at x, y position.',
                             'Double Right Click at x, y position.',
                             'Press Left Click down at x, y position. Follow this with Move Mouse action to simulate dragging.',
                             'Release Left Click down at x, y, position.',
                             'Move Mouse to x, y location.',
                             'Mose Mouse by x, y relative offset.',
                             'Presses keyboard key down.',
                             'Releases keyboard key press.',
                             'Presses spacebar.']
        for description in self.descriptions:
            self.list_boxes[1].insert('end', description)

    def set_checkboxes(self):
        for i in range(len(self.descriptions)):
            new_check_box = c.CheckBox(self.check_box_frame, highlightthickness=0, text='', image=self.pixel, width=10,
                                       height=12, relief='sunken', borderwidth=1, compound='center')
            new_check_box.grid(row=i, column=0)
            self.checkboxes.append(new_check_box)

        if self.master.optionsChoiceMenuValues == 'default':
            self.check_all()
        else:
            index_list = []
            for elem in self.master.optionsChoiceMenuValues:
                index = self.commands.index(elem)
                index_list.append(index)
            for i in range(len(self.checkboxes)):
                if index_list.count(i) > 0:
                    self.checkboxes[i].switch()

    def check_all(self):
        all_flag = True
        for checkbox in self.checkboxes:
            if not checkbox.checked:
                all_flag = False
        if all_flag:
            for checkbox in self.checkboxes:
                checkbox.switch()
        else:
            for checkbox in self.checkboxes:
                if not checkbox.checked:
                    checkbox.switch()

    def save_quit(self):
        save_list = []
        for i in range(len(self.commands)):
            if self.checkboxes[i].checked:
                save_list.append(self.commands[i])
        if len(save_list) < 1:
            messagebox.showinfo("Error!", "Please select at least one checkbox parameter.")
            return
        self.master.optionsChoiceMenuValues = save_list
        self.master.optionMenu.add_options()
        self.master.reset_option_button()
        self.destroy()
