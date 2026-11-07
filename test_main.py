from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"mensagem": "API rodando com sucesso!"}


def test_somar():
    response = client.get("/somar/10/20")
    assert response.status_code == 200
    assert response.json() == {"resultado": 30}


def test_multiplicar():
    # Na Parte 3, você fará este teste falhar de propósito alterando o esperado para 5
    response = client.get("/multiplicar/2/2")
    assert response.status_code == 200
    assert response.json() == {"resultado": 4}