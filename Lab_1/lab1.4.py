import random


# Задача №4: Работа со списками
def main():
    # Генерируем список из 10 случайных чисел
    numbers = [random.randint(1, 100) for _ in range(10)]

    # Выводим исходный список
    print("Исходный список:", numbers)

    # Максимальное и минимальное значение в списке
    max_value = max(numbers)
    min_value = min(numbers)
    print(f"Максимальное значение: {max_value}, Минимальное значение: {min_value}")

    # Сумма всех элементов списка
    total_sum = sum(numbers)
    print(f"Сумма всех элементов: {total_sum}")

    # Сортируем список по возрастанию
    sorted_numbers = sorted(numbers)
    print("Отсортированный список:", sorted_numbers)


if __name__ == "__main__":
    main()