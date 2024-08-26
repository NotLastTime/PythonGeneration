import tkinter as tk
from windows.windows_settings import *
from windows.choice_window import create_choice_window

def open_window_choise(main):
    create_choice_window(main)
    main.withdraw()

# Создание и настройка основного окна
main = tk.Tk()
window_settings(main, 500, 500)
main.title('PYTHON GENERATION')

# Создание и размещение виджетов
frame = tk.Frame(main)
frame.place(relx=0.5, rely=0.5, anchor='center')

label = tk.Label(frame, text='Приветствую тебя, дошедший до финала!', font=('Montserrat', 15))
label.pack(pady=30)

button_start = button_settings(frame, text='Начать', command=lambda: open_window_choise(main))
button_start.pack(pady=5)

# Запуск основного цикла
main.mainloop()


