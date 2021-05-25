
# Plik główny dla Fast API
from fastapi import FastAPI, Response, Request, Query, Path, HTTPException, status
from typing import List, Optional
from fastapi.responses import HTMLResponse, StreamingResponse
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

@app.post("/item", status_code=status.HTTP_201_CREATED, description="Dodaje nowy rekord")
async def add_employee(emp: Employee, response : Response):
    """
        Funkcja dodająca nowy rekord

        - **emp**: rekord nowego pracownika
        - **response**: obiekt odpowiedzi z API
    """
    obj = max(employees, key=lambda x:x.id)
    if obj:
        emp.id = obj.id+1
    else:
        emp.id = 1
    employees.append(emp)
    return { "message" : "OK"}

@app.get("/find", description="Wyszukiwanie po nazwisku")
async def find_employee(response: Response,
                        q: Optional[str] = Query(None,
                                                 title="Nazwisko", alias="lname",
                                                 description="podaj nazwisko",
                                                 min_length=3, max_length=50)):
    emp = list(filter(lambda x: q.upper() in x.lname.upper(), employees))
    if len(emp):
        return emp[0]
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")

@app.patch("/item/{emp_id}", description="Aktualizacja rekordu")
async def patch_employee(emp_id:int, data: Employee, response: Response):
    emp = list(filter(lambda x: x.id == emp_id, employees))
    if len(emp):
        emp[0].fname = data.fname
        emp[0].lname = data.lname
        return {"message":"OK"}
    else:
        response.status_code = status.HTTP_418_IM_A_TEAPOT
        return {"message":"Not found"}

@app.get("/cat")
async def show_cat():
    fd = open("kot.jpg", mode="rb")
    return StreamingResponse(fd, media_type="image/jpeg")

@app.get("/html")
async def get_html():
    html_content = """
    <html>
    <body><h1>Hello world!</h1></body>
    </html>
    """
    return HTMLResponse(content=html_content)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
