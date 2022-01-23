# modules
import tkinter as tk
from tkinter import *


class Btn(tk.Button):
    def __init__(self, master: None, text, icon, fg, bg):
        super().__init__(master)
        self.text = text
        self.icon = icon
        self.fg = fg
        self.bg = bg
        
        self["width"] = 300
        self["text"] = self.text
        self["font"] = (None, 20, "bold")
        self["image"] = self.icon,
        self["compound"] = "left"
        self["borderwidth"] = 0
        self["highlightthickness"] = 0
        self["activeforeground"] = self.bg
        self["activebackground"] = self.fg
        self["fg"] = self.fg
        self["bg"] = self.bg

        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)


    def on_enter(self, e):
        self["background"] = self.fg
        self["foreground"] = self.bg
    
    def on_leave(self, e):
        self["background"] = self.bg
        self["foreground"] = self.fg


        

