
# Konfiguracja na potrzeby połączenia z bazą danych
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = 'sqlite:///users1.db'

engine = create_engine(DATABASE_URL, echo=False, connect_args={
    'check_same_thread' : False
})

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()