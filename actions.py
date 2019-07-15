import pyautogui as pag
import random
import time
from functools import wraps


def sleep_curs_back(func):
    @wraps(func)
    def wrapper_inner(*args, **kwargs):
        args[0].sleep(args[4])
        if args[3]:
            pos = pag.position()
            func(*args, **kwargs)
            pag.moveTo(pos[0], pos[1])
        else:
            func(*args, **kwargs)
    return wrapper_inner


class Actions:
    def __init__(self, script):
        self.rand = random.SystemRandom()
        self.script = script
        self.func_map = {'Left Click': self.left_click,
                         'Ctrl + Click': self.ctrl_click,
                         'Shift + Click': self.shift_click,
                         'Alt + Click': self.alt_click,
                         'Ctrl + Alt + Click': self.ctrl_alt_click,
                         'Middle Click': self.middle_click,
                         'Right Click': self.right_click,
                         'Ctrl + Right Click': self.ctrl_right,
                         'Alt + Right Click': self.alt_right,
                         'Ctrl + Alt + Right Click': self.ctrl_alt_right,
                         'Double Click': self.double_click,
                         'Double Right Click': self.double_right,
                         'Begin Dragging - Left Click Down': self.left_drag_down,
                         'End Dragging - Left Click Up': self.left_drag_up,
                         'Move Mouse': self.move_mouse,
                         'Move Mouse By Offset': self.move_mouse_offset,
                         }

        # 'Move Mouse By Offset': lambda *_: self.move_mouse_offset(*_, 'hey'), use lambda to pass additional arguments

        self.exit_flag = False

    def start(self):
        for elem in self.script:
            if self.exit_flag:
                return
            self.func_map[elem.name](elem.x, elem.y, elem.curs_back, elem.delay, elem.repeat)

    def set_exit_flag(self):
        self.exit_flag = True

    def sleep(self, delay):
        delay = delay.split('+')
        value = self.rand.randint(1, int(delay[1]))
        delay = int(delay[0]) + value
        time.sleep(delay / 1000)

    @sleep_curs_back
    def left_click(self, x, y, curs_back, delay, repeat):
        for i in range(repeat):
            if self.exit_flag:
                return
            pag.click(x, y)

    @sleep_curs_back
    def ctrl_click(self, x, y, curs_back, delay, repeat):
        for i in range(repeat):
            if self.exit_flag:
                return
            pag.keyDown('ctrl')
            pag.click(x, y)
            pag.keyUp('ctrl')

    @sleep_curs_back
    def shift_click(self, x, y, curs_back, delay, repeat):
        for i in range(repeat):
            if self.exit_flag:
                return
            pag.keyDown('shift')
            pag.click(x, y)
            pag.keyUp('shift')

    @sleep_curs_back
    def alt_click(self, x, y, curs_back, delay, repeat):
        for i in range(repeat):
            if self.exit_flag:
                return
            pag.keyDown('alt')
            pag.click(x, y)
            pag.keyUp('alt')

    @sleep_curs_back
    def ctrl_alt_click(self, x, y, curs_back, delay, repeat):
        for i in range(repeat):
            if self.exit_flag:
                return
            pag.keyDown('ctrl')
            pag.keyDown('alt')
            pag.click(x, y)
            pag.keyUp('alt')
            pag.keyUp('ctrl')

    @sleep_curs_back
    def middle_click(self, x, y, curs_back, delay, repeat):
        for i in range(repeat):
            if self.exit_flag:
                return
            pag.click(x, y, button='middle')

    @sleep_curs_back
    def right_click(self, x, y, curs_back, delay, repeat):
        for i in range(repeat):
            if self.exit_flag:
                return
            pag.click(x, y, button='right')

    @sleep_curs_back
    def ctrl_right(self, x, y, curs_back, delay, repeat):
        for i in range(repeat):
            if self.exit_flag:
                return
            pag.keyDown('ctrl')
            pag.click(x, y, button='right')
            pag.keyUp('ctrl')

    @sleep_curs_back
    def alt_right(self, x, y, curs_back, delay, repeat):
        for i in range(repeat):
            if self.exit_flag:
                return
            pag.keyDown('alt')
            pag.click(x, y, button='right')
            pag.keyUp('alt')

    @sleep_curs_back
    def ctrl_alt_right(self, x, y, curs_back, delay, repeat):
        for i in range(repeat):
            if self.exit_flag:
                return
            pag.keyDown('ctrl')
            pag.keyDown('alt')
            pag.click(x, y, button='right')
            pag.keyUp('alt')
            pag.keyUp('ctrl')

    @sleep_curs_back
    def double_click(self, x, y, curs_back, delay, repeat):
        for i in range(repeat):
            if self.exit_flag:
                return
            pag.doubleClick(x, y)

    @sleep_curs_back
    def double_right(self, x, y, curs_back, delay, repeat):
        for i in range(repeat):
            if self.exit_flag:
                return
            pag.doubleClick(x, y, button='right')

    @sleep_curs_back
    def left_drag_down(self, x, y, curs_back, delay, repeat):
        for i in range(repeat):
            if self.exit_flag:
                return
            pag.mouseDown(x, y)

    @sleep_curs_back
    def left_drag_up(self, x, y, curs_back, delay, repeat):
        for i in range(repeat):
            if self.exit_flag:
                return
            pag.mouseUp(x, y)

    @sleep_curs_back
    def move_mouse(self, x, y, curs_back, delay, repeat):
        for i in range(repeat):
            if self.exit_flag:
                return
            pag.moveTo(x, y)

    @sleep_curs_back
    def move_mouse_offset(self, x, y, curs_back, delay, repeat):
        for i in range(repeat):
            if self.exit_flag:
                return
            pag.moveRel(x, y)
