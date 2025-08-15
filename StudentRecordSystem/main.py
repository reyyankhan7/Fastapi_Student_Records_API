from fastapi import FastAPI
from . import models, database
from .routers import auth, student

models.Base.metadata.create_all(bind=database.engine)
app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(student.router, prefix="/students", tags=["Students"])
