import tkinter as tk


class ScriptButtonFrame(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        print(self.master)

        dimensions = args[0]
        values = args[1]

        for i in range(1, 8):
            if i == 4:
                value = 'No' if values[i-1] is False else 'Yes'
            else:
                value = values[i-1]
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








