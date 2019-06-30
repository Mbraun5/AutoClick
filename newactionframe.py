import pyautogui as pag
import tkinter as tk
import optionmenu as om
import checkbox as cb


class NewActionFrame(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self)
        self.master = master

        self.titleFrame = tk.Frame(self)
        self.titleFrame.pack(side='top')
        self.addFrame = tk.Frame(self)
        self.addFrame.pack(side='left', fill='both', expand=True)

        self.addFrame.columnconfigure(4, weight=1)

        self.pixel = tk.PhotoImage(width=1, height=1)

        self.titleLabel = tk.Label(self.titleFrame, text="Add New Action", font=('Helvetica', '11', 'bold'))
        self.titleLabel.pack()

        vcmd = (self.register(self.callback))
        self.xLabel = tk.Label(self.addFrame, text="X-Coordinate:", font=('Helvetica', '9'))
        self.xLabel.grid(row=0, column=0, padx=5.5, sticky='e')
        self.xEntry = tk.Entry(self.addFrame, width=6, font=('Helvetica', '9', 'bold'), validate='all',
                               justify='center', validatecommand=(vcmd, '%P'))
        self.xEntry.grid(row=0, column=1, padx=5, sticky='ew')
        self.xEntry.bind("<FocusOut>", lambda _:self.check_entry(self.xEntry, pag.size()[0]))

        self.yLabel = tk.Label(self.addFrame, text="Y-Coordinate:", font=('Helvetica', '9'))
        self.yLabel.grid(row=0, column=2, padx=5, sticky='e')
        self.yEntry = tk.Entry(self.addFrame, width=6, font=('Helvetica', '9', 'bold'), validate='all',
                               justify='center', validatecommand=(vcmd, '%P'))
        self.yEntry.grid(row=0, column=3, padx=5.5, sticky='e')
        self.yEntry.bind("<FocusOut>", lambda _: self.check_entry(self.yEntry, pag.size()[1]))

        self.resetButton = tk.Button(self.addFrame, text='Reset', font=('Helvetica', '7'), image=self.pixel,
                                     borderwidth=1, relief='flat', width=65, height=13, compound='center')
        self.resetButton.grid(row=0, column=4, padx=5, sticky='w')

        self.actionLabel = tk.Label(self.addFrame, text="Action Type:", font=('Helvetica', '9'))
        self.actionLabel.grid(row=1, column=0, padx=5, pady=(2, 2), sticky='e')

        self.optionButton = tk.Button(self.addFrame, text="           -- select an action --          " + u"\u2b9f",
                                      font=('Helvetica', '9'), image=self.pixel, width=219, height=13,
                                      compound='center', command=lambda: print("success"), borderwidth=1, relief='flat')
        self.optionButton.grid(row=1, column=1, columnspan=3, padx=5, pady=(2, 2), sticky='ew')

        self.optionsChoiceButton = tk.Button(self.addFrame, text=' ... ', font=('Helvetica', '7'), image=self.pixel,
                                             borderwidth=1, relief='flat', width=65, height=13, compound='center')
        self.optionsChoiceButton.grid(row=1, column=4, padx=5, pady=(2, 2), sticky='w')

        self.checkLabel = tk.Label(self.addFrame, text='Cursor back:', font=('Helvetica', '9'))
        self.checkLabel.grid(row=2, column=0, padx=5, pady=(2, 2), sticky='e')

        self.checkBox = cb.CheckBox(self.addFrame, highlightthickness=0, text='', image=self.pixel, width=15, height=15,
                                    relief='sunken', borderwidth=1, compound='center')
        self.checkBox.grid(row=2, column=1, padx=5, pady=(2, 2), sticky='w')

        self.delayLabel = tk.Label(self.addFrame, text='Delay before action:', font=('Helvetica', '9'))
        self.delayLabel.grid(row=2, column=2, padx=5, pady=(0, 2), sticky='w')

        self.delayEntry = tk.Entry(self.addFrame, width=6, font=('Helvetica', '9', 'bold'), validate='all',
                                   justify='center', validatecommand=(vcmd, '%P'))
        self.delayEntry.grid(row=2, column=3, padx=5, sticky='ew')
        self.delayEntry.bind("<FocusOut>", lambda _: self.check_entry(self.delayEntry, 999999))

        self.msLabel = tk.Label(self.addFrame, text='Milliseconds', font=('Helvetica', '9'))
        self.msLabel.grid(row=2, column=4, padx=5, pady=(0, 2), sticky='w')

        # self.checkButton = tk.Checkbutton(self.addFrame, offrelief='flat')
        # self.checkButton.grid(row=2, column=1, padx=0, pady=(2, 2), sticky='w')

        # self.test = tk.Button(self.addFrame, text='', width=70, height=0, image=self.pixel, compound='center')
        # self.test.grid(row=1, column=5, padx=5, pady=2, sticky='w')

        self.commentLabel = tk.Label(self.addFrame, text="Comment:", font=('Helvetica', '9'))
        self.commentLabel.grid(row=3, column=0, padx=5, sticky='e')
        self.commentEntry = tk.Entry(self.addFrame, font=('Helvetica', '9', 'bold'))
        self.commentEntry.grid(row=3, column=1, columnspan=5, padx=5, pady=(0, 5), sticky='we')

        self.clearButton = tk.Button(self.addFrame, text='C', image=self.pixel, height=13, compound='center',
                                     font=('Helvetica', '9'), relief='flat', borderwidth=1)
        self.clearButton.grid(row=3, column=6, padx=5, pady=(0, 5), sticky='w')

        self.addButtonOne = tk.Button(self.addFrame, text='Add to top', image=self.pixel, compound='center',
                                      font=('Helvetica', '9'), width=85)
        self.addButtonOne.grid(row=0, column=7, padx=5, pady=(0, 5), sticky='e', columnspan=2)
        self.addButtonTwo = tk.Button(self.addFrame, text='Add to bottom', image=self.pixel, compound='center',
                                      font=('Helvetica', '9'), width=85)
        self.addButtonTwo.grid(row=1, column=7, padx=5, pady=(0, 5), sticky='e', columnspan=2)
        self.addButtonThree = tk.Button(self.addFrame, text='Add to location', image=self.pixel, compound='center',
                                        font=('Helvetica', '9'), width=85)
        self.addButtonThree.grid(row=2, column=7, padx=5, pady=(0, 5), sticky='e', columnspan=2)

        self.repeatLabel = tk.Label(self.addFrame, text="Repeat count:", font=('Helvetica', '9'))
        self.repeatLabel.grid(row=3, column=7, padx=5, sticky='e')
        self.repeatEntry = tk.Entry(self.addFrame, width=6, font=('Helvetica', '9', 'bold'), validate='all',
                                    justify='center', validatecommand=(vcmd, '%P'))
        self.repeatEntry.grid(row=3, column=8, padx=5, sticky='w')
        self.repeatEntry.bind("<FocusOut>", lambda _: self.check_entry(self.repeatEntry, 999999))


        '''
        default_value = tk.StringVar(self)
        default_value.set('Left Click')
        choices = {'Left Click', 'this', 'is', 'a', 'test'}

        self.actionOptions = tk.OptionMenu(self.addFrame, default_value, *choices)
        self.actionOptions.grid(row=1, column=1, padx=5, sticky='w', columnspan=3)
        '''

        self.config()

    @staticmethod
    def callback(P):
        if P == '' or str.isdigit(P):
            return True
        return False

    def check_entry(self, entry, value):
        if entry.get() == '':
            return
        if int(entry.get()) > value:
            entry.delete(0, 'end')
            entry.insert(0, str(value))

    def config(self):
        self['bg'] = '#0E2B41'
        self.addFrame['bg'] = '#0E2B41'
        # self.buttonFrame['bg'] = '#0E2B41'
        self.titleFrame['bg'] = '#0E2B41'

        self.titleLabel['bg'] = '#0E2B41'
        self.titleLabel['fg'] = '#F4FFFD'

        self.xLabel['bg'] = '#0E2B41'
        self.xLabel['fg'] = '#F4FFFD'
        self.yLabel['bg'] = '#0E2B41'
        self.yLabel['fg'] = '#F4FFFD'

        self.actionLabel['bg'] = '#0E2B41'
        self.actionLabel['fg'] = '#F4FFFD'
        self.commentLabel['bg'] = '#0E2B41'
        self.commentLabel['fg'] = '#F4FFFD'

        self.checkLabel['bg'] = '#0E2B41'
        self.checkLabel['fg'] = '#F4FFFD'

        self.checkBox['bg'] = '#F4FFFD'
        self.checkBox['activebackground'] = '#0E2B41'
        self.checkBox['highlightbackground'] = '#0E2B41'
        self.checkBox['highlightcolor'] = '#0E2B41'

        self.clearButton['bg'] = '#F4FFFD'

        self.delayLabel['bg'] = '#0E2B41'
        self.delayLabel['fg'] = '#F4FFFD'
        self.msLabel['bg'] = '#0E2B41'
        self.msLabel['fg'] = '#F4FFFD'

        self.repeatLabel['bg'] = '#0E2B41'
        self.repeatLabel['fg'] = '#F4FFFD'

        config = {'bg': '#000F08',
                  'fg': '#F4FFFD',
                  'borderwidth': 1}
        self.addButtonOne.config(config)
        self.addButtonTwo.config(config)
        self.addButtonThree.config(config)



