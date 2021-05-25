
from sqlalchemy.orm import Query
from db import Base, engine, session
from schema import User
from sqlalchemy import text, desc

Base.metadata.create_all(engine)

# usuwanie danych z tabeli
session.query(User).delete()
session.commit()

# dodaj dane do tablicy
user1 = User(login="jkowalski", password="qwerty1", name="Jan Kowalski")
user2 = User(login="mnowak", password="qwerty1", name="Marek Nowak")
user3 = User(login="mjurek", password="qwerty1", name="Marek Jurek")
session.add(user1)
session.add(user2)
session.add(user3)
session.commit()

query : Query = session.query(User)

print(query.all()) # pokaż wszystkie rekordy

print(query.filter(User.id==1).scalar()) # pobranie na podstawie warunku
print(query.filter(User.id==1).first()) # pobranie na podstawie warunku
print(query.get(1)) # pobranie na podstawie warunku

print("="*60)
print(query.filter(User.login=="jkowalski").all())
print(query.filter_by(login="jkowalski").all())

print("="*60)
print(query.filter( User.id.in_([1,3]) ).all())

print("="*60)
print(query.filter( User.login.like('%wa%') ).all()) #szukamy na podstawie wzorca

print("="*60)
print( query.order_by(text("login desc")).all() ) # sortowanie
print( query.order_by( desc(User.login) ).all() )

print("="*60)
query.filter(User.id==1).delete() # usuwanie na podstawie warunku
session.commit()

print("="*60)
user : User = query.get(2)
user.password = "alamakota1"
session.commit()