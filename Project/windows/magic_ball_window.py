import tkinter as tk
from .windows_settings import window_settings
from content.magic_ball import MagicBallGame

# Глобальная переменная для хранения окна
mb_window = None

def create_magic_window(parent):
    global mb_window
    
    if mb_window is None or not mb_window.winfo_exists():
        mb_window = tk.Toplevel(parent)
        window_settings(mb_window, 500, 500)
        mb_window.title('Магический шар')
        
        MagicBallGame(mb_window) # Инициализация контента
        
    mb_window.deiconify() # Покзываем окно, если оно скрыто
    return mb_window