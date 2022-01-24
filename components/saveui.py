# modules
import os, datetime
import tkinter as tk
import sqlite3 as sql
import colors as c
from tkinter import *
from tkinter import messagebox
from sqlite3 import Error
from PIL import Image, ImageTk

# files
from components.better_button import Better_button

# saveui class
class SaveUI(tk.Tk):
    def __init__(self, master, database):
        super().__init__()
        self.master = master
        self.db = database
        self.configure(background=c.bg)
        self.wm_title("Re:store (save)")
        self.wm_protocol("WM_WINDOW_DESTROY", self.close)
        self.bind("<Escape>", self.close)

        # frame creation
        self.frame = Frame(self)
        self.frame.configure(background=c.bg)
        self.frame.pack(expand=True)

        # cancel button
        self.cancel_img = Image.open(os.path.join("images", "back.png"))
        self.cancel_img = self.cancel_img.resize((50, 50), Image.ANTIALIAS)
        self.cancel_icon = ImageTk.PhotoImage(self.cancel_img, master=self)
        self.cancel_btn = Better_button(self.frame,
                                    "C A N C E L",
                                    self.cancel_icon,
                                    c.deletecolor,
                                    c.bg,
                                    command=self.close)
        self.cancel_btn.pack(side=LEFT)

        #self.submit_img = Image.open(os.path.join("images", "delete.png"))
        #self.submit_img = self.submit_img.resize((50, 50), Image.ANTIALIAS)
        #self.submit_icon = ImageTk.PhotoImage(self.submit_img, master=self)
        self.submit_btn = Better_button(self.frame,
                                    "S U B M I T",
                                    self.cancel_icon,
                                    c.submitcolor,
                                    c.bg,
                                    None)
        self.submit_btn.pack(side=LEFT)


    def close(self, e= None):
        self.master.wm_deiconify()
        self.destroy()
