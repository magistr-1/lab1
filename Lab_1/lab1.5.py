import random


# Дополнительная задача №5: Работа со списком
def main():
    # Генерируем список из 20 случайных чисел от 1 до 100
    numbers = [random.randint(1, 100) for _ in range(20)]

    # Чётные числа
    even_numbers = [num for num in numbers if num % 2 == 0]
    print("Четные числа:", even_numbers)

    # Числа, делящиеся на 3
    divisible_by_3 = [num for num in numbers if num % 3 == 0]
    print("Делимые на 3:", divisible_by_3)

    # Среднее арифметическое всех чисел
    average = sum(numbers) / len(numbers)
    print(f"Среднее арифметическое: {average:.2f}")


if __name__ == "__main__":
    main()