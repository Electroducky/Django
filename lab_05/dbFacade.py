import json
from tinydb import TinyDB
from tinydb import where

# print(db.table("students").get(doc_id=studentId))


db = TinyDB('lab_05\models\db.json')


def getValue(data, table, key, id=1):
    d = data.table(table).search(where(key))
    return d[key]


def getUniversityInfo():
    university = {}
    university["name"] = getValue(db, "university", "name")
    university["adress"] = db.table("address").get(doc_id=1)
    university["head"] = db.table("head").get(doc_id=1)
    university["len_administrative"] = len(db.table("administrative"))
    university["len_scientific_educational"] = len(db.table("scientific_educational"))
    university["len_megaFaculties"] = len(db.table("megaFaculties"))
    university["len_faculties"] = len(db.table("faculties"))
    university["len_chairs"] = len(db.table("chairs"))

    return university

    # def getGroupsInfo():
    #
    #
    # def getDepartmentInfo():
    #
    #
    # def getDisciplineInfo():
