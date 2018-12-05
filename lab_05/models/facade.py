import json
from tinydb import TinyDB

db = TinyDB('lab_05\models\db.json')
db.purge_tables()

def to_json(obj):
    return json.loads(json.dumps(obj, default=lambda o: o.__dict__))

def add(table, obj):
     return db.table(table).insert(to_json(obj))
