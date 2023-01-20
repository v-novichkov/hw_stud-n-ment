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

    def mid_grade(self):
        count_courses = 0
        count_grades = 0
        sum_grades = 0
        for k, v  in self.grades.items():
            if k is not None and v is not None:
                count_courses += 1
                count_grades += len(v)
                sum_grades += sum(v)
            else:
                print(f'У студента {self.name} нет закрепленных курсов или оценок')
        mid_grades = sum_grades / count_grades / count_courses
        return mid_grades

    def __str__(self):
        res = f' Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за дз: {self.mid_grade()} \nКурсы в процессе изучения: {self.courses_in_progress} \nЗавершенные курсы: {self.finished_courses}'
        return res

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []



class Lecturer(Mentor):
    def __init__(self, name, surname):
      super().__init__(name, surname)
      self.grades = {}


    def mid_grade(self):
        count_courses = 0
        count_grades = 0
        sum_grades = 0
        for k, v  in self.grades.items():
            if k is not None and v is not None:
                count_courses += 1
                count_grades += len(v)
                sum_grades += sum(v)
            else:
                print(f'У лектора {self.name} нет закрепленных курсов или оценок')
        mid_grades = sum_grades / count_grades / count_courses
        return mid_grades

    def __str__(self):
        res = f' Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.mid_grade()}'
        return res

class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f' Имя: {self.name} \n Фамилия: {self.surname}'
        return res

# для проверки
Ivan_Ivanov = Student('Ivan', 'Ivanov', 'Male')
Petr_Petrov = Lecturer('Petr', 'Petrov')
Petr_Petrovs = Reviewer('Petr', 'Petrovs')

Petr_Petrovs.courses_attached.append('math')
Ivan_Ivanov.courses_in_progress.append('math')
Ivan_Ivanov.courses_in_progress.append('info')
Petr_Petrovs.courses_attached.append('info')
Petr_Petrovs.rate_hw(Ivan_Ivanov, 'math', 8)
Petr_Petrovs.rate_hw(Ivan_Ivanov, 'info', 8)

Petr_Petrov.courses_attached.append('math')

Petr_Petrov.courses_attached.append('info')

Ivan_Ivanov.finished_courses.append('python')
#
Ivan_Ivanov.rate_lect(Petr_Petrov, 'math', 1)
Ivan_Ivanov.rate_lect(Petr_Petrov, 'math', 3)
Ivan_Ivanov.rate_lect(Petr_Petrov, 'info', 8)
Ivan_Ivanov.rate_lect(Petr_Petrov, 'info', 1)

print(Ivan_Ivanov.grades)
print(Ivan_Ivanov)
