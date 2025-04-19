# Задача №3: Цикл while
def main():
    # Запрашиваем число n
    n = int(input("Введите целое положительное число n: "))

    # Выводим числа от n до 1 в обратном порядке
    print("Числа от n до 1 в обратном порядке:")
    current_number = n
    while current_number >= 1:
        print(current_number, end=" ")
        current_number -= 1
    print()

    # Вычисляем факториал числа n
    factorial = 1
    temp_n = n
    while temp_n > 0:
        factorial *= temp_n
        temp_n -= 1
    print(f"Факториал числа {n}: {factorial}")


if __name__ == "__main__":
    main()