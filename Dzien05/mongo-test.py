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

res =coll.insert_one({
    "imie": "Jan", "nazwisko": "Kowalski", "wiek": 44
})
print(res.inserted_id)

coll.insert_one({
    "imie": "Jan", "nazwisko": "Nowak", "kierownik" : True
})

res = coll.insert_many([
    {"nazwisko": "Kowalski", "nr_pracownika": 1234},
    {"nazwisko": "Ziutkowski", "nr_pracownika": 4567},
])
print(res.inserted_ids)

# listowanie dok. z kolekcji
for doc in coll.find():
    print(doc)

# wyszukiwanie pojedynczego dokumentu
print("="*50)
doc = coll.find_one({"nr_pracownika" : 1234})
print(doc)

print("="*50)
docs = coll.find({"nazwisko" : "Kowalski"}, {"_id" : 0})
for doc in docs:
    print(doc)

# aktualizacja dokumentu
res = coll.update_many({"nr_pracownika" : 1234}, {"$set": {
    "wiek" : 50, "kierownik" : True, "nr_pracownika" : 9876
}})
print(res)




