import tkinter as tk


class ScriptFrame(tk.Frame):
    def __init__(self, master, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)

        self.scrollbar = tk.Scrollbar(self, orient='vertical')
        self.scrollbar.pack(fill='y', side='right', expand='false')

        self.titleFrame = tk.Frame(self, bg='#FFDDAA', height=20)
        self.titleFrame.pack(anchor='n', fill='x')

        self.titles = ['#', 'Action', 'X-Coor', 'Y-Coor', 'Cursor Back?', 'Delay (ms)', 'Repeat', 'Comment']
        self.labels = []
        for title in self.titles:
            new_label = tk.Label(self.titleFrame, text=title, width=10, font=('Helvetica', '9'))
            new_label.pack(side='left')
            self.labels.append(new_label)
        self.labels[0].config(width=5)
        self.labels[len(self.titles)-1].pack(side='left', fill='x', expand=True)

        self.textFrame = tk.Frame(self, bg='#abcabc', height=20)
        self.textFrame.pack(anchor='n', fill='x')

        self.newbutton = tk.Button(self, text='HAHAsdfsdfsdfsdfsdf', anchor='w')
        self.newbutton.config(width=5)
        self.newbutton.pack(anchor='nw')


''' Double click handler
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
'''