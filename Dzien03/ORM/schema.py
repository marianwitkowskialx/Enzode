
# Definicja obiektów bazodanowych
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from db import Base

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(String(255), unique=True )
    password = Column(String(255))
    name = Column(String(100), index=True)

    def __repr__(self):
        return f"User:{self.id} {self.login} {self.password} {self.name}|"
