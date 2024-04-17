import tkinter as tk
from tkinter import messagebox

from state import app_state
from Pages.table_page import list_tables

def on_item_selected_db(event):
    # Getting index of the selected item
    w = event.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    #messagebox.showinfo("Selection", f"You selected: {value}")
    #db_window.destroy()
    tbList= list_tables(value)
    tbList.mainloop()

def show_dbs():
    global db_window
    db_window = tk.Tk()
    db_window.title("DB List")
    tk.Label(db_window, text="Select a Database").pack(pady=20)
    
    db_list = app_state["db_list"]
    print(db_list)
    listbox = tk.Listbox(db_window, height=10, width=50, border=0)
    listbox.bind('<<ListboxSelect>>', on_item_selected_db)
    for db in db_list:
        listbox.insert(tk.END, db)
    
    listbox.pack(pady=20)
    db_window.geometry("400x300")
    return db_window
    
    

