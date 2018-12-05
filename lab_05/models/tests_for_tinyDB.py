import json
import dataset as dataset
import random
import random
import string
from tinydb import TinyDB, Query, where
from lab_05.models.data_classes import University, Address, Student, Group


def to_json(any):
    return json.loads(json.dumps(any, default=lambda o: o.__dict__))


db = TinyDB('test_db.json')
db.purge_tables()

db.table("university").insert({"name": "ITMO"})
University = Query()
print(len(db.table("university")))
print(db.table("university").search(where("name")))
