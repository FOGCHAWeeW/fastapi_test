from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Привет, мир!"}

def test_read_hello():
    response =  client.get("/hello/Даня")
    assert response.status_code == 200
    assert response.json() == {"message": "Привет, Даня!"}