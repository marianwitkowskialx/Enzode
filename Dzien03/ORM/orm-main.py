
from sqlalchemy.orm import Query
from db import Base, engine, session
from schema import User

Base.metadata.create_all(engine)

# usuwanie danych z tabeli
session.query(User).delete()
session.commit()

# dodaj dane do tablicy
user = User(login="jkowalski", password="qwerty1", name="Jan Kowalski")
session.add(user)
session.commit()

