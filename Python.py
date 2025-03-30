class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = []

    def average_grade(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        return 0

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        super().rate_hw(student, course, grade)

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

print(best_student.grades)

lecturer = Lecturer('John', 'Doe')
lecturer.courses_attached += ['Python']
lecturer.grades += [9, 10, 8]

reviewer = Reviewer('Jane', 'Smith')
reviewer.courses_attached += ['Python']
reviewer.rate_hw(best_student, 'Python', 9)

print(f'Average grade of lecturer {lecturer.name} {lecturer.surname}: {lecturer.average_grade()}')
print(best_student.grades)