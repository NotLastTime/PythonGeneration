import tkinter as tk
from .windows_settings import window_settings
from content.caesar_cipher import CaesarCipherGame

# Глобальная переменная для хранения окна
cc_window = None

def create_caesar_game_window(parent):
    global cc_window
    
    if cc_window is None or not cc_window.winfo_exists():
        cc_window = tk.Toplevel(parent)  # Используем Toplevel для создания нового окна
        window_settings(cc_window, 500, 500)
        cc_window.title('Шифр Цезаря')
        
        CaesarCipherGame(cc_window) # Инициализация контента
    
    cc_window.deiconify()  # Показываем окно, если оно было скрыто
    return cc_window
