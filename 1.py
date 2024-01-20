class Student:
    def __init__(self, name, age, group, literature_grades):
        self.name = name
        self.age = age
        self.group = group
        self.literature_grades = literature_grades

    def calculate_average_grade(self):
        total = sum(self.literature_grades)
        count = len(self.literature_grades)
        average_grade = total / count
        return round(average_grade, 2)

# Пример использования класса
student1 = Student("Иванов", 20, "Группа 123", [4, 5, 4, 3, 5])
average_grade = student1.calculate_average_grade()
print(f"Средняя оценка студента {student1.name} по литературе: {average_grade}")