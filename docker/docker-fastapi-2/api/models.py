
from sqlalchemy import Column, Integer, String, Boolean, Date, DateTime
from database import Base
from datetime import datetime


class EmployeeModel(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    fname = Column(String(255), index=True)
    lname = Column(String(255), index=True)
    pesel = Column(String(11))
    manager = Column(Integer)

    _acl = Column(String, default='')

    @property
    def acl(self):
        return [int(x) for x in self._acl.split(';')]

    @acl.setter
    def acl(self, value):
        self._acl = ";".join([str(x) for x in value])

    create_ts = Column(DateTime, default=datetime.now())