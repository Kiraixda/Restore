import os
import sqlite3 as sql
from sqlite3 import Error
from tkinter import messagebox

class Database:
    def __init__(self, db):
        try:
            if not os.path.exists(os.path.join("Database", f"{db}")):
                os.makedirs(os.path.join("Database"))
            
            self.conn = sql.connect(os.path.join("Database", f"{db}"))
            self.cur = self.conn.cursor()
            sql_create_table = """CREATE TABLE IF NOT EXISTS restore (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                service TEXT,
                email TEXT,
                password TEXT,
                saved_at TIMESTAMP
            )"""
            self.cur.execute(sql_create_table)
            self.conn.commit()
        
        except Error as err:
            messagebox.showerror("Error", f"{err}")
    

    def save(self, service, email, password, timestamp):
        try:
            sql_save = """INSERT INTO restore (service, email, password, saved_at) VALUES (?, ?, ?, ?)"""
            self.cur.execute(sql_save, (service, email, password, timestamp))
            self.conn.commit()
        
        except Error as err:
            messagebox.showerror("Error", f"{err}")


    def close(self):
        try:
            self.cur.close()
            self.conn.close()

        except Error as err:
            messagebox.showerror("Error", f"{err}")

