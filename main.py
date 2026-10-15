from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Привет, мир!"}

@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Привет, {name}!"}

@app.post("/users")
def create_user(user: User):
    return {"message": f"Создан пользователь {user.name}, \
            возраст {user.age}"}




