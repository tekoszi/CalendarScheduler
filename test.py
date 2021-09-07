import os, json

filename = 'db.json'

def loadDB():
    with open(filename, mode='r') as json_file:
        db = json.load(json_file)
        return db


def witeDB(db):
    with open(filename, mode='w') as json_file:
        json.dump(db, json_file)


db = loadDB()

for idx, (key, value) in enumerate(db['people'].items()):
    db['people'][key] = {"SL":None, "calendars":{"8":["w" for x in range(32)],"9":["w" for x in range(32)] }, "name": "Full name "+str(idx+1)}

print(db)
witeDB(db)