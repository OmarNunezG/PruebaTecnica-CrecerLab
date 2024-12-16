import uuid

from fastapi.testclient import TestClient
from fastapi import status

from app.main import app

client = TestClient(app)


def test_create_event():
    payload = {
        "description": "string",
        "user_id": str(uuid.uuid4()),
    }
    response = client.post("/events", json=payload)
    assert response.status_code == status.HTTP_200_OK
    assert "Location2" in response.headers
