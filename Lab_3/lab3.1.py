class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []

    def add_grade(self, grade):
        if not isinstance(grade, int) or grade < 0 or grade > 10:
            raise ValueError("Оценка должна быть целым числом от 0 до 10")
        self.grades.append(grade)

    def get_average(self):
        return sum(self.grades) / len(self.grades) if self.grades else None

    def display_info(self):
        avg = self.get_average()
        print(f'Имя студента: {self.name}')
        print(f'ID студента: {self.student_id}')
        print(f'Средняя оценка: {"%.2f" % avg}' if avg is not None else 'Нет оценок')