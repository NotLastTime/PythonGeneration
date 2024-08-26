import tkinter as tk
from .windows_settings import window_settings
from content.guess_number import GuessNumbersGame

# Глобальная переменная для хранения окна
gn_window = None

def create_guess_window(parent):
    global gn_window
    
    if gn_window is None or not gn_window.winfo_exists():
        gn_window = tk.Toplevel(parent)
        window_settings(gn_window, 500, 500)
        gn_window.title('Числовая угадайка')
        
        GuessNumbersGame(gn_window) # Инициализация контента
        
    gn_window.deiconify() # Показываем окно, если оно было скрыто    
    return gn_window
