import tkinter as tk
from .windows_settings import window_settings
from content.passwords_gen import PasswordsGenerator

pg_window = None

def create_pass_gen_window(parent):
    global pg_window
    
    if pg_window is None or not pg_window.winfo_exists():
        pg_window = tk.Toplevel(parent)
        window_settings(pg_window, 500,500)
        pg_window.title('Генератор паролей')
        
        PasswordsGenerator(pg_window)
        
    pg_window.deiconify()
    return pg_window    