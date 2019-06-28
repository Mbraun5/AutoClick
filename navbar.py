import tkinter as tk
import pyautogui as pag
import menu as m


class NavBar(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.master = master

        # SystemButtonText - Fg
        # SystemButtonFace - Bg
        # 323334 metallic black
        self.config(bg='#011936')
        self.passiveConfig = {'bg': '#011936',
                              'fg': '#F4FFFD',
                              'activebackground': '#011936',
                              'activeforeground': '#F4FFFD'
                              }
        self.activeConfig = {'activebackground': '#ED254E',
                             'activeforeground': '#F9DC5C',
                             'bg': '#ED254E',
                             'fg': '#F9DC5C'
                             }

        self.fileButton = tk.Button(self, text="File", underline=0, borderwidth=0, **self.passiveConfig)
        self.fileButton.pack(side='left')
        self.fileMenu = m.Menu(self.master, self.passiveConfig['bg'], self.passiveConfig['fg'], self.activeConfig['bg'],
                               self.activeConfig['fg'])
        self.fileMenu.add_command(label="New Script", command=lambda: self.placeholder(self.fileMenu, "New Script"))
        self.fileMenu.add_command(label="Save Script", command=lambda: self.placeholder(self.fileMenu, "Save Script"))
        self.fileMenu.add_command(label="Save As", command=lambda: self.placeholder(self.fileMenu, "Save As"))
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="Exit", command=self.master.quit)

        self.editButton = tk.Button(self, text="Edit", underline=0, borderwidth=0, **self.passiveConfig)
        self.editButton.pack(side='left')
        self.editMenu = m.Menu(self.master, self.passiveConfig['bg'], self.passiveConfig['fg'], self.activeConfig['bg'],
                               self.activeConfig['fg'])
        self.editMenu.add_command(label='Placeholder', command=lambda: self.placeholder(self.editMenu, "Placeholder"))

        self.viewButton = tk.Button(self, text="View", underline=0, borderwidth=0, **self.passiveConfig)
        self.viewButton.pack(side='left')
        self.viewMenu = m.Menu(self.master, self.passiveConfig['bg'], self.passiveConfig['fg'], self.activeConfig['bg'],
                               self.activeConfig['fg'])
        self.viewMenu.add_command(label="Placeholder", command=lambda: self.placeholder(self.viewMenu, "Placeholder"))

        self.activeButton = None
        self.activeMenu = None
        self.menuDict = {self.fileButton: self.fileMenu,
                         self.editButton: self.editMenu,
                         self.viewButton: self.viewMenu}
        self.menuPad = {self.fileMenu: 0,
                        self.editMenu: 23.5,
                        self.viewMenu: 51}
        self.buttonList = [self.fileButton, self.editButton, self.viewButton]
        self.buttonIndex = 0

        self.fileButton.bind("<Enter>", lambda _: self.check_focus(self.fileButton))
        self.editButton.bind("<Enter>", lambda _: self.check_focus(self.editButton))
        self.viewButton.bind("<Enter>", lambda _: self.check_focus(self.viewButton))
        self.ignoreAltEvent = False

    def post(self, button, menu):
        button.config(**self.activeConfig)
        menu.post(self.menuPad[menu])

    def altevent(self, event):
        if event.keycode == 18:
            if self.ignoreAltEvent is False:
                if self.activeButton is not None:
                    self.activeButton.config(**self.passiveConfig)
                    self.activeButton = None
                    self.activeMenu.unpost()
            else:
                self.ignoreAltEvent = False
        elif self.activeButton is None:
            return
        elif event.keycode == 37:
            self.change_menu("left")
        elif event.keycode == 38:
            self.activeMenu.change_index("up")
        elif event.keycode == 39:
            self.change_menu("right")
        elif event.keycode == 40:
            self.activeMenu.change_index("down")

    def keyevent(self, event):
        if self.activeButton is not None:
            self.activeButton.config(**self.passiveConfig)
            self.activeMenu.unpost()
        if event.char == 'f':
            self.activeButton = self.fileButton
            self.activeMenu = self.fileMenu
            self.post(self.fileButton, self.fileMenu)
            self.buttonIndex = 0
        elif event.char == 'e':
            self.activeButton = self.editButton
            self.activeMenu = self.editMenu
            self.post(self.editButton, self.editMenu)
            self.buttonIndex = 1
        elif event.char == 'v':
            self.activeButton = self.viewButton
            self.activeMenu = self.viewMenu
            self.post(self.viewButton, self.viewMenu)
            self.buttonIndex = 2
        self.ignoreAltEvent = True

    def button_event(self):
        x, y = pag.position()
        widget = self.winfo_containing(x, y)
        if isinstance(widget, tk.Button) and self.activeButton is None and isinstance(widget.master, NavBar):
            widget.configure(**self.activeConfig)
            self.activeButton = widget
            self.activeMenu = self.menuDict[widget]
            self.post(widget, self.menuDict[widget])
            self.buttonIndex = self.buttonList.index(widget)
        else:
            if self.activeButton is not None:
                self.activeButton.config(**self.passiveConfig)
                self.menuDict[self.activeButton].hover_off()
                self.menuDict[self.activeButton].unpost()
                self.activeButton = None

    def check_focus(self, button):
        if self.activeButton is not None:
            self.activeButton.config(**self.passiveConfig)
            self.activeMenu.unpost()
            self.buttonIndex = self.buttonList.index(button)
            self.post(button, self.menuDict[button])
            self.activeButton = button
            self.activeMenu = self.menuDict[button]

    def change_menu(self, direction):
        self.activeButton.config(**self.passiveConfig)
        self.activeMenu.unpost()
        if direction == "right":
            self.buttonIndex = (self.buttonIndex + 1) % len(self.buttonList)
        else:
            self.buttonIndex = (self.buttonIndex + len(self.buttonList) - 1) % len(self.buttonList)
        self.activeButton = self.buttonList[self.buttonIndex]
        self.activeMenu = self.menuDict[self.activeButton]
        self.post(self.activeButton, self.activeMenu)

    def placeholder(self, menu, button):
        x, y = pag.position()
        widget = self.winfo_containing(x, y)
        print("You clicked {}".format(button))
        # menu.hover_off()
        # menu.unpost()
