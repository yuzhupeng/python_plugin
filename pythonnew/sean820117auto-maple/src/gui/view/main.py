"""Displays the current minimap as well as various information regarding the current routine."""

import tkinter as tk
from src.gui.view.details import Details
from src.gui.view.minimap import Minimap
from src.gui.view.routine import Routine
from src.gui.view.status import Status
from src.gui.interfaces import Tab


class View(Tab):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, 'View', **kwargs)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.minimap = Minimap(self)
        self.minimap.grid(row=0, column=1, sticky=tk.NSEW, padx=5, pady=5)

        self.status = Status(self)
        self.status.grid(row=1, column=1, sticky=tk.NSEW, padx=5, pady=5)

        self.details = Details(self)
        self.details.grid(row=2, column=1, sticky=tk.NSEW, padx=5, pady=5)

        self.routine = Routine(self)
        self.routine.grid(row=0, column=0, rowspan=3, sticky=tk.NSEW, padx=5, pady=5)
