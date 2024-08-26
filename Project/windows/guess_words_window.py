import tkinter as tk
from .windows_settings import window_settings
from content.guess_words import GuessWordGame

# Глобальная переменная для хранения окна
gw_window = None

def create_guess_word_window(parent):
    global gw_window
    
    if gw_window is None or not gw_window.winfo_exists():
        gw_window = tk.Toplevel(parent)
        window_settings(gw_window, 500, 500)
        gw_window.title('Угадайка слов')
        
        GuessWordGame(gw_window) # Инициализация контента
        
    gw_window.deiconify() # Показываем окно, если оно было скрыто    
    return gw_window
