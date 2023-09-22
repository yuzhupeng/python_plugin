"""Displays the current minimap as well as various information regarding the current routine."""

import tkinter as tk
from src.easymaple.gui.view.details import Details
from src.easymaple.gui.view.minimap import Minimap
from src.easymaple.gui.view.routine import Routine
from src.easymaple.gui.view.status import Status
from src.easymaple.gui.interfaces import Tab


class View(Tab):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, 'View', **kwargs)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(3, weight=1)

        self.minimap = Minimap(self)
        self.minimap.grid(row=0, column=2, sticky=tk.NSEW, padx=10, pady=10)

        self.status = Status(self)
        self.status.grid(row=1, column=2, sticky=tk.NSEW, padx=10, pady=10)

        self.details = Details(self)
        self.details.grid(row=2, column=2, sticky=tk.NSEW, padx=10, pady=10)

        self.routine = Routine(self)
        self.routine.grid(row=0, column=1, rowspan=3, sticky=tk.NSEW, padx=10, pady=10)
