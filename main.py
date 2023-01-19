class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress or course in self.finished_courses:
            if grade > 0 and grade <= 10:
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
                else:
                    lecturer.grades[course] = [grade]
            else:
                print('Оценка не может быть меньше 1 или больше 10')
                return
        else:
            return 'Ошибка'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []



class Lecturer(Mentor):
    def __init__(self, name, surname):
      super().__init__(name, surname)
      self.grades = {}


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

# для проверки
Ivan_Ivanov = Student('Ivan', 'Ivanov', 'Male')
Petr_Petrov = Lecturer('Petr', 'Petrov')

Petr_Petrov.courses_attached.append('math')
Ivan_Ivanov.courses_in_progress.append('math')

Ivan_Ivanov.rate_lect(Petr_Petrov, 'math', 1)

print(Petr_Petrov.grades)