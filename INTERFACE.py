import tkinter as tk
import subprocess  # Модуль для запуска внешних приложений

# Функция для запуска игры "Угадай число"
# Функция для запуска игры "Угадай число"
def run_number_game():
    subprocess.Popen(["python", "my_guessthe_number.py"])  # Новый путь к файлу

# Функция для запуска игры "21 очко"
def run_blackjack_game():
    subprocess.Popen(["python", "black_jack.py"])  # Новый путь к файлу

# Функция для запуска игры "Крестики-нолики"
def run_tictac_game():
    subprocess.Popen(["python", "ttt_game.py"])  # Новый путь к файлу

# Создание окна
root = tk.Tk()
root.title("Выбор игры")

# Размеры окна
window_width = 300
window_height = 200
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)
root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

# Кнопка для запуска игры "Угадай число"
btn_number_game = tk.Button(
    root,
    text="Угадай число",
    font=("Arial", 16),
    command=run_number_game
)
btn_number_game.pack(fill="both", expand=True, padx=10, pady=(10, 5))

# Кнопка для запуска игры "21 очко"
btn_blackjack_game = tk.Button(
    root,
    text="21 очко",
    font=("Arial", 16),
    command=run_blackjack_game
)
btn_blackjack_game.pack(fill="both", expand=True, padx=10, pady=(5, 10))

# Кнопка для запуска игры "Крестики-нолики"
btn_tictac_game = tk.Button(
    root,
    text="Крестики-нолики",
    font=("Arial", 16),
    command=run_tictac_game
)
btn_tictac_game.pack(fill="both", expand=True, padx=10, pady=(5, 10))

# Запускаем окно
root.mainloop()