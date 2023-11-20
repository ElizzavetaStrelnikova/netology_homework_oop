# coding=utf-8
import math


class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _middle_grades_student(self):
        c_sum = 0
        c_count = 0
        all_courses = [self.finished_courses, self.courses_in_progress]
        for c in all_courses:
            c_sum += sum(self.grades[c[0]])
            c_count += len(self.grades[c[0]])
        result = round(c_sum / c_count, 2)
        return result

    def middle_grades_by_course(self, course):
        if course in self.grades.keys():
            return round(sum(self.grades[course]) / len(self.grades[course]), 2)
        else:
            return None

    def __str__(self):
        res = (f'\nСтудент\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: '
               f'{self._middle_grades_student()}\nКурсы в процессе '
               f'изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}')
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Это не студент!')
            return
        elif self._middle_grades_student() < other._middle_grades_student():
            return True
        else:
            return False

    def __eq__(self, other):
        if not isinstance(other, Student):
            print('Это не студент!')
            return
        elif self._middle_grades_student() == other._middle_grades_student():
            return True
        else:
            return False

    def __gt__(self, other):
        if not isinstance(other, Student):
            print('Это не студент!')
            return
        elif self._middle_grades_student() > other._middle_grades_student():
            return True
        else:
            return False

class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


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
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super(Lecturer, self).__init__(name, surname)
        self.grades = {}

    def _middle_grades_lecturer(self):
        c_sum = 0
        c_count = 0
        for c in self.courses_attached:
            c_sum += sum(self.grades[c])
            c_count += len(self.grades[c])
        result = round(c_sum / c_count, 2)
        return result
    
    def middle_grades_by_course(self, course):
        if course in self.grades.keys():
            return round(sum(self.grades[course]) / len(self.grades[course]), 2)
        else:
            return None

    def __str__(self):
        res = f'\nЛектор\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._middle_grades_lecturer()}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Это не лектор!')
            return
        elif self._middle_grades_lecturer() < other._middle_grades_lecturer():
            return True
        else:
            return False

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            print('Это не лектор!')
            return
        elif self._middle_grades_lecturer() == other._middle_grades_lecturer():
            return True
        else:
            return False

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            print('Это не лектор!')
            return
        elif self._middle_grades_lecturer() > other._middle_grades_lecturer():
            return True
        else:
            return False

def get_average_grade_by_course(person_list, course):
    """
    для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса
    (в качестве аргументов принимаем список студентов и название курса);
    :param person_list: список студентов
    :param course: название курса
    :return: средняя оценка
    """
    grade_list = []

    for person in person_list:
        avg_grade = person.middle_grades_by_course(course)
        if avg_grade:
            grade_list.append(person.middle_grades_by_course(course))

    return round(sum(grade_list) / len(grade_list), 2)

one_student = Student("Александр", "Стрельников", "мужской")
second_student = Student("Елизавета", "Стрельникова", "женский")
one_student.courses_in_progress += ['Python']
second_student.courses_in_progress += ['Java']
one_student.finished_courses += ['C++']
second_student.finished_courses += ['Python']
one_student.grades['Python'] = [4,5,4]
one_student.grades['C++'] = [3,5,5]
second_student.grades['Java'] = [4,4,4]
second_student.grades['Python'] = [4,5,5]

one_reviewer= Reviewer("Наталья", "Бочкарева")
second_reviewer= Reviewer("Борис", "Токарев")
one_reviewer.courses_attached += ['Python', 'Java', 'C++']
second_reviewer.courses_attached += ['Python', 'Java', 'C++']

one_lecturer= Lecturer("Сергей", "Трофимов")
second_lecturer= Lecturer("Зинаида", "Тютчева")
one_lecturer.courses_attached += ['Python', 'Java']
second_lecturer.courses_attached += ['C++']
one_lecturer.grades['Python'] = [5,5,5]
one_lecturer.grades['Java'] = [4,4,4]
second_lecturer.grades['C++'] = [5,4,5]

one_student.rate_lecturer(one_lecturer, 'Python', 5)
one_student._middle_grades_student()
is_smaller_student = one_student.__lt__(second_student)
is_equal_student = one_student.__eq__(second_student)
is_bigger_student = one_student.__gt__(second_student)


one_reviewer.rate_hw(one_student, 'Python', 5)

is_smaller_lecturer = one_lecturer.__lt__(second_lecturer)
is_equal_lecturer = one_lecturer.__eq__(second_lecturer)
is_bigger_lecturer = one_lecturer.__gt__(second_lecturer)

avg_grade_stud_python = get_average_grade_by_course([one_student, second_student], 'Python')
avg_grade_lec_python = get_average_grade_by_course([one_lecturer, second_lecturer], 'Python')

# print(one_lecturer.grades)
print(one_student)

print(is_smaller_student)
print(is_equal_student)
print(is_bigger_student)
# print(one_student.grades)

print(one_reviewer)

print(one_lecturer)

print(is_smaller_lecturer)
print(is_equal_lecturer)
print(is_bigger_lecturer)

print('средняя оценка студентов по питону:' + str(avg_grade_stud_python))
print('средняя оценка преподов по питону:' + str(avg_grade_lec_python))




