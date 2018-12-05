import random
import string
import json

from lab_05.models import facade
from lab_05.models.data_classes import University, Address, Student, Group, Employee, Person, EduProgram, StudyYear, \
    Chair, Faculty, \
    Unit, Administrative, Scientific_Educational


import codecs

names = json.load(codecs.open('dataset/names.json', 'r', 'utf-8-sig'))

surnames = json.load(codecs.open('dataset/surnames.json', 'r', 'utf-8-sig'))

patronymics = json.load(codecs.open('dataset/patronymics.json', 'r', 'utf-8-sig'))


# def to_json(any):
#     return json.loads(json.dumps(any, default=lambda o: o.__dict__))
#
#
# db = TinyDB('db.json')
# db.purge_tables()
#
# db.table("university").insert(to_json(University("itmo", Address("aaa", 56))))
#
# db.table("students").insert(to_json(Student('petya', 'vasechkin', 10, 1000)))
# db.table("students").insert(to_json(Student('sarra', 'konnor', 50, 2000)))
# db.table("students").insert(to_json(Student('ramsan', 'xabib', 52, 0)))
#
# db.table("prepods").insert(to_json(Employee('petr', 'vasechkov', 10, 'director')))
# db.table("prepods").insert(to_json(Employee('aaa', 'bbb', 50, 'prosto prepod')))
# db.table("prepods").insert(to_json(Employee('ggg', 'ccc', 52, 'prepod pokruche')))
#
# db.table("group").insert(to_json(Group("23531/4", [1, 2])))

# for result in db.table("group").search(where('name') == '23531/4'):
#     for studentId in result['students']:
#         print(db.table("students").get(doc_id=studentId))


def generate_person_name():
    return names[random.randint(0, len(names) - 1)]["Name"]


def generate_surname():
    return surnames[random.randint(0, len(surnames) - 1)]["Surname"]


def generate_patronymic():
    return patronymics[random.randint(0, len(patronymics) - 1)]["patronymic"]


def generate_name(name):
    return name + str(random.randint(1, 200))


def generate_group_name():
    return random.choice(string.ascii_lowercase) + str(random.randint(1, 9999))


def generate_id():
    return random.randint(1, 9999)


def generate_list(n):
    return list((map(str, range(1, n))))


def create_id_list(function):
        return [function(), function(), function()]


def add_student():
    return facade.add("students",
                      Student(generate_person_name(), generate_surname(), generate_patronymic(), generate_id(), 1600))


def add_teacher():
    return facade.add("teachers",
                      Person(generate_person_name(), generate_surname(), generate_patronymic(), generate_id()))


def add_employee():
    return facade.add("employees",
                      Employee(generate_person_name(), generate_surname(), generate_patronymic(), generate_id(),
                               "сотрудник"))


def add_head():
    return facade.add("heads",
                      Employee(generate_person_name(), generate_surname(), generate_patronymic(), generate_id(),
                               "руководитель"))


def add_group():
    return facade.add("groups", Group(generate_group_name(), create_id_list(lambda: add_student())))


def add_studyYear():
    return facade.add("studyYear", StudyYear("2018/2019", create_id_list(lambda: add_group())))


def add_eduProgram():
    return facade.add("eduPrograms",
                      EduProgram(generate_name("Образовательная программа"), add_studyYear()))


def add_chair():
    return facade.add("chairs",
                      Chair(generate_name("Кафедра"), generate_id(), add_head(),
                            create_id_list(lambda: add_teacher()), create_id_list(lambda: add_eduProgram())))


def add_faculty():
    return facade.add("faculties",
                      Faculty(generate_name("Факультет"), generate_id(), add_head(),
                              create_id_list(lambda: add_employee()), create_id_list(lambda: add_chair())))


def add_megaFaculty():
    return facade.add("megaFaculties",
                      Faculty(generate_name("мегафакультет"), generate_id(), add_head(),
                              create_id_list(lambda: add_employee()), create_id_list(lambda: add_faculty())))


def add_address():
    return facade.add("address", Address("Санкт-Петербург", "Кроверский проспект 49", "197101"))


def add_unit(name):
    return facade.add(name, Unit(name, generate_id(), create_id_list(lambda: add_employee()), add_head()))


def add_administrative():
    return facade.add("administrative", Administrative(add_unit("ректорат"), add_unit("бухгалтерия")))


def add_scientific_educational():
    return facade.add("scientific_educational", Scientific_Educational(create_id_list(lambda: add_megaFaculty())))


def add_university():
    facade.add("university",
                      University("ИТМО", generate_id(), add_head(), add_address(),
                                 [add_administrative(), add_scientific_educational()]))
#add_scientific_educational()

add_university()
