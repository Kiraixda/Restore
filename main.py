# modules
import os, sys
import tkinter as tk
import colors as c
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk


# files
from components.better_button import Better_button
from components.database import Database
from components.saveui import SaveUI

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
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
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
        self.save_btn = Better_button(self.frame, 
                            "S A V E",
                            self.save_icon,
                            c.savecolor,
                            c.bg,
                            self.on_save).pack()
        


        # search button
        self.search_img = Image.open(os.path.join("images", "search.png"))
        self.search_img = self.search_img.resize((50, 50), Image.ANTIALIAS)
        self.search_icon = ImageTk.PhotoImage(self.search_img)
        self.search_btn = Better_button(self.frame,
                            "S E A R C H",
                            self.search_icon,
                            c.searchcolor,
                            c.bg,
                            None).pack()


        # update button
        self.update_img = Image.open(os.path.join("images", "update.png"))
        self.update_img = self.update_img.resize((50, 50), Image.ANTIALIAS)
        self.update_icon = ImageTk.PhotoImage(self.update_img)
        self.update_btn = Better_button(self.frame,
                            "U P D A T E",
                            self.update_icon,
                            c.updatecolor,
                            c.bg,
                            None).pack()

        
        # generate button
        self.gen_img = Image.open(os.path.join("images", "generate.png"))
        self.gen_img = self.gen_img.resize((50, 50), Image.ANTIALIAS)
        self.gen_icon = ImageTk.PhotoImage(self.gen_img)
        self.gen_btn = Better_button(self.frame,
                        "G E N E R A T E",
                        self.gen_icon,
                        c.gencolor,
                        c.bg,
                        None).pack()


        # delete button
        self.delete_img = Image.open(os.path.join("images", "delete.png"))
        self.delete_img = self.delete_img.resize((50, 50), Image.ANTIALIAS)
        self.delete_icon = ImageTk.PhotoImage(self.delete_img)
        self.delete_btn = Better_button(self.frame,
                            "D E L E T E",
                            self.delete_icon,
                            c.deletecolor,
                            c.bg,
                            None).pack()
    
    
    # closing everything
    def on_closing(self, e = None):
        self.db.close()
        sys.exit()


    # commands
    def on_save(self):
        self.withdraw()
        saveui = SaveUI(self, self.db)
        saveui.mainloop()
        


# main loop
if __name__ == "__main__":
    app = MainUI("RE:STORE")
    app.mainloop()