from pydantic import BaseModel

class StudentBase(BaseModel):
    name: str
    age: int
    student_class: str

class StudentCreate(StudentBase):
    pass

class StudentUpdate(BaseModel):
    name: str | None = None
    age: int | None = None
    student_class: str | None = None

class StudentOut(StudentBase):
    id: int
    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str
