# task1.py
def process_data(file_name='data.txt'):
    try:
        with open(file_name, 'r') as file:
            numbers = [float(line.strip()) for line in file.readlines()]

        # Вычисления
        total_sum = sum(numbers)
        avg = total_sum / len(numbers)
        maximum = max(numbers)
        minimum = min(numbers)

        # Форматируем результат
        results = f"""
Сумма: {total_sum}
Среднее: {avg}
Максимум: {maximum}
Минимум: {minimum}
"""

        # Запись результата в файл
        with open('result.txt', 'w') as output_file:
            output_file.write(results)

        print("Результат успешно записан в файл result.txt")

    except FileNotFoundError:
        print(f"Ошибка: файл '{file_name}' не найден!")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


process_data()