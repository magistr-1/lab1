# Файл: main.py

import math_operations as mo

try:
    print(f"Сложение: {mo.add(10, 5)}")  # Должно вывести 15
    print(f"Вычитание: {mo.subtract(10, 5)}")  # Должно вывести 5
    print(f"Умножение: {mo.multiply(10, 5)}")  # Должно вывести 50
    print(f"Деление: {mo.divide(10, 5)}")  # Должно вывести 2.0

    # Проверка обработки исключения при делении на ноль
    result = mo.divide(10, 0)
except ValueError as e:
    print(e)  # Должно вывести сообщение о невозможности деления на ноль