# modules
import os, datetime
import tkinter as tk
import colors as c
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# files
from components.widgets.better_button import Better_button
from components.widgets.better_entry import Better_entry

# saveui class
class SaveUI(tk.Tk):
    def __init__(self, master, database):
        super().__init__()
        self.master = master
        self.db = database
        self.configure(background=c.bg)
        self.wm_title("Re:store (save)")
        self.wm_protocol("WM_DELETE_WINDOW", self.close)
        self.bind("<Escape>", self.close)
        self.bind("<Return>", self.on_submit)

        # service parts
        self.service_txt = StringVar(self)
        self.service_label = Label(self,
                                bg=c.bg,
                                fg=c.white,
                                text="S E R V I C E",
                                font=("bold", 16),
                                justify="center",
                                padx=20,
                                pady=20
                                ).grid(row=0, column=0, sticky=W)        

        self.service_entry = Better_entry(self, 
                                    textvariable=self.service_txt,
                                    font=("bold", 16),
                                    bg=c.bg,
                                    fg=c.white,
                                    justify="center",
                                    insertbackground=c.white).grid(row=0, column=1)


        # email parts
        self.email_txt = StringVar(self)
        self.email_label = Label(self,
                                bg=c.bg,
                                fg=c.white,
                                text="E M A I L",
                                font=("bold", 16),
                                justify="center",
                                padx=20,
                                pady=20
                                ).grid(row=1, column=0, sticky=W)        

        self.email_entry = Better_entry(self, 
                                    textvariable=self.email_txt,
                                    font=("bold", 16),
                                    bg=c.bg,
                                    fg=c.white,
                                    justify="center",
                                    insertbackground=c.white).grid(row=1, column=1, padx=20)


        # password parts
        self.password_txt = StringVar(self)
        self.password_label = Label(self,
                                bg=c.bg,
                                fg=c.white,
                                text="P A S S W O R D",
                                font=("bold", 16),
                                justify="center",
                                padx=20,
                                pady=20
                                ).grid(row=2, column=0, sticky=W)        

        self.password_entry = Better_entry(self, 
                                    textvariable=self.password_txt,
                                    font=("bold", 16),
                                    bg=c.bg,
                                    fg=c.white,
                                    justify="center",
                                    insertbackground=c.white).grid(row=2, column=1, padx=20)
        

        # submit & cancel
        self.cancel_img = Image.open(os.path.join("images", "back.png"))
        self.cancel_img = self.cancel_img.resize((50, 50), Image.ANTIALIAS)
        self.cancel_icon = ImageTk.PhotoImage(self.cancel_img, master=self)
        self.cancel_btn = Better_button(self,
                                        "C A N C E L",
                                        self.cancel_icon,
                                        c.deletecolor,
                                        c.bg,
                                        self.close).grid(row=3, column=0)
        
        self.submit_img = Image.open(os.path.join("images", "submit.png"))
        self.submit_img = self.submit_img.resize((50, 50), Image.ANTIALIAS)
        self.submit_icon = ImageTk.PhotoImage(self.submit_img, master=self)
        self.submit_btn = Better_button(self,
                                        "S U B M I T",
                                        self.submit_icon,
                                        c.submitcolor,
                                        c.bg,
                                        self.on_submit).grid(row=3, column=1)



    def on_submit(self, e= None):
        if self.service_txt.get() and self.email_txt.get() and self.password_txt.get():
            service = self.service_txt.get().lower()
            email = self.email_txt.get()
            password = self.password_txt.get()
            timestamp = datetime.datetime.now().strftime("%d/%m/%Y")
            self.db.save(service, email, password, timestamp)
            self.close()
        
        else:
            messagebox.showwarning("Warning", "Fill in every field")

    def close(self, e= None):
        self.master.wm_deiconify()
        self.destroy()
