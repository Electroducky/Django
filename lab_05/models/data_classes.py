class Address:
    def __init__(self, city, street, code):
        self.city = city
        self.street = street
        self.postalCode = code


class University:
    def __init__(self, name, id, head, address, units):
        self.name = name
        self.id = id
        self.head = head
        self.address = address
        self.units = units


class Person:
    def __init__(self, name, surname, patronymic, id):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.id = id


class Student(Person):
    def __init__(self, name, surname, patronymic, id, scholarship):
        super().__init__(name, surname, patronymic, id)
        self.scholarship = scholarship


class Employee(Person):
    def __init__(self, name, surname, patronymic, id, position):
        super().__init__(name, surname, patronymic, id)
        self.position = position


class Head(Employee):
    def __init__(self, name, surname, patronymic, id, position):
        super().__init__(name, surname, patronymic, id, position)


class Administrative():
    def __init__(self, rectorate, bookkeeping):
        self.rectorate = rectorate
        self.bookkeeping = bookkeeping


class Scientific_Educational():
    def __init__(self, megaFaculties):
        self.megaFaculties = megaFaculties


class Unit:
    def __init__(self, name, id, head, employees):
        self.name = name
        self.id = id
        self.head = head
        self.employees = employees


class MegaFaculty(Unit):
    def __init__(self, name, id, head, employees, faculties):
        super().__init__(name, id, head, employees)
        self.faculties = faculties


class Faculty(Unit):
    def __init__(self, name, id, head, employees, chairs):
        super().__init__(name, id, head, employees)
        self.chairs = chairs


class Chair(Unit):
    def __init__(self, name, id, head, employees, eduPrograms):
        super().__init__(name, id, head, employees)
        self.eduPrograms = eduPrograms


class EduProgram:
    def __init__(self, name, studyYear):
        self.name = name
        self.studyYear = studyYear


class StudyYear:
    def __init__(self, year, groups):
        self.year = year
        self.groups = groups


class Group:
    def __init__(self, name, students):
        self.name = name
        self.students = students
