# task5.py
numbers = list(range(1, 21))

# Используем lambda-функции и map/filter/sorted
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))       # Оставляем только чётные числа
increased_numbers = list(map(lambda x: x + 10, numbers))        # Добавляем к каждому элементу 10
sorted_descending = sorted(numbers, reverse=True)                # Сортируем по убыванию

print("Список четных чисел:", even_numbers)
print("Список увеличенный на 10:", increased_numbers)
print("Отсортированный по убыванию:", sorted_descending)