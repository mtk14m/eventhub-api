from fastapi.testclient import TestClient

from eventhub.main import app

client = TestClient(app)

def test_health_smoke():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status":"ok"}