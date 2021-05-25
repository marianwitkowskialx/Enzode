
# Klasa przechowujaca informacje o pracownika
from pydantic import BaseModel, Field, validator, ValidationError
from typing import List, Optional
from datetime import datetime

class Employee(BaseModel):
    id : Optional[int] = -1
    fname : str = Field(None, min_length=2, max_length=100)
    lname : str = Field(None, min_length=2, max_length=100)
    pesel: str = ""
    manager: bool = False
    acl: List[int] = []
    create_ts : Optional[datetime] = datetime.now()

    @validator("pesel")
    def validate_pesel(cls, s:str):
        if len(s)==11 and s.isdigit():
            return s
        raise ValidationError("Podaj poprawny PESEL")