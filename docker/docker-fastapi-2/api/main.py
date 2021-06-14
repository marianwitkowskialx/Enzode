from fastapi import FastAPI, Response, status, \
    Query, Path, Request, HTTPException, Depends
from fastapi.responses import HTMLResponse, StreamingResponse, RedirectResponse, JSONResponse
import uvicorn
from typing import List, Optional
from employee import Employee
from models import Base, EmployeeModel
from database import SessionLocal, engine
from datetime import datetime
import time
from sqlalchemy.orm import Session


Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


employees: List[Employee] = []

@app.on_event("startup")
async def startup():
    print("starting...")


@app.on_event("shutdown")
async def shutdown():
    print("shutdown...")


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
    return RedirectResponse(url="/docs/")


@app.get("/items", response_model=List[Employee])
async def get_list(db: Session = Depends(get_db)):
    data = db.query(EmployeeModel).all()
    return data


@app.get("/item/{emp_id}", status_code=status.HTTP_200_OK, response_model=Employee)
async def get_employee(emp_id: int, response: Response, debug: int=0, db: Session = Depends(get_db)):
    item : EmployeeModel = db.query(EmployeeModel).where(EmployeeModel.id == emp_id).first()
    if item:
        if debug:
            return item
        else:
            delattr(item, "create_ts")
            return item
    raise HTTPException(status_code=404, detail="not found")

@app.post("/item", status_code=status.HTTP_201_CREATED)
async def add_employee(emp: Employee, response : Response, db: Session = Depends(get_db)):
    record = EmployeeModel(**emp.dict())
    db.add(record)
    db.commit()
    return { "id" : record.id }

@app.get("/find", description="Wyszukiwanie pracownika", response_model=List[Employee])
async def find_employee(response: Response, q: Optional[str] = Query(None,
                                                 title="Nazwisko",
                                                 alias="query",
                                                 description="Podaj poszukiwaną frazę",
                                                 min_length=3, max_length=50),
                        db: Session = Depends(get_db)):
    like_str = f"%{q}%"
    item : EmployeeModel = db.query(EmployeeModel).filter(EmployeeModel.lname.ilike(like_str)).all()
    if len(item):
        return item
    response.status_code = status.HTTP_404_NOT_FOUND
    return {"message": "Not found"}


@app.get("/findemp/{phrase}", description="Wyszukiwanie pracownika v2")
async def findemp(response: Response,
                  phrase : str = Path(..., min_length=3),
                  db: Session = Depends(get_db)):
    like_str = f"%{phrase}%"
    item : EmployeeModel = db.query(EmployeeModel).filter(EmployeeModel.lname.ilike(like_str)).all()
    if len(item):
        return item
    response.status_code = status.HTTP_404_NOT_FOUND
    return {"message": "Not found"}

@app.put("/item/{emp_id}", description="Aktualizacja danych")
async def update_emp(emp_id: int, data: Employee,
                     response : Response, db: Session = Depends(get_db)):

    db.query(EmployeeModel).where(EmployeeModel.id == emp_id).update({
        EmployeeModel.fname : data.fname,
        EmployeeModel.lname : data.lname,
    }, synchronize_session = False)
    db.commit()
    return {"message": "OK"}


@app.delete("/item/{emp_id}", description="Usuwanie danych")
async def delete_emp(emp_id: int,response : Response, db: Session = Depends(get_db)):
    r = db.query(EmployeeModel).where(EmployeeModel.id == emp_id).delete()
    db.commit()
    return {"message": r}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
