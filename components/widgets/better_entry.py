# modules
import tkinter as tk
from tkinter import *
import colors as c

class Better_entry(tk.Entry):
    def __init__(self, master: None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self["highlightthickness"] = 2
        self.bind("<FocusIn>", self.on_focus)
        self.bind("<FocusOut>", self.on_unfocus)

    def on_focus(self, e):
        self.configure(highlightbackground=c.focused, highlightcolor=c.focused) 
    
    def on_unfocus(self, e):
        if not self.get():
            self.configure(highlightbackground=c.deletecolor, highlightcolor=c.deletecolor)
        
        else:
            self.configure(highlightbackground=c.submitcolor, highlightcolor=c.submitcolor)