# task4.py
import re


def extract_data(file_name='text.txt'):
    emails_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    phone_pattern = r'\+7-\d{3}-\d{3}-\d{2}-\d{2}'
    capital_word_pattern = r'\b[A-Z][a-z]*\b'

    try:
        with open(file_name, 'r') as file:
            content = file.read()

        # Извлекаем данные
        emails = re.findall(emails_pattern, content)
        phones = re.findall(phone_pattern, content)
        capital_words = re.findall(capital_word_pattern, content)

        # Записываем результаты в разные файлы
        write_to_file('emails.txt', '\n'.join(emails), 'Email адреса:')
        write_to_file('phones.txt', '\n'.join(phones), 'Номера телефонов:')
        write_to_file('capital_words.txt', '\n'.join(capital_words), 'Слова с большой буквы:')

    except FileNotFoundError:
        print(f"Ошибка: файл '{file_name}' не найден!")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


def write_to_file(filename, content, header=None):
    with open(filename, 'w') as file:
        if header:
            file.write(header + "\n")
        file.write(content)


extract_data()