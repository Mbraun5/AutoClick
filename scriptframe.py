import tkinter as tk
import scriptButtonFrame as sbf
from tkinter import messagebox
import threading as t
import actions as a


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
        # self.indexFrame.pack(side='left', anchor='w', fill='y', expand=False)

        self.commandsFrame.rowconfigure(0, weight=1)
        self.commandsFrame.columnconfigure(1, weight=1)
        self.indexFrame.grid(row=0, column=0, sticky='ns')

        self.valueFrame = tk.Frame(self.commandsFrame)
        self.valueFrame.columnconfigure(0, weight=1)
        # self.valueFrame.pack(side='right', anchor='w', fill='both', expand=True)

        self.valueFrame.grid(row=0, column=1, sticky='nsew')

        self.commandsFrame.bind('<Configure>', self.configure_interior_window)
        self.canvas.bind('<Configure>', self.configure_canvas)
        self.bind('<MouseWheel>', self.mouse_event)

        self.cvrFrame = tk.Frame(self.master, width=103, bg='#465362')
        self.cvrFrame.grid(row=2, column=0, sticky='nse')

        self.btnFrame = tk.Frame(self.master, bg='#465362')
        self.btnFrame.grid(row=2, column=0, sticky='e')

        self.btnPaddingy = "0 10"
        self.btnPaddingx = "5 5"
        self.startButton = tk.Button(self.btnFrame, text='Start', font=('Helvetica', '9'), image=self.pixel, width=85,
                                     compound='center', command=self.start_script)
        self.startButton.pack(anchor='center', expand=True, fill='x', pady="10 10", padx=self.btnPaddingx)
        self.upButton = tk.Button(self.btnFrame, text='Move Up', font=('Helvetica', '9'))
        self.upButton.pack(anchor='center', expand=True, fill='x', pady=self.btnPaddingy, padx=self.btnPaddingx)
        self.downButton = tk.Button(self.btnFrame, text='Move Down', font=('Helvetica', '9'))
        self.downButton.pack(anchor='center', expand=True, fill='x', pady=self.btnPaddingy, padx=self.btnPaddingx)
        self.deleteButton = tk.Button(self.btnFrame, text='Delete', font=('Helvetica', '9'))
        self.deleteButton.pack(anchor='center', expand=True, fill='x', pady=self.btnPaddingy, padx=self.btnPaddingx)
        self.deleteAllButton = tk.Button(self.btnFrame, text='Delete All', font=('Helvetica', '9'),
                                         command=self.delete_all)
        self.deleteAllButton.pack(anchor='center', expand=True, fill='x', pady=self.btnPaddingy, padx=self.btnPaddingx)

        self.config()
        self.actions = []
        self.indexes = []

        self.active_rows = []

        self.active_config = {'bg': '#000F08',
                              'fg': '#F4FFFD',
                              'borderwidth': 0,
                              'activebackground': '#000F08',
                              'activeforeground': '#F4FFFD'
                              }
        self.passive_config = {'bg': '#F4FFFD',
                               'fg': '#000F08',
                               'borderwidth': 0,
                               'activebackground': '#F4FFFD',
                               'activeforeground': '#000F08'
                               }
        self.shiftFlag = False
        self.row_copy = None
        self.script_thread = None
        self.events = None
        self.active = False

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
        num_btn = tk.Button(self.indexFrame, width=self.dimensions[0], text=len(self.actions) + 1, anchor='w', padx=6,
                            bg='#ffffff', borderwidth=0, relief='flat')
        num_btn.pack()
        self.indexes.append(num_btn)
        new_script = sbf.ScriptButtonFrame(self.valueFrame, self.dimensions, args)
        if location == 'bottom':
            new_script.grid(row=len(self.actions), sticky='nsew')
            self.actions.append(new_script)
        elif location == 'top':
            for elem in self.actions:
                elem.grid_remove()
                elem.grid_forget()
            self.actions.insert(0, new_script)
            for index, elem in enumerate(self.actions):
                elem.grid(row=index, sticky='nsew')
        else:
            loc = int(location) - 1
            for i in range(loc, len(self.actions)):
                self.actions[i].grid_remove()
                self.actions[i].grid_forget()
            self.actions.insert(loc, new_script)
            for i in range(loc, len(self.actions)):
                self.actions[i].grid(row=i, sticky='nsew')

    def deselect_all(self):
        if len(self.active_rows) > 0:
            for i in range(self.active_rows[0], self.active_rows[1] + 1):
                self.indexes[i].config(self.passive_config)
                self.actions[i].set_passive()
                self.active_rows = []

    def button_event(self, event):
        if not self.shiftFlag:
            if isinstance(event.widget, tk.Scrollbar):
                return
            prev_rows = self.active_rows
            self.deselect_all()

            try:
                if isinstance(event.widget.master.master.master.master.master, ScriptFrame):
                    event.widget.master.set_active()
                    index = self.actions.index(event.widget.master)
                    self.indexes[index].config(self.active_config)
                    self.active_rows = [index, index]
            except AttributeError:
                pass
            try:
                if isinstance(event.widget.master.master.master.master, ScriptFrame):
                    event.widget.config(self.active_config)
                    index = self.indexes.index(event.widget)
                    self.actions[index].set_active()
                    self.active_rows = [index, index]
            except AttributeError:
                pass
            if event.widget == self.upButton:
                self.move_up(prev_rows)
            elif event.widget == self.downButton:
                self.move_down(prev_rows)
            elif event.widget == self.deleteButton:
                self.delete(rows=prev_rows)

    def shift_click_event(self, event):
        self.shiftFlag = True
        try:
            if isinstance(event.widget.master.master.master.master.master, ScriptFrame):
                event.widget.master.set_active()
                index = self.actions.index(event.widget.master)
                self.indexes[index].config(self.active_config)

                if len(self.active_rows) == 0:
                    self.active_rows = [index, index]
                elif index > self.active_rows[1]:
                    for i in range(self.active_rows[1] + 1, index):
                        self.indexes[i].config(self.active_config)
                        self.actions[i].set_active()
                    self.active_rows[1] = index
                elif index < self.active_rows[0]:
                    for i in range(index + 1, self.active_rows[0]):
                        self.indexes[i].config(self.active_config)
                        self.actions[i].set_active()
                    self.active_rows[0] = index
        except AttributeError:
            pass
        try:
            if isinstance(event.widget.master.master.master.master, ScriptFrame):
                event.widget.config(self.active_config)
                index = self.indexes.index(event.widget)
                self.actions[index].set_active()

                if len(self.active_rows) == 0:
                    self.active_rows.append(index)
                elif index > self.active_rows[-1]:
                    for i in range(self.active_rows[-1] + 1, index):
                        self.indexes[i].config(self.active_config)
                        self.actions[i].set_active()
                    self.active_rows[1] = index
                else:
                    for i in range(index + 1, self.active_rows[-1]):
                        self.indexes[i].config(self.active_config)
                        self.actions[i].set_active()
                    self.active_rows[0] = index
        except AttributeError:
            pass
        self.after(40, self.remove_flag)

    def remove_flag(self):
        self.shiftFlag = False

    def copy_event(self, event=None, recopy=False):
        if not recopy:
            self.row_copy = []
            for i in range(self.active_rows[0], self.active_rows[1] + 1):
                self.row_copy.append(self.actions[i].copy())
        else:
            copy = []
            for elem in self.row_copy:
                copy.append(elem.copy())
            self.row_copy = copy

    def paste_event(self, event):
        if self.row_copy is None:
            messagebox.showinfo('Error!',
                                'Select a list of actions and copy them using Ctrl + c before you can paste actions.'
                                + '\nThere are currently no copied actions stored.')
            return
        if len(self.active_rows) <= 0:
            messagebox.showinfo('Error!',
                                'To paste your copied rows, first select an action from the list.\n The copied actions'
                                + 'will be appended after the last action or selected actions if more than one is'
                                + 'selected.')
            return
        for i in range(len(self.row_copy)):
            num_btn = tk.Button(self.indexFrame, width=self.dimensions[0], text=len(self.indexes) + 1, anchor='w',
                                padx=6,
                                bg='#ffffff', borderwidth=0, relief='flat')
            num_btn.pack()
            self.indexes.append(num_btn)

        for i in range(self.active_rows[1], len(self.actions)):
            self.actions[i].grid_remove()
            self.actions[i].grid_forget()
        self.actions = self.actions[:self.active_rows[1]+1] + self.row_copy + self.actions[self.active_rows[1]+1:]
        for i in range(self.active_rows[1], len(self.actions)):
            self.actions[i].grid(row=i, sticky='nsew')
        self.copy_event(recopy=True)

    def select_all_event(self, event):
        if len(self.actions) <= 0:
            return
        self.active_rows = [0, len(self.actions)-1]
        for i in range(self.active_rows[0], self.active_rows[1]+1):
            self.actions[i].set_active()
            self.indexes[i].config(self.active_config)

    def move_up(self, rows):
        if len(rows) <= 0:
            messagebox.showinfo('Error!',
                                'Select an action or group of actions and select the move up button to move the entire'
                                + ' group up before the first selected item.')
            return
        if rows[0] == 0:
            return
        self.actions[rows[0]-1].grid(row=rows[1], sticky='news')
        for i in range(rows[0], rows[1] + 1):
            self.actions[i].grid(row=i-1, sticky='news')
            self.actions[i-1], self.actions[i] = self.actions[i], self.actions[i-1]

    def move_down(self, rows):
        if len(rows) <= 0:
            messagebox.showinfo('Error!',
                                'Select an action or group of actions and select the move down button to move the '
                                + 'entire group down after the last selected item.')
            return
        if rows[1] == len(self.actions)-1:
            return
        self.actions[rows[1]+1].grid(row=rows[0], sticky='news')
        for i in range(rows[0], rows[1] + 1):
            self.actions[i].grid(row=i+1, sticky='news')
        self.actions.insert(rows[0], self.actions[rows[1]+1])
        del self.actions[rows[1]+2]

    def delete(self, event=None, rows=None):
        if rows is None:
            rows = self.active_rows
            self.deselect_all()
        if len(rows) <= 0:
            messagebox.showinfo('Error!',
                                'Select an action or group of actions and select the delete button to delete the entire'
                                + ' group.')
            return
        for i in range(rows[0], rows[1] + 1):
            self.actions[rows[0]].grid_remove()
            self.actions[rows[0]].grid_forget()
            del self.actions[rows[0]]
            self.indexes[-1].pack_forget()
            del self.indexes[-1]
        for i in range(rows[0], len(self.actions)):
            self.actions[i].grid(row=i, sticky='news')

    def delete_all(self):
        for index, elem in enumerate(self.actions):
            elem.grid_remove()
            elem.grid_forget()
            self.indexes[index].pack_forget()
        self.indexes = []
        self.actions = []

    def start_script(self):
        self.script_thread = t.Thread(target=self.start_script_t)
        self.script_thread.start()

    def start_script_t(self):
        self.active = True
        self.events = a.Actions(self.actions)
        self.events.start()
        self.active = False

    def stop_script(self):
        self.events.set_exit_flag()
        self.active = False


""" Double click handler
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
"""
