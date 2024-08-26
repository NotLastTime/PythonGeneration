import tkinter as tk
from .windows_settings import window_settings
from content.calculator import Calclator

cg_window = None

def create_calculator_window(parent):
    global cg_window
    
    if cg_window == None or not cg_window.winfo_exists():
        cg_window = tk.Toplevel(parent)
        window_settings(cg_window, 500, 500)
        cg_window.title('Кальпулятор систем счилсения')
        
        Calclator(cg_window)
        
    cg_window.deiconify()
    return cg_window
        