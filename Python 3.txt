class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        
    def average_grade(self):
        if self.grades:
            total_grades = sum(sum(grades) for grades in self.grades.values())
            total_courses = sum(len(grades) for grades in self.grades.values())
            return total_grades / total_courses
        return 0

    def __str__(self):
        avg_grade = self.average_grade()
        finished_courses = ', '.join(self.finished_courses) if self.finished_courses else 'Нет'
        courses_in_progress = ', '.join(self.courses_in_progress) if self.courses_in_progress else 'Нет'
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {avg_grade:.1f}\n'
                f'Курсы в процессе изучения: {courses_in_progress}\n'
                f'Завершенные курсы: {finished_courses}')

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.average_grade() < other.average_grade()
        return NotImplemented


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def average_grade(self):
        # Для примера, предположим, что у менторов нет оценок, но можно добавить логику
        return 0

    def __str__(self):
        avg_grade = self.average_grade()
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {avg_grade:.1f}')

    def __lt__(self, other):
        if isinstance(other, Mentor):
            return self.average_grade() < other.average_grade()
        return NotImplemented


# Пример использования
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

print(best_student)
print(cool_mentor)

# Сравнение студентов и менторов
another_student = Student('John', 'Doe', 'male')
another_student.courses_in_progress += ['Python']
cool_mentor.rate_hw(another_student, 'Python', 8)

print(best_student < another_student)  # True или False в зависимости от оценок