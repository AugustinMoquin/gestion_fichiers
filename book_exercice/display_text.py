import tkinter as tk
from tkinter import Scrollbar, Text

def display(content):

    window = tk.Tk()
    window.geometry("600x900")
    window.title("Henry Jones")
    
    
    scrollbar = Scrollbar(window)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Create a text widget
    text_widget = Text(window, wrap=tk.WORD, yscrollcommand=scrollbar.set)
    text_widget.pack(expand=True, fill=tk.BOTH)
    scrollbar.config(command=text_widget.yview)
    
    text_widget.delete(1.0, tk.END)  # Clear previous text
    text_widget.insert(tk.END, content)

    window.mainloop()
    