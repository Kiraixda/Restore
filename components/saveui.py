# modules
import os, sys, datetime
import tkinter as tk
import sqlite3 as sql
import colors as c
from tkinter import *
from tkinter import messagebox
from sqlite3 import Error
from PIL import Image, ImageTk

# files
from components.better_button import Better_button

class SaveUI(tk.Tk):
    def __init__(self, master, database):
        super().__init__()
        self.master = master
        self.db = database
        self.configure(background=c.bg)
        self.wm_title("Re:store (save)")
        self.wm_protocol("WM_WINDOW_DESTROY", self.close)
        self.bind("<Escape>", self.close)


    def close(self, e= None):
        self.master.wm_deiconify()
        self.destroy()
