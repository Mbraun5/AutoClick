import tkinter as tk
import keyboard


class ShortcutFrame(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self)
        self.master = master

        self.configLabel = tk.Label(self, text="Configure Global Keyboard Shortcuts")
        self.configLabel.grid(row=0, column=0)

        self.getPositionLabel = tk.Label(self, text="Get Mouse Cursor Position:")
        self.getPositionLabel.grid(row=1, column=0)
        self.startStopLabel = tk.Label(self, text="Start / Stop Script Execution:")
        self.startStopLabel.grid(row=2, column=0)

        self.getPositionText = tk.Text(self, state="disabled", width=15, height=1)
        self.getPositionText.grid(row=1, column=1)
        self.startStopText = tk.Text(self, state="disabled", width=15, height=1)
        self.startStopText.grid(row=2, column=1)
        keyboard.on_press(self.handle_press)
        self.textDict = {self.getPositionText: 'None',
                         self.startStopText: 'None'}

        self.getPositionAssign = tk.Button(self, text="Assign", command=lambda: print("PositionAssign"))
        self.getPositionAssign.grid(row=1, column=2)
        self.startStopAssign = tk.Button(self, text="Assign", command=lambda: print("StartAssign"))
        self.startStopAssign.grid(row=2, column=2)
        self.getPositionClear = tk.Button(self, text="Clear", command=lambda: self.clear(self.getPositionText))
        self.getPositionClear.grid(row=1, column=3)
        self.startStopClear = tk.Button(self, text="Clear", command=lambda: self.clear(self.startStopText))
        self.startStopClear.grid(row=2, column=3)

    def handle_press(self, key):
        widget = self.master.focus_displayof()
        if widget == self.getPositionText:
            if self.textDict[self.startStopText] == key.name:
                return
            widget.config(state='normal')
            widget.delete(1.0, 'end')
            widget.insert('end', key.name)
            widget.config(state='disabled')
            self.textDict[self.getPositionText] = key.name
        elif widget == self.startStopText:
            if self.textDict[self.getPositionText] == key.name:
                return
            widget.config(state='normal')
            widget.delete(1.0, 'end')
            widget.insert('end', key.name)
            widget.config(state='disabled')
            self.textDict[self.startStopText] = key.name
        self.master.focus()

    def clear(self, text):
        text.config(state='normal')
        text.delete(1.0, 'end')
        text.config(state='disabled')
        self.textDict[text] = 'None'
