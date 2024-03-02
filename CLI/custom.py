import customtkinter

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

def custom_display(window):
    
    apparence_label = customtkinter.CTkLabel(window, text="choose an apparence", font=("Helvetica", 18))
    apparence_label.pack(pady=10)
    combobox_apparence = customtkinter.CTkComboBox(master=window,
                                        values=["light", "dark", "system"],
                                        command=combobox_callback_apparence)
    combobox_apparence.pack(padx=20, pady=10)
    combobox_apparence.set("light")
    
    # theme_label = customtkinter.CTkLabel(window, text="choose an theme", font=("Helvetica", 18))
    # theme_label.pack(pady=10)
    # combobox_theme = customtkinter.CTkComboBox(master=window,
    #                                     values=["green", "blue", "yellow"],
    #                                     command=combobox_callback_theme)
    # combobox_theme.pack(padx=20, pady=10)
    # combobox_theme.set("light") 
