import customtkinter
from global_var import *

def toggle_appearance_mode(app):
    current_mode = app.appearance_mode()
    new_mode = "light" if current_mode == "dark" else "dark"
    app.set_appearance_mode(new_mode)
    customtkinter.set_appearance_mode(new_mode)
    

def change_color_theme(app):
    current_theme = app.theme()
    print(current_theme)
    new_theme = "light" if current_theme == "dark" else "dark"
    customtkinter.set_default_color_theme(new_theme)
    
def combobox_callback_apparence(choice):
    customtkinter.set_appearance_mode(choice)
        
# def combobox_callback_theme(choice):
#     customtkinter.set_default_color_theme(choice)

def combobox_callback_family(choice):
    custom_font[0] = choice

def combobox_callback_size(choice):
    custom_font[1] = choice


def custom_display(window):
    #theme
    apparence_label = customtkinter.CTkLabel(window, text="choose an apparence", font=custom_font)
    apparence_label.pack(pady=10)
    combobox_apparence = customtkinter.CTkComboBox(master=window,
                                        values=["light", "dark", "system"],
                                        command=combobox_callback_apparence)
    combobox_apparence.pack(padx=20, pady=10)
    combobox_apparence.set("light")
    #font family
    font_label = customtkinter.CTkLabel(window, text="choose a font family and a size", font=custom_font)
    font_label.pack(pady=10)
    combobox_family = customtkinter.CTkComboBox(master=window,
                                        values=["Arial", "Times New Roman", "Courier", "Verdana", "Helvetica"],
                                        command=combobox_callback_family)
    combobox_family.pack(padx=20, pady=10)
    combobox_family.set("Helvetica")
    
    combobox_size = customtkinter.CTkComboBox(master=window,
                                        values=["Arial", "Times New Roman", "Courier", "Verdana", "Helvetica"],
                                        command=combobox_callback_size)
    combobox_size.pack(padx=20, pady=10)
    combobox_size.set("12")
    
