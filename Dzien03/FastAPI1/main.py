
# Plik główny dla Fast API
from fastapi import FastAPI, Response, Request, Query, Path, HTTPException, status
from typing import List, Optional
import uvicorn
from employee import Employee

app = FastAPI()

# tworzenie wsadowych danych
employees : List[Employee] = []

e1 = Employee(id=1, fname="Jan", lname="Kowalski",
              pesel="12345678901", manager=True, acl=[101,102,103])
employees.append(e1)

e2 = Employee(id=2, fname="Janina", lname="Nowak",
              pesel="98765678901",  acl=[102])
employees.append(e2)

@app.get("/")
async def main():
    return {"message":"OK"}

@app.get("/items", response_model=List[Employee])
async def get_list():
    return employees

#@app.get("/item/{emp_id}", response_model=Employee,
#         response_model_exclude={'create_ts'})
@app.get("/item/{emp_id}", status_code=status.HTTP_200_OK)
async def get_employee(emp_id : int, response: Response, verbose: int=0):
    emp = list(filter(lambda x: x.id==emp_id, employees))
    if len(emp):
        if verbose:
            return emp[0]
        else:
            return emp[0].dict(exclude={'create_ts'})
    #response.status_code = status.HTTP_404_NOT_FOUND
    #return {"message":"record not found"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="record not found")

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
