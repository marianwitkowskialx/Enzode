from fastapi import FastAPI, Response, status, \
    Query, Path, Request, HTTPException
from fastapi.responses import HTMLResponse, StreamingResponse
import uvicorn
from typing import List, Optional
from employee import Employee
from datetime import datetime
import time


app = FastAPI()

employees: List[Employee] = []

emp = Employee(id=1, fname="Jan", lname="Kowalski", pesel="80121212345", manager=False, acl=[101, 102, 103])
employees.append(emp)

emp = Employee(id=2, fname="Elvis", lname="Presley", pesel="80121212346", manager=True, acl=[101, 102, 103])
employees.append(emp)

@app.on_event("startup")
async def startup():
    print("starting...")

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

@app.get("/img")
def read_image():
    file_like = open("cat.png", mode="rb")
    return StreamingResponse(file_like, media_type="image/png")


@app.get("/html")
async def read_items():
    html_content = """
    <html>
        <body>
            <h1>ENZODE</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)


@app.get("/request")
async def get_request(r : Request):
    return { "headers" : r.headers,
             "cookies" : r.cookies,
             "method" : r.method,
             "client" : r.client}

@app.get("/")
async def main():
    return {"message": "OK"}


@app.get("/items", response_model=List[Employee])
async def get_list():
    return employees


@app.get("/item/{emp_id}", status_code=status.HTTP_200_OK, response_model_exclude={'create_ts'})
async def get_employee(emp_id: int, response: Response, debug: int=0):
    emp = list(filter(lambda x: x.id == emp_id, employees))
    if len(emp):
        if debug:
            return emp[0]
        else:
            return emp[0]#.dict(exclude={'create_ts'})
    response.status_code = status.HTTP_404_NOT_FOUND
    #return {"message" : "Not found"}
    raise HTTPException(status_code=404, detail="not found")

@app.post("/item", status_code=status.HTTP_201_CREATED)
async def add_employee(emp: Employee, response : Response):
    """
        Create an item with all the information:

        - **name**: each item must have a name
        - **description**: a long description
        - **price**: required
        - **tax**: if the item doesn't have tax, you can omit this
        - **tags**: a set of unique tag strings for this item
    """
    obj = max(employees, key=lambda p: p.id)
    if obj:
        emp.id = obj.id + 1
        emp.create_ts = datetime.now()
        employees.append(emp)
        return { "message" : "OK"}
    else:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return { "message" : "ERROR"}

@app.get("/find", description="Wyszukiwanie pracownika")
async def find_employee(response: Response, q: Optional[str] = Query(None,
                                                 title="Nazwisko",
                                                 alias="query",
                                                 description="Podaj poszukiwaną frazę",
                                                 min_length=3, max_length=50)):
    emp = list(filter(lambda x: q.upper() in x.lname.upper(), employees))
    if len(emp):
        return emp[0].dict(exclude={'create_ts'})
    response.status_code = status.HTTP_404_NOT_FOUND
    return {"message": "Not found"}


@app.get("/findemp/{phrase}", description="Wyszukiwanie pracownika v2")
async def findemp(response: Response, phrase : str = Path(..., min_length=3)):
    emp = list(filter(lambda x: phrase.upper() in x.lname.upper(), employees))
    if len(emp):
        return emp[0].dict(exclude={'create_ts'})
    response.status_code = status.HTTP_404_NOT_FOUND
    return {"message": "Not found"}

@app.put("/item/{emp_id}", description="Aktualizacja danych")
async def update_emp(emp_id: int, data: Employee, response : Response):
    emp = list(filter(lambda x: x.id == emp_id, employees))
    if len(emp):
        emp[0].fname = data.fname
        emp[0].lname = data.lname
        return {"message": "OK"}
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": "Not found"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
