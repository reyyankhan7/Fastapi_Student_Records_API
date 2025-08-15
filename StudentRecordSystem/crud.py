from sqlalchemy.orm import Session
from . import models, schemas
from passlib.hash import bcrypt

def create_student(db: Session, student: schemas.StudentCreate):
    db_student = models.Student(**student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def get_students(db: Session):
    return db.query(models.Student).all()

def get_student_by_name(db: Session, name: str):
    return db.query(models.Student).filter(models.Student.name == name).first()

def update_student(db: Session, student_id: int, update_data: schemas.StudentUpdate):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if student:
        for key, value in update_data.dict(exclude_unset=True).items():
            setattr(student, key, value)
        db.commit()
        db.refresh(student)
    return student

def create_user(db: Session, user: schemas.UserCreate):
    hashed_pw = bcrypt.hash(user.password)
    db_user = models.User(username=user.username, password=hashed_pw)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def authenticate_user(db: Session, username: str, password: str):
    user = db.query(models.User).filter(models.User.username == username).first()
    if not user or not bcrypt.verify(password, user.password):
        return None
    return user
