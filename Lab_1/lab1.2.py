# Задача №2: Цикл for
def main():
    # Запрашиваем число n
    n = int(input("Введите целое положительное число n: "))

    # Выводим числа от 1 до n
    print("Числа от 1 до n:")
    for i in range(1, n + 1):
        print(i, end=" ")
    print()  # Для перехода на новую строку

    # Выводим квадраты чисел от 1 до n
    print("Квадраты чисел от 1 до n:")
    for i in range(1, n + 1):
        print(i * i, end=" ")
    print()

    # Сумма чисел от 1 до n
    total_sum = sum(range(1, n + 1))
    print(f"Сумма чисел от 1 до n равна: {total_sum}")


if __name__ == "__main__":
    main()