from fastapi import FastAPI
from fastapi.testclient import TestClient

# Créer une instance de l'application FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "OK"}

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "OK"}
