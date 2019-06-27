import pyautogui as pag
import tkinter as tk
import time as t
import navbar as nav


class Main(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.configure(background='#465362')
        self.navbar = nav.NavBar(self, bg='blue')
        self.navbar.grid(row=0, column=0, sticky='ew')
        self.grid_columnconfigure(0, weight=1)

        self.bind('<Alt_L>f', self.navbar.keyevent)
        self.bind('<Alt_L>e', self.navbar.keyevent)
        self.bind('<Alt_L>v', self.navbar.keyevent)
        self.bind('<KeyRelease>', self.navbar.altevent)
        self.bind('<ButtonRelease-1>', self.navbar.buttonevent)


if __name__ == "__main__":
    root = Main()
    root.title('Automation')
    root.mainloop()

    '''

    #self.bind('g', lambda event: self.test(event))
    @staticmethod
    def test(event):
        print("here")
        pag.keyDown('alt')
        pag.keyDown('f', 0.1)
        pag.keyUp('f', 0.05)
        pag.keyUp('alt', 0.05)

    screenWidth, screenHeight = pyautogui.size()
    pyautogui.moveTo(screenWidth / 2, screenHeight / 2)
    #pyautogui.moveTo(1900, 1080)
    print(screenWidth, screenHeight)
    print(pyautogui.KEYBOARD_KEYS)
    pyautogui.hotkey('')
    #ha = pyautogui.alert(text='HEY', title='hmm', button='ok')
    #print(ha)
    #x, y = pyautogui.locateCenterOnScreen('test.png')
    #print(x, y)
    #pyautogui.moveTo(x, y)
    time.sleep(2)

    distance = 200
    while distance > 0:
        pyautogui.dragRel(distance, 0, duration=0.0001)   # move right
        distance -= 5
        pyautogui.dragRel(0, distance, duration=0.0001)   # move down
        pyautogui.dragRel(-distance, 0, duration=0.0001)  # move left
        distance -= 5
        pyautogui.dragRel(0, -distance, duration=0.0001)  # move up
    '''