import tkinter as tk
import keyboard
import pyautogui as pag


class ShortcutFrame(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self)
        self.master = master

        self.titleFrame = tk.Frame(self)
        self.titleFrame.pack()
        self.bodyFrame = tk.Frame(self)
        self.bodyFrame.pack()

        self.configLabel = tk.Label(self.titleFrame, text="Configure Global Keyboard Shortcuts",
                                    font=('Helvetica', '11', 'bold'))
        self.configLabel.pack()
        self.getPositionLabel = tk.Label(self.bodyFrame, text="Get Mouse Cursor Position:", font=('Helvetica', '9'))
        self.getPositionLabel.grid(row=1, column=0, padx=10, sticky='e')
        self.startStopLabel = tk.Label(self.bodyFrame, text="Start / Stop Script Execution:", font=('Helvetica', '9'))
        self.startStopLabel.grid(row=2, column=0, padx=10, sticky='e')

        self.textConfig = {'highlightthickness': 3,
                           'highlightcolor': '#058C42',
                           'highlightbackground': '#0E2B41',
                           'state': 'disabled'}
        self.getPositionText = tk.Text(self.bodyFrame, width=15, height=1, borderwidth=2, relief='groove')
        self.text_config(self.getPositionText)
        self.getPositionText.grid(row=1, column=1, padx=10, pady=5)

        self.getPositionTextTwo = tk.Text(self.bodyFrame, width=15, height=1, borderwidth=2, relief='groove')
        self.text_config(self.getPositionTextTwo)
        self.getPositionTextTwo.grid(row=1, column=1, padx=10, pady=5)
        self.getPositionTextTwo.grid_remove()

        self.startStopText = tk.Text(self.bodyFrame, width=15, height=1, borderwidth=2, relief='groove')
        self.text_config(self.startStopText)
        self.startStopText.grid(row=2, column=1, padx=10, pady=5)

        self.startStopTextTwo = tk.Text(self.bodyFrame, width=15, height=1, borderwidth=2, relief='groove')
        self.text_config(self.startStopTextTwo)
        self.startStopTextTwo.grid(row=2, column=1, padx=10, pady=5)
        self.startStopTextTwo.grid_remove()

        keyboard.on_press(self.handle_press)
        self.textDict = {self.getPositionText: 'None',
                         self.startStopText: 'None'}
        self.textMap = {self.getPositionText: self.getPositionTextTwo,
                        self.getPositionTextTwo: self.getPositionText,
                        self.startStopText: self.startStopTextTwo,
                        self.startStopTextTwo: self.startStopText}
        self.assignMap = {self.getPositionText: 'None',
                          self.startStopText: 'None'}

        self.getPositionAssign = tk.Button(self.bodyFrame, text="Assign", width=10, borderwidth=1,
                                           command=lambda: self.assign(self.getPositionText))
        self.getPositionAssign.grid(row=1, column=2, padx=10)
        self.startStopAssign = tk.Button(self.bodyFrame, text="Assign", width=10, borderwidth=1,
                                         command=lambda: self.assign(self.startStopText))
        self.startStopAssign.grid(row=2, column=2, padx=10)
        self.getPositionClear = tk.Button(self.bodyFrame, text="Clear", width=10, borderwidth=1,
                                          command=lambda: self.clear(self.getPositionText))
        self.getPositionClear.grid(row=1, column=3, padx=10)
        self.startStopClear = tk.Button(self.bodyFrame, text="Clear", width=10, borderwidth=1,
                                        command=lambda: self.clear(self.startStopText))
        self.startStopClear.grid(row=2, column=3, padx=10)

        self.conf()

    def handle_press(self, key):
        widget = self.master.focus_displayof()
        if widget == self.getPositionText or widget == self.getPositionTextTwo:
            if self.textDict[self.startStopText] == key.name:
                return
            self.textDict[self.getPositionText] = key.name
        elif widget == self.startStopText or widget == self.startStopTextTwo:
            if self.textDict[self.getPositionText] == key.name:
                return
            self.textDict[self.startStopText] = key.name
        else:
            return
        try:
            self.textMap[widget].config(state='normal')
            self.textMap[widget].delete(1.0, 'end')
            self.textMap[widget].insert('end', key.name, "justify")
            self.textMap[widget].config(state='disabled')
            widget.grid_remove()
            self.textMap[widget].grid()
            self.textMap[widget].focus()
        except Exception as e:
            print(e)

    def assign(self, text):
        self.assignMap[text] = self.textDict[text]
        self.master.focus()

    def clear(self, text):
        text.config(state='normal')
        text.delete(1.0, 'end')
        text.insert('end', 'None', "justify")
        text.config(state='disabled')
        text.grid()
        self.textMap[text].grid_remove()
        self.textDict[text] = 'None'
        self.assignMap[text] = 'None'
        self.master.focus()

    def button_event(self):
        x, y = pag.position()
        widget = self.winfo_containing(x, y)
        if isinstance(widget, tk.Text) and widget.master == self.bodyFrame:
            widget.focus()

    # 465362
    def conf(self):
        self['bg'] = '#0E2B41'
        self.bodyFrame['bg'] = '#0E2B41'

        # self['bg'] = '#465362'
        # self.bodyFrame['bg'] = '#465362'

        # self.configLabel['bg'] = '#465362'
        self.configLabel['bg'] = '#0E2B41'
        self.configLabel['fg'] = '#F4FFFD'

        # self.getPositionLabel['bg'] = '#465362'
        self.getPositionLabel['bg'] = '#0E2B41'
        self.getPositionLabel['fg'] = '#F4FFFD'
        # self.startStopLabel['bg'] = '#465362'
        self.startStopLabel['bg'] = '#0E2B41'
        self.startStopLabel['fg'] = '#F4FFFD'

        self.getPositionAssign['bg'] = '#000F08'
        self.getPositionAssign['fg'] = '#F4FFFD'
        self.startStopAssign['bg'] = '#000F08'
        self.startStopAssign['fg'] = '#F4FFFD'

        self.getPositionClear['bg'] = '#000F08'
        self.getPositionClear['fg'] = '#F4FFFD'
        self.startStopClear['bg'] = '#000F08'
        self.startStopClear['fg'] = '#F4FFFD'

    def text_config(self, widget):
        widget.tag_config("justify", justify='center')
        widget.insert('end', 'None', "justify")
        widget.config(**self.textConfig)
