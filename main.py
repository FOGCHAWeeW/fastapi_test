from fastapi import FastAPI, Depends, HTTPException, APIRouter
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models
import fastapi_swagger_dark

models.Base.metadata.create_all(bind=engine)

app = FastAPI(docs_url=None)
router = APIRouter()
fastapi_swagger_dark.install(router)
app.include_router(router)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class UserCreate(BaseModel):
    name: str
    age: int

class UserResponse(BaseModel):
    id: int
    name: str
    age: int

    class Config:
        from_attributes = True     

@router.post("/users", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = models.User(name=user.name, age=user.age)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.get("/users", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()

@router.get("/users/{users_id}")
def get_user(users_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == users_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/users/{users_id}")
def del_user(users_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == users_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    else:
        db.delete(user)
        db.commit()
    return {"message": f"{user.name} deleted"}

@router.get("/")
def read_root():
    return {"message": "Привет, мир!"}

@router.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Привет, {name}!"}