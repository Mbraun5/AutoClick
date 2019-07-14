import tkinter as tk
import pyautogui as pag
import menu as m
from config import Config


class NavBar(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)

        self.config(bg=Config.nav_bg_color())
        self.activeConfig = Config.nav_active_config()
        self.passiveConfig = Config.nav_passive_config()

        btn_config = {'underline': 0,
                      'borderwidth': 0
                      }
        self.fileButton = tk.Button(self, text="File", **btn_config, **self.passiveConfig)
        self.editButton = tk.Button(self, text="Edit", **btn_config, **self.passiveConfig)
        self.viewButton = tk.Button(self, text="View", **btn_config, **self.passiveConfig)
        self.fileButton.pack(side='left')
        self.editButton.pack(side='left')
        self.viewButton.pack(side='left')
        self.buttonList = [self.fileButton, self.editButton, self.viewButton]
        self.buttonIndex = 0

        self.fileMenu = m.Menu(self.master)
        self.fileMenu.add_command(label="New Script", command=lambda: self.placeholder(self.fileMenu, "New Script"))
        self.fileMenu.add_command(label="Save Script", command=lambda: self.placeholder(self.fileMenu, "Save Script"))
        self.fileMenu.add_command(label="Save As", command=lambda: self.placeholder(self.fileMenu, "Save As"))
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="Exit", command=self.master.quit)

        self.editMenu = m.Menu(self.master)
        self.editMenu.add_command(label='Placeholder', command=lambda: self.placeholder(self.editMenu, "Placeholder"))

        self.viewMenu = m.Menu(self.master)
        self.viewMenu.add_command(label="Placeholder", command=lambda: self.placeholder(self.viewMenu, 'Placeholder'))
        self.viewMenu.add_command(label='Documentation', command=lambda: self.placeholder(self.viewMenu,
                                                                                          'View Documentation'))

        self.activeButton = None
        self.activeMenu = None
        self.ignoreAltEvent = False

        self.menuDict = {self.fileButton: self.fileMenu,
                         self.editButton: self.editMenu,
                         self.viewButton: self.viewMenu}
        # x-padding amount to line menu options up with corresponding menu labels
        self.menuPad = {self.fileMenu: 0,
                        self.editMenu: 23.5,
                        self.viewMenu: 51}

        self.fileButton.bind("<Enter>", lambda _: self.check_focus(self.fileButton))
        self.editButton.bind("<Enter>", lambda _: self.check_focus(self.editButton))
        self.viewButton.bind("<Enter>", lambda _: self.check_focus(self.viewButton))

    def post(self, button, menu):
        '''
        Posts menu frame below corresponding navbar button
        :param button: tk.Button
        :param menu: m.Menu - child class of tk.Frame
        :return: None
        '''
        button.config(**self.activeConfig)
        menu.post(self.menuPad[menu], 0)

    def key_release_event(self, event):
        '''
        Maps actions based on key down events instantiated by user.
        :param event: tkinter event object
        :return: None
        '''
        # alt keypress
        if event.keycode == 18:
            # checks flag to prevent keyboard navigation events from unposting menu
            if self.ignoreAltEvent is False:
                if self.activeButton is not None:
                    self.activeButton.config(**self.passiveConfig)
                    self.activeButton = None
                    self.activeMenu.unpost()
            else:
                self.ignoreAltEvent = False
        elif self.activeButton is None:
            return
        # Left, Up, Right, Down key presses accordingly
        elif event.keycode == 37:
            self.change_menu("left")
        elif event.keycode == 38:
            self.activeMenu.change_index("up")
        elif event.keycode == 39:
            self.change_menu("right")
        elif event.keycode == 40:
            self.activeMenu.change_index("down")

    def alt_key_event(self, event):
        '''
        Maps all alt + key event actions
        :param event: tkinter event object
        :return: None
        '''
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

    def button_event(self, event):
        '''
        Maps actions from button release events.
        :param event: tkinter event object
        :return: None
        '''
        widget = event.widget

        # If user clicked navbar button and there currently is not another active button...
        if isinstance(widget.master, NavBar) and isinstance(widget, tk.Button) and self.activeButton is None:
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
        '''
        Changes state of navbar button to active if it is scrolled over while there is another navbar button selected.
        The button that is scrolled off of is set to passive. This is for aesthetic purposes.
        :param button:
        :return:
        '''
        if self.activeButton is not None:
            self.activeButton.config(**self.passiveConfig)
            self.activeMenu.unpost()
            self.buttonIndex = self.buttonList.index(button)
            self.post(button, self.menuDict[button])
            self.activeButton = button
            self.activeMenu = self.menuDict[button]

    def change_menu(self, direction):
        '''
        Provides functionality for users to navigate navbar using keyboard presses only.
        Left and right arrows change the menu being viewed.
        This function is only called if there is an active button.
        :param direction: str
        :return: None
        '''
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
