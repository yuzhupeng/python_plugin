import tkinter as tk
from src.gui.interfaces import LabelFrame
from src.common import config
from src.modules.listener import Listener

class Status(LabelFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, 'Status', **kwargs)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(3, weight=1)

        self.curr_cb = tk.StringVar()
        self.curr_routine = tk.StringVar()
        self.start_btn_text = tk.StringVar()

        self.cb_label = tk.Label(self, text='Command Book:')
        self.cb_label.grid(row=0, column=1, padx=5, pady=(5, 0), sticky=tk.E)
        self.cb_entry = tk.Entry(self, textvariable=self.curr_cb, state=tk.DISABLED)
        self.cb_entry.grid(row=0, column=2, padx=(0, 5), pady=(5, 0), sticky=tk.EW)

        self.r_label = tk.Label(self, text='Routine:')
        self.r_label.grid(row=1, column=1, padx=5, pady=(0, 5), sticky=tk.E)
        self.r_entry = tk.Entry(self, textvariable=self.curr_routine, state=tk.DISABLED)
        self.r_entry.grid(row=1, column=2, padx=(0, 5), pady=(0, 5), sticky=tk.EW)
        self.start_btn = tk.Button(self, textvariable=self.start_btn_text, width=6, command=Listener.toggle_enabled)
        self.start_btn_text.set('start') 
        self.start_btn.grid(row=2, column=1,columnspan=2, padx=(0, 5), pady=(0, 5), sticky="")
    
    def set_cb(self, string):
        self.curr_cb.set(string)

    def set_routine(self, string):
        self.curr_routine.set(string)
    
    def set_start_btn(self, string):
        self.start_btn_text.set(string)

    # def toggle_script_enable(self):
    #     print('toggle_script_enable test')
    #     Listener.toggle_enabled()
    #     if not config.enabled:
    #         self.start_btn_text.set('start') 
    #     else:
    #         self.start_btn_text.set('pause') 
