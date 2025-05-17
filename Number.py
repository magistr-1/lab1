import random
from datetime import datetime

def save_game_stats(guesses, result, time_taken):
    with open('game_statistics.txt', 'a') as file:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        file.write(f'{timestamp}: Число попыток - {guesses}, Результат - {"Успех" if result else "Неудача"}, Время игры - {time_taken:.2f} секунд\n')

def play_game():
    number_to_guess = random.randint(1, 100)
    guesses = 0
    start_time = datetime.now()

    while True:
        try:
            guess = int(input("Угадайте число от 1 до 100: "))
            guesses += 1

            if guess < number_to_guess:
                print("Загаданное число больше.")
            elif guess > number_to_guess:
                print("Загаданное число меньше.")
            else:
                end_time = datetime.now()
                time_taken = (end_time - start_time).total_seconds()
                print(f"Победа! Вы угадали число за {guesses} попытки(-ок)! Время игры: {time_taken:.2f} секунды.")
                save_game_stats(guesses, True, time_taken)
                break
        except ValueError:
            print("Ошибка ввода. Введите целое число.")

if __name__ == '__main__':
    play_game()