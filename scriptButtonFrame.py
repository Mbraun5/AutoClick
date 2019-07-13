import tkinter as tk


class ScriptButtonFrame(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)

        # for copying purposes
        self.args = args
        self.kwargs = kwargs

        dimensions = args[0]
        self.values = args[1]

        self.name = args[1][0]
        self.x = int(args[1][1])
        self.y = int(args[1][2])
        self.curs_back = args[1][3]
        self.delay = args[1][4]
        self.repeat = int(args[1][5])
        self.comment = args[1][6]

        for i in range(1, 8):
            if i == 4:
                value = 'No' if self.values[i-1] is False else 'Yes'
            else:
                value = self.values[i-1]
            new_btn = tk.Button(self, text=value, anchor='w', padx=6, bg='#ffffff', borderwidth=0, relief='flat',
                                font=('Helvetica', '9'))
            if i == 7:
                self.commentButton = new_btn
            else:
                new_btn.config(width=dimensions[i])

        for btn in self.winfo_children():
            btn.pack(side='left')

        self.commentButton.pack(side='left', expand=True, fill='both')

    def set_active(self):
        for btn in self.winfo_children():
            btn.config(self.master.master.master.master.active_config)

    def set_passive(self):
        for btn in self.winfo_children():
            btn.config(self.master.master.master.master.passive_config)

    def copy(self):
        return ScriptButtonFrame(self.master, self.args[0], self.args[1])








