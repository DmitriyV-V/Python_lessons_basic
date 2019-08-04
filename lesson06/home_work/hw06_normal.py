# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе


class School:
    def __init__(self, school, students, teachers):
        self.school = school
        self.students = students
        self.teachers = teachers

    def get_all_classes(self):
        classes = set([student.get_class_num for student in self.students])
        return list(sorted(classes, key=lambda x: int(x[:-1])))

    def get_students(self, class_num):
        return [student.get_short_name for student in self.students if class_num == student.get_class_num]

    def get_teachers(self, class_num):
        return [teacher.get_short_name for teacher in self.teachers if class_num in teacher.get_classes]

    def find_student(self, student_full_name):
        for person in self.students:
            if str(student_full_name) == person.get_full_name:
                teachers = [teachers.get_short_name for teachers in self.teachers if person.get_class_num in
                            teachers.get_classes]
                lessons = [teachers.get_subjects for teachers in self.teachers if person.get_class_num in
                           teachers.get_classes]
                parents = person.get_parents

                return {'full_name': student_full_name, 'class_room': person.get_class_num,
                        'teachers': teachers, 'lessons': lessons, 'parents': parents}

    @property
    def name(self):
        return f'Название школы: {self.school}'


class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @property
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    @property
    def get_short_name(self):
        return self.name + ' ' + self.surname[0] + '.'


class Student(Person):
    def __init__(self, name, surname, class_num, mother, father):
        Person.__init__(self, name, surname)
        self.class_num = class_num
        self.parents = {
            'mother': mother,
            'father': father
            }

    @property
    def get_class_num(self):
        return self.class_num

    @property
    def get_parents(self):
        return self.parents


class Teacher(Person):
    def __init__(self, name, surname, classes, subject):
        Person.__init__(self, name, surname)
        self.classes = classes
        self.subject = subject

    @property
    def get_subjects(self):
        return self.subject

    @property
    def get_classes(self):
        return self.classes


students = [Student("Ванька", "Быстров", "5А", "Батька Быстров", "Мамка Быстрова"),
            Student("Петька", "Тормозов", "6Б", "Батька Тормозов", "Мамка Тормозова"),
            Student("Лешка", "Отставашкин", "7В", "Батька Отставашкин", "Мамка Отставашкина"),
            Student("Ленка", "Умникова", "5А", "Батька Умников", "Мамка Умникова"),
            Student("Катька", "Пряник", "5А", "Батька Пряник", "Мамка Пряник"),
            Student("Лизка", "Спашкина", "10И", "Батька Спашкин", "Мамка Спашкина")]

teachers = [Teacher("Инокентий", "Шматкович", ["5А", "6Б"], "информатика"),
            Teacher("Евлампий", "Дудишкин", ["7В", "10И"], "информатика")]

school = School('Школа 1', students, teachers)

print(school.name)


# 1. Получить полный список всех классов школы
print('\n1. Все классы школы:')
print(', '.join(school.get_all_classes()))

# 2. Получить список всех учеников в указанном классе
print('\n2. Все ученики класса 5А:')
print(', '.join(school.get_students("5А")))

# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
student_1 = school.find_student("Ванька Быстров")
print('\n3.\nУченик: {0}\nКласс: "{1}"\n''Учитель: {2}\nУрок: {3}'
      .format(student_1['full_name'], student_1['class_room'], ', '.join(student_1['teachers']),
              ', '.join(student_1['lessons'])))

# 4. Узнать ФИО родителей указанного ученика
print('\n4. Родители: {0}, {1}'.format(student_1['parents']['mother'], student_1['parents']['father']))

# 5. Получить список всех Учителей, преподающих в указанном классе
print('\n5.\nКласс: "5А"\nУчитель: ''{0}'.format(', '.join(school.get_teachers('5А'))))
