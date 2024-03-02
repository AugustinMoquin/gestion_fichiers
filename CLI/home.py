import customtkinter
from customtkinter import *
import tkinter as ttk
from tkinter import *
import tkinter.messagebox
import sys
import sqlite3
from graph_creation import *
from add_json import *
from custom import *

def db_connect():
    db_path = '../SERVER/db/tkinter.db'  # Replace with the desired SQLite database file path
    conn = sqlite3.connect(db_path)
    return conn

conn = db_connect()
cursor = conn.cursor()

#-------------------------------#
# def get_table_size(table):
#     cursor.execute(f"SELECT page_count * page_size FROM pragma_page_size, pragma_page_count WHERE name = '{table}';")
#     size = cursor.fetchone()[0]
#     return size

#-------------------------------#
#get the table names
def get_table_name():
    cursor = conn.cursor()

    table_query = "SELECT name FROM sqlite_master WHERE type='table';"
    cursor.execute(table_query)
    table_names = cursor.fetchall()
    # conn.close()

    table_names = [table[0] for table in table_names]

    return table_names

#--------------------------------------------#
#create a new window to display the data
def show_db(window, table_name, app):
    window = customtkinter.CTkToplevel(master=window)
    window.geometry("1000x800")
    window.title(table_name)
    window.focus()
    
    scroll_frame = customtkinter.CTkScrollableFrame(window, orientation="horizontal") 
    scroll_frame.pack(anchor=N, fill=BOTH, expand=True, side=LEFT)
    table_view(scroll_frame, table_name, app)

#-------------------------------------#
#fetch the data and the name of the column
def fetch_data(table_name):
    
    try :
        #--------------------------------#
        query = f"SELECT * FROM {table_name}"
        cursor.execute(query)

        rows = cursor.fetchall()
        #--------------------------------#
        query = f"PRAGMA table_info({table_name})"
        cursor.execute(query)

        columns_info = cursor.fetchall()

        column_names = [column[1] for column in columns_info]
    except Exception as e:
        print(f"there was an error : {e}")
    return rows, column_names

#--------------------------------------#
#db managment (delete)
def delete_row(table, id, Dwindow, app):
    try :
        query = f"DELETE FROM {table} WHERE rowid = {id};"
        cursor.execute(query)
        conn.commit()
        Dwindow.withdraw()
        #to reset the rowid
        cursor.execute("VACUUM")
        conn.commit()
        #reload the page
        show_db(Dwindow, table, app)
    except Exception as e:
        print(f"there was a problem during deletion : {e}")

def delete_tab(table, Dwindow, app):
    try:
        drop_table_query = f"DROP TABLE IF EXISTS {table}"

        cursor.execute(drop_table_query)
        conn.commit()
        #close the window as the table is no more
        Dwindow.withdraw()
        app.withdraw()
        #reopen the main screen to reload the data
        main_page()
    except sqlite3.Error as e:
        print(f"Error deleting table '{table}': {e}")

#-------------------------------------#
#viewing the data from the db
def table_view(window, table_name, app):
    rows, columns = fetch_data(table_name)

    #display the names of the column
    Ncolumn = 0
    for column in columns:
        text = customtkinter.CTkButton(window, text=column, corner_radius=2, hover=False)
        text.grid(row=0, column=Ncolumn, padx=20, pady=20)
        Ncolumn+=1
    delete = customtkinter.CTkButton(window, text="🗑", corner_radius=2, width=10, fg_color="red", command=lambda :delete_tab(table_name, window, app))
    delete.grid(row=0, column=Ncolumn, padx=20, pady=20)
    
    # sep = customtkinter.CTkLabel(fg_color="white", height=1)
    # sep.pack()
    
    Mrows = 1
    for items in rows:
        Mcolumn = 0
        
        for item in items:
            # print(item)
            text = customtkinter.CTkButton(window, text=item, corner_radius=2, hover=False, fg_color="grey")
            text.grid(row=Mrows, column=Mcolumn, padx=20, pady=20)
            Mcolumn+=1
        delete = customtkinter.CTkButton(window, text="🗑", corner_radius=2, width=10, fg_color="orange", command=lambda id=Mrows:delete_row(table_name, id, window, app))
        delete.grid(row=Mrows, column=Mcolumn, padx=20, pady=20)
        Mrows+=1
        
#---------------------------------------#
#creating a tab view for a menu

def tab_view(view):
    tabView = customtkinter.CTkTabview(view, width=1000, height=800)
    tabView.pack(padx=20, pady = 20)

    tabView.add("tables")
    tabView.add("graph")
    tabView.add("custom")
    tabView.add("add")

    tabView.set("tables")

    return tabView

#------------------------------------------#

#---------------------------------------------#
def main_page():
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue")

    app = customtkinter.CTk()
    app.geometry("1000x700")
    #------------------------------#
    table_names = get_table_name()
    #------------------------------#
    #------------------------------#
    Vrow = 0
    Vcolumn = 0
    temp=1
    #------------------------------#
    
    # set the tab view
    tabView = tab_view(app)
    #first tab view
    for table in table_names:
        #get the size of the table
        # size = get_table_size(table)

        table_button = customtkinter.CTkButton(master=tabView.tab("tables"), text=f"nom : {table} \n size : a venir", command=lambda n=table: show_db(tabView, n, app)) 
        table_button.grid(row=Vrow, column=Vcolumn, padx=20, pady=20)
        Vcolumn+=1
        temp+=1
        #go back to the lobby
        if temp%5 == 0:
            Vrow +=1
            Vcolumn = 0
    #second tab view
    graph_display(tabView.tab("graph"), table_names)

    #third tab view 
    custom_display(tabView.tab("custom"))

    #fourth tab view
    file_explore(tabView.tab("add"))

    app.mainloop()

def main():

    main_page()
    

    cursor.close()
    conn.close()

main()