# task2.py
def divide_numbers():
    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))

        # Деление
        result = num1 / num2
        print(f"Результат деления: {result}")

    except ZeroDivisionError:
        print("Ошибка: деление на ноль невозможно!")
    except ValueError:
        print("Ошибка: введены некорректные данные (нечисловое значение).")
    except Exception as e:
        print(f"Произошла неизвестная ошибка: {e}")


divide_numbers()