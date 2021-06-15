
# Komunikacja z bazą mongoDB
from pymongo import MongoClient
from pymongo.database import Database, Collection

# Laczenie z MongoDB
client = MongoClient("18.156.117.57", 27017)

# Wybranie bazy danych
db : Database = client["mar_wit"]

if 'pracownik' in db.list_collection_names():
    db.drop_collection('pracownik')

coll : Collection = db["pracownik"]
coll.insert_one({
    "imie": "Jan", "nazwisko": "Kowalski", "wiek": 44
})
coll.insert_one({
    "imie": "Jan", "nazwisko": "Nowak", "kierownik" : True
})
coll.insert_many([
    {"nazwisko": "Kowalski", "nr_pracownika": 1234},
    {"nazwisko": "Ziutkowski", "nr_pracownika": 4567},
])


