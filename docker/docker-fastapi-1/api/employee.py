
from pydantic import BaseModel, Field, validator, ValidationError
from pydantic.types import constr
from typing import List, Tuple, Dict, Optional
from datetime import datetime


class Employee(BaseModel):
    id : Optional[int] = -1
    fname: str = Field(None, min_length=2, max_length=100)
    lname: str = Field(None, min_length=2, max_length=100)
    pesel: str = ""
    manager: bool = False
    acl: List[int] = []
    create_ts: Optional[datetime] = datetime.now()

    @validator("pesel")
    def pesel_validator(cls, v : str):
        if v.isdigit() and len(v)==11:
            return v
        raise ValueError("Podaj PESEL")