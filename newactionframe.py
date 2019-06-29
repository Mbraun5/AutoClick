import pyautogui as pag
import tkinter as tk


class NewActionFrame(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self)
        self.master = master

        self.titleFrame = tk.Frame(self)
        self.titleFrame.pack(side='top')
        self.addFrame = tk.Frame(self)
        self.addFrame.pack(side='left', fill='both')
        self.buttonFrame = tk.Frame(self)
        self.buttonFrame.pack(side='right', fill='both')

        self.titleLabel = tk.Label(self.titleFrame, text="Add New Action", font=('Helvetica', '11', 'bold'))
        self.titleLabel.pack()

        vcmd = (self.register(self.callback))
        self.xLabel = tk.Label(self.addFrame, text="X-Coordinate:", font=('Helvetica', '9'))
        self.xLabel.grid(row=0, column=0, padx=5)
        self.xEntry = tk.Entry(self.addFrame, width=6, font=('Helvetica', '9', 'bold'), validate='all',
                               validatecommand=(vcmd, '%P'))
        self.xEntry.grid(row=0, column=1, padx=5, sticky='w')
        self.xEntry.bind("<FocusOut>", lambda _:self.check_entry(self.xEntry, pag.size()[0]))

        self.yLabel = tk.Label(self.addFrame, text="Y-Coordinate:", font=('Helvetica', '9'))
        self.yLabel.grid(row=0, column=2, padx=5, sticky='w')
        self.yEntry = tk.Entry(self.addFrame, width=6, font=('Helvetica', '9', 'bold'), validate='all',
                               validatecommand=(vcmd, '%P'))
        self.yEntry.grid(row=0, column=3, padx=5, sticky='w')
        self.yEntry.bind("<FocusOut>", lambda _:self.check_entry(self.yEntry, pag.size()[1]))

        self.actionLabel = tk.Label(self.addFrame, text="Action Type:", font=('Helvetica', '9'))
        self.actionLabel.grid(row=1, column=0, padx=5, sticky='e')

        default_value = tk.StringVar(self)
        default_value.set('Left Click')
        choices = {'Left Click', 'this', 'is', 'a', 'test'}

        self.actionOptions = tk.OptionMenu(self.addFrame, default_value, *choices)
        self.actionOptions.grid(row=1, column=1, padx=5, sticky='w', columnspan=3)

        self.config()

    @staticmethod
    def callback(P):
        if str.isdigit(P) or P == '':
            return True
        return False

    def check_entry(self, entry, value):
        if int(entry.get()) > value:
            entry.delete(0, 'end')
            entry.insert(0, str(value))


    def config(self):
        self['bg'] = '#0E2B41'
        self.addFrame['bg'] = '#0E2B41'
        self.buttonFrame['bg'] = '#0E2B41'
        self.titleFrame['bg'] = '#0E2B41'

        self.titleLabel['bg'] = '#0E2B41'
        self.titleLabel['fg'] = '#F4FFFD'

        self.xLabel['bg'] = '#0E2B41'
        self.xLabel['fg'] = '#F4FFFD'
        self.yLabel['bg'] = '#0E2B41'
        self.yLabel['fg'] = '#F4FFFD'

        self.actionLabel['bg'] = '#0E2B41'
        self.actionLabel['fg'] = '#F4FFFD'




