import tkinter as tk
from .windows_settings import window_settings
from content.choice import Choice

# Глобальная переменная для хранения окна
ch_window = None

def create_choice_window(parent):
    global ch_window
    
    if ch_window is None or not ch_window.winfo_exists():
        ch_window = tk.Toplevel(parent)
        window_settings(ch_window, 500, 500)
        ch_window.title('PYTHON GENERATION')
        
        Choice(ch_window) # Инициализация контента
        
    ch_window.deiconify() # Показываем окно, если оно было скрыто    
    return ch_window
