import tkinter as tk
import keyboard


class ShortcutFrame(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self)
        self.master = master

        self.titleFrame = tk.Frame(self)
        self.titleFrame.pack()
        self.bodyFrame = tk.Frame(self)
        self.bodyFrame.pack()

        self.configLabel = tk.Label(self.titleFrame, text="Configure Global Keyboard Shortcuts")
        self.configLabel.pack()
        self.getPositionLabel = tk.Label(self.bodyFrame, text="Get Mouse Cursor Position:")
        self.getPositionLabel.grid(row=1, column=0, padx=10, sticky='e')
        self.startStopLabel = tk.Label(self.bodyFrame, text="Start / Stop Script Execution:")
        self.startStopLabel.grid(row=2, column=0, padx=10, sticky='e')

        self.getPositionText = tk.Text(self.bodyFrame, state="disabled", width=15, height=1, borderwidth=2,
                                       relief='groove')
        self.getPositionText.grid(row=1, column=1, padx=10, pady=5)
        self.getPositionTextTwo = tk.Text(self.bodyFrame, state="disabled", width=15, height=1, borderwidth=2,
                                          relief='groove')
        self.getPositionTextTwo.grid(row=1, column=1, padx=10, pady=5)
        self.getPositionTextTwo.grid_remove()

        self.startStopText = tk.Text(self.bodyFrame, state="disabled", width=15, height=1, borderwidth=2,
                                     relief='groove')
        self.startStopText.grid(row=2, column=1, padx=10, pady=5)
        self.startStopTextTwo = tk.Text(self.bodyFrame, state="disabled", width=15, height=1, borderwidth=2,
                                        relief='groove')
        self.startStopTextTwo.grid(row=2, column=1, padx=10, pady=5)
        self.startStopTextTwo.grid_remove()

        self.getPositionText.tag_config("justify", justify='center')
        self.getPositionTextTwo.tag_config("justify", justify='center')
        self.startStopText.tag_config("justify", justify='center')
        self.startStopTextTwo.tag_config("justify", justify='center')
        keyboard.on_press(self.handle_press)
        self.textDict = {self.getPositionText: 'None',
                         self.startStopText: 'None'}
        self.textMap = {self.getPositionText: self.getPositionTextTwo,
                        self.getPositionTextTwo: self.getPositionText,
                        self.startStopText: self.startStopTextTwo,
                        self.startStopTextTwo: self.startStopText}

        self.getPositionAssign = tk.Button(self.bodyFrame, text="Assign", width=10, borderwidth=1,
                                           command=lambda: print("PositionAssign"))
        self.getPositionAssign.grid(row=1, column=2, padx=10)
        self.startStopAssign = tk.Button(self.bodyFrame, text="Assign", width=10, borderwidth=1,
                                         command=lambda: print("StartStopAssign"))
        self.startStopAssign.grid(row=2, column=2, padx=10)
        self.getPositionClear = tk.Button(self.bodyFrame, text="Clear", width=10, borderwidth=1,
                                          command=lambda: self.clear(self.getPositionText))
        self.getPositionClear.grid(row=1, column=3, padx=10)
        self.startStopClear = tk.Button(self.bodyFrame, text="Clear", width=10, borderwidth=1,
                                        command=lambda: self.clear(self.startStopText))
        self.startStopClear.grid(row=2, column=3, padx=10)

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
        except Exception as e:
            print(e)

    def clear(self, text):
        text.config(state='normal')
        text.delete(1.0, 'end')
        text.insert('end', 'None', "justify")
        text.config(state='disabled')
        text.grid()
        self.textMap[text].grid_remove()
        self.textDict[text] = 'None'
        self.master.focus()
