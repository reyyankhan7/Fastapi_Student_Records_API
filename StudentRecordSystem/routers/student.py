from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from .. import crud, schemas, database

router = APIRouter()
security = HTTPBearer()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.StudentOut)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db), token: HTTPAuthorizationCredentials = Depends(security)):
    return crud.create_student(db, student)

@router.get("/", response_model=list[schemas.StudentOut])
def get_students(db: Session = Depends(get_db), token: HTTPAuthorizationCredentials = Depends(security)):
    return crud.get_students(db)

@router.get("/search/{name}", response_model=schemas.StudentOut)
def search_student(name: str, db: Session = Depends(get_db), token: HTTPAuthorizationCredentials = Depends(security)):
    return crud.get_student_by_name(db, name)

@router.put("/{student_id}", response_model=schemas.StudentOut)
def update_student(student_id: int, update_data: schemas.StudentUpdate, db: Session = Depends(get_db), token: HTTPAuthorizationCredentials = Depends(security)):
    return crud.update_student(db, student_id, update_data)
