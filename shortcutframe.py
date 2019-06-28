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
        self.startStopText = tk.Text(self.bodyFrame, state="disabled", width=15, height=1, borderwidth=2,
                                     relief='groove')
        self.startStopText.grid(row=2, column=1, padx=10, pady=5)
        self.getPositionText.tag_config("justify", justify='center')
        self.startStopText.tag_config("justify", justify='center')
        keyboard.on_press(self.handle_press)
        self.textDict = {self.getPositionText: 'None',
                         self.startStopText: 'None'}

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
        if widget == self.getPositionText:
            if self.textDict[self.startStopText] == key.name:
                return
            widget.config(state='normal')
            widget.delete(1.0, 'end')
            widget.insert('end', key.name, "justify")
            widget.config(state='disabled')
            self.textDict[self.getPositionText] = key.name
        elif widget == self.startStopText:
            if self.textDict[self.getPositionText] == key.name:
                return
            widget.config(state='normal')
            widget.delete(1.0, 'end')
            widget.insert('end', key.name, "justify")
            widget.config(state='disabled')
            self.textDict[self.startStopText] = key.name
        self.master.focus()

    def clear(self, text):
        text.config(state='normal')
        text.delete(1.0, 'end')
        text.config(state='disabled')
        self.textDict[text] = 'None'
