# modules
import os, sys
import tkinter as tk
import colors as c
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk


# files
from components.btn import Btn
from components.database import Database


# main window class
class MainUI(tk.Tk):
    def __init__(self, title):
        # window initialization
        super().__init__()
        self.db = Database("Restore.db")
        self.configure(background=c.bg)
        self.wm_title(f"{title}")
        self.img = Image.open(os.path.join("images", "logo.png"))
        self.icon = ImageTk.PhotoImage(self.img)
        self.wm_iconphoto(True, self.icon)
        self.protocol("WM_DELETE_WINDOW", self.close)
        self.bind("<Escape>", self.on_closing)


        # create frame
        self.frame = Frame(self)
        self.frame.configure(background=c.bg)
        self.frame.pack(expand=True)


        # screen icon
        self.icon_label = Label(self.frame,
                                text=f"{title}",
                                image=self.icon,
                                compound="top",
                                font=(None, 30, "bold"),
                                fg="#ffffff",
                                bg=c.bg).pack(side=TOP)


        # buttons
        # save button
        self.save_img = Image.open(os.path.join("images", "save.png"))
        self.save_img = self.save_img.resize((50, 50), Image.ANTIALIAS)
        self.save_icon = ImageTk.PhotoImage(self.save_img)
        self.save_btn = Btn(self.frame, 
                            "S A V E",
                            self.save_icon,
                            c.savecolor,
                            c.bg)
        self.save_btn.pack()


        # search button
        self.search_img = Image.open(os.path.join("images", "search.png"))
        self.search_img = self.search_img.resize((50, 50), Image.ANTIALIAS)
        self.search_icon = ImageTk.PhotoImage(self.search_img)
        self.search_btn = Btn(self.frame,
                            "S E A R C H",
                            self.search_icon,
                            c.searchcolor,
                            c.bg)
        self.search_btn.pack()


        # update button
        self.update_img = Image.open(os.path.join("images", "update.png"))
        self.update_img = self.update_img.resize((50, 50), Image.ANTIALIAS)
        self.update_icon = ImageTk.PhotoImage(self.update_img)
        self.update_btn = Btn(self.frame,
                            "U P D A T E",
                            self.update_icon,
                            c.updatecolor,
                            c.bg)
        self.update_btn.pack()

        
        # generate button
        self.gen_img = Image.open(os.path.join("images", "generate.png"))
        self.gen_img = self.gen_img.resize((50, 50), Image.ANTIALIAS)
        self.gen_icon = ImageTk.PhotoImage(self.gen_img)
        self.gen_btn = Btn(self.frame,
                        "G E N E R A T E",
                        self.gen_icon,
                        c.gencolor,
                        c.bg)
        self.gen_btn.pack()


        # delete button
        self.delete_img = Image.open(os.path.join("images", "delete.png"))
        self.delete_img = self.delete_img.resize((50, 50), Image.ANTIALIAS)
        self.delete_icon = ImageTk.PhotoImage(self.delete_img)
        self.delete_btn = Btn(self.frame,
                            "D E L E T E",
                            self.delete_icon,
                            c.deletecolor,
                            c.bg)
        self.delete_btn.pack()
    
    
    # closing everything
    def on_closing(self, e):
        self.db.close()
        sys.exit()
    

    def close(self):
        self.db.close()
        sys.exit()


# main loop
if __name__ == "__main__":
    app = MainUI("RE:STORE")
    app.mainloop()