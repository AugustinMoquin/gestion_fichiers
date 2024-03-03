from db_insert import *
import customtkinter
from tkinter import filedialog
from global_var import *

def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.json*"),
                                                       ("all files",
                                                        "*.*")))
      
    # Change label contents
    label_file_explorer.configure(text="File Opened: "+filename)
    
    size = 1024 * 1024
    if filename != None:
        err = is_valid_json_file(filename, size)
        if err:
            sql_to_db(filename)
        else:
            label_file_explorer.configure(text="err")
    

def file_explore(window):
    global label_file_explorer
    label_file_explorer = customtkinter.CTkLabel(window, 
                            text = "File Explorer using Tkinter",
                            width = 100, height = 4)
    label_file_explorer.pack()
    
      
    button_explore = customtkinter.CTkButton(window, 
                        text = "Browse Files",
                        command = browseFiles)
    button_explore.pack()

    

#     # sql_to_db("../SERVER/json_file/Film.json")
