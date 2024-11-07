class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Student(Person):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = []
        self.courses_in_progress = []
        self.finished_courses = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_average_grade(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка: {self.get_average_grade():.1f}\n"
                f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
                f"Завершенные курсы: {', '.join(self.finished_courses)}")

    def __lt__(self, other):
        return self.get_average_grade() < other.get_average_grade()


class Reviewer(Person):
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


class Lecturer(Person):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_average_grade(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка: {self.get_average_grade():.1f}")

    def __lt__(self, other):
        return self.get_average_grade() < other.get_average_grade()


student1 = Student("Иван", "Иванов")
student1.courses_in_progress = ["Python", "Git"]
student1.finished_courses = ["Введение в программирование"]
student1.add_grade(8)
student1.add_grade(9)
lecturer1 = Lecturer("Петр", "Петров")
lecturer1.add_grade(9)
lecturer1.add_grade(10)
reviewer = Reviewer("Алексей", "Алексеев")

print(student1)
print(lecturer1)
print(reviewer)

student2 = Student("Анна", "Петрова")
student2.add_grade(9)
print(student1 < student2)