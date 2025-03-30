class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        
    def __str__(self):
        return f'Student: {self.name} {self.surname}, Gender: {self.gender}, Grades: {self.grades}'

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
    
    def __str__(self):
        return f'Mentor: {self.name} {self.surname}, Courses attached: {self.courses_attached}'

def average_homework_grade(students, course):
    total_grades = 0
    total_students = 0
    for student in students:
        if course in student.grades:
            total_grades += sum(student.grades[course])
            total_students += len(student.grades[course])
    return total_grades / total_students if total_students > 0 else 0

def average_lecture_grade(mentors, course):
    total_grades = 0
    total_mentors = 0
    for mentor in mentors:
        if course in mentor.courses_attached:
            total_mentors += 1
    return total_grades / total_mentors if total_mentors > 0 else 0

student1 = Student('Ruoy', 'Eman', 'your_gender')
student1.courses_in_progress.append('Python')

student2 = Student('John', 'Doe', 'male')
student2.courses_in_progress.append('Python')

mentor1 = Mentor('Some', 'Buddy')
mentor1.courses_attached.append('Python')

mentor2 = Mentor('Jane', 'Smith')
mentor2.courses_attached.append('Python')

mentor1.rate_hw(student1, 'Python', 10)
mentor1.rate_hw(student1, 'Python', 9)
mentor1.rate_hw(student2, 'Python', 8)

mentor2.rate_hw(student1, 'Python', 7)
mentor2.rate_hw(student2, 'Python', 6)


print(student1)
print(student2)
students = [student1, student2]

average_grade = average_homework_grade(students, 'Python')
print(f'Average homework grade for Python: {average_grade}')

mentors = [mentor1, mentor2]
average_lecture_grade_value = average_lecture_grade(mentors, 'Python')
print(f'Average lecture grade for Python: {average_lecture_grade_value}')