import tkinter as tk
import keyboard
import pyautogui as pag

# Switch from using keyboard to pynput keyboard.


class ShortcutFrame(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
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

        self.labels = [self.configLabel,
                       self.getPositionLabel,
                       self.startStopLabel]
        self.buttons = [self.getPositionAssign,
                        self.getPositionClear,
                        self.startStopAssign,
                        self.startStopClear]

        self.kb_map = None
        self.keybind_map()
        self.config()

    def handle_press(self, key):
        if key.name == self.assignMap[self.getPositionText]:
            self.master.newActionFrame.set_current_xy()
        elif key.name == self.assignMap[self.startStopText]:
            if self.master.script_frame.active:
                self.master.script_frame.stop_script()
            else:
                self.master.script_frame.start_script()
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
            self.textMap[widget].insert('end', key.name, 'justify')
            self.textMap[widget].config(state='disabled')
            widget.grid_remove()
            self.textMap[widget].grid()
            self.textMap[widget].focus()
        except Exception as e:
            print(e)

    def lose_focus(self, text):
        text.config(state='normal')
        text.delete(1.0, 'end')
        try:
            text.insert('end', '{}'.format(self.assignMap[text]), 'justify')
            if self.master.focus_displayof() != self.textMap[text]:
                self.textDict[text] = self.assignMap[text]
        except KeyError:
            text.insert('end', '{}'.format(self.assignMap[self.textMap[text]]), 'justify')
            if self.master.focus_displayof() != self.textMap[text]:
                self.textDict[self.textMap[text]] = self.assignMap[self.textMap[text]]
        text.config(state='disabled')

    def assign(self, text):
        self.assignMap[text] = self.textDict[text]
        self.focus()

    def clear(self, text):
        text.config(state='normal')
        text.delete(1.0, 'end')
        text.insert('end', 'None', 'justify')
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

    def config(self):
        self['bg'] = '#0E2B41'
        self.bodyFrame['bg'] = '#0E2B41'

        config = {'bg': '#0E2B41',
                  'fg': '#F4FFFD',
                  'font': ('Helvetica', '9')
                  }
        for label in self.labels:
            label.config(config)
        self.configLabel.config(font=('Helvetica', '11', 'bold'))

        config = {'bg': '#000F08',
                  'fg': '#F4FFFD',
                  'borderwidth': 1,
                  'activebackground': '#092327',
                  'activeforeground': '#86E7B8'
                  }
        for button in self.buttons:
            button.config(config)

    def text_config(self, widget):
        config = {'highlightthickness': 3,
                  'highlightcolor': '#058C42',
                  'highlightbackground': '#0E2B41',
                  'state': 'disabled'}
        widget.tag_config('justify', justify='center')
        widget.insert('end', 'None', 'justify')
        widget.config(**config)
        widget.bind("<FocusOut>", lambda _: self.lose_focus(widget))

    def keybind_map(self):
        self.kb_map = {'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e',
                       'f': 'f', 'g': 'g', 'h': 'h', 'i': 'i', 'j': 'j',
                       'k': 'k', 'l': 'l', 'm': 'm', 'n': 'n', 'o': 'o',
                       'p': 'p', 'q': 'q', 'r': 'r', 's': 's', 't': 't',
                       'u': 'u', 'v': 'v', 'w': 'w', 'x': 'x', 'y': 'y',
                       'z': 'z', 'caps lock': '<capslock>'}


    '''
    ['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',
    ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
    '8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
    'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',
    'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
    'browserback', 'browserfavorites', 'browserforward', 'browserhome',
    'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
    'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
    'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
    'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
    'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
    'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
    'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
    'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
    'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
    'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
    'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
    'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
    'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
    'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
    'command', 'option', 'optionleft', 'optionright']
    '''