import mysql.connector

import tkinter as tk
from tkinter import messagebox

from state import app_state

def on_item_selected(event):
    # Getting index of the selected item
    w = event.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    messagebox.showinfo("Selection", f"You selected: {value}")

def list_tables(db):
    tb_window = tk.Tk()
    tb_window.title(db+" Table List")
    tk.Label(tb_window, text="Select a Table").pack(pady=20)
    mydb = mysql.connector.connect(
    host=app_state["host"],
    user=app_state["user"],
    password=app_state["password"],
    database=db
    )
    
    cursor=mydb.cursor()
    cursor.execute("show tables")
    tables= cursor.fetchall()
    print(tables)

    listbox = tk.Listbox(tb_window, height=10, width=50, border=0)
    listbox.bind('<<ListboxSelect>>', on_item_selected)
    for (table,) in tables:
        listbox.insert(tk.END, table)
    
    listbox.pack(pady=20)
    tb_window.geometry("400x300")
    return tb_window
    
    

