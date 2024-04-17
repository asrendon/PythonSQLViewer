import mysql.connector
import tkinter as tk
from tkinter import messagebox

from Pages.db_page import show_dbs
from Pages.table_page import list_tables
from state import app_state

def login():
    global username_entry, password_entry, host_entry, db_entry
    # Predefined username and password
    try:
        if db_entry.get()=="":
            mydb = mysql.connector.connect(
            host=host_entry.get(),
            user=username_entry.get(),
            password=password_entry.get()
            )
            app_state["user"]=username_entry.get()
            app_state["password"]=password_entry.get()
            app_state["host"]= host_entry.get()
            app_state["logged_in"]= True
            cursor=mydb.cursor()
            databases = ("show databases")
            cursor.execute(databases)
            db_list=[]
            for (db) in cursor:
                db_list.append(db[0])
            app_state["db_list"]=db_list
            root.destroy()
            dbview= show_dbs()
            dbview.mainloop()
        else:
            mydb = mysql.connector.connect(
            host=host_entry.get(),
            user=username_entry.get(),
            password=password_entry.get(),
            database=db_entry.get()
            )
            app_state["user"]=username_entry.get()
            app_state["password"]=password_entry.get()
            app_state["host"]= host_entry.get()
            app_state["logged_in"]= True
            db=db_entry.get()
            root.destroy()
            tbList= list_tables(db)
            tbList.mainloop()
        
    except Exception as e:
        messagebox.showerror("Login Failed", e)
        print("An exception occurred:", type(e).__name__) 

    
def main():
    global username_entry, password_entry, host_entry,root,db_entry
    # Create the main window
    root = tk.Tk()
    root.title("MySQL Database Login")

    # Set the size of the window
    root.geometry("300x220")

    # Host label and text entry box
    tk.Label(root, text="Host:").pack()
    host_entry = tk.Entry(root, width=25)
    #host_entry.insert(0,"")
    host_entry.pack()

    # Username label and text entry box
    tk.Label(root, text="Username:").pack()
    username_entry = tk.Entry(root, width=25)
    #username_entry.insert(0,"")
    username_entry.pack()

    # Password label and password entry box
    tk.Label(root, text="Password:").pack()
    password_entry = tk.Entry(root, show='*', width=25)
    #password_entry.insert(0,"")
    password_entry.pack()

    # Optional Database label and password entry box
    tk.Label(root, text="Database (opt):").pack()
    db_entry = tk.Entry(root, width=25)
    db_entry.pack()

    # Login button
    login_button = tk.Button(root, text="Login", command=login)
    login_button.pack(pady=10)

    # Start the event loop
    root.mainloop()

    


if __name__ == "__main__":
    main()