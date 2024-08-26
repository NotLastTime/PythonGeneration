import tkinter as tk

def window_settings(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')
    window.resizable(False, False)
    #window.overrideredirect(True)
    
def button_settings(parent, text, command, **kwargs):
    button=tk.Button(
        parent,
        text=text,
        command=command,
        font=('Arial', 10),
        background='lightblue', activebackground='lightblue',
        width=24,
        **kwargs
    ); return button
        