from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_task():
    response = client.post("/tasks", json={"id": 1, "title": "Test", "description": "Testing", "completed": False, "priority": 1})
    assert response.status_code == 200

def test_priority_filter():
    client.post("/tasks", json={"id": 10, "title": "Low", "description": "Low Priority", "completed": False, "priority": 5})
    
    response = client.get("/tasks?priority=5")
    
    assert response.status_code == 200
    
    tasks = response.json()
    assert any(task["priority"] == 5 for task in tasks), "Nenhuma tarefa com prioridade 5 foi encontrada"


def test_patch_completion():
    client.post("/tasks", json={"id": 20, "title": "Complete me", "description": "To be done", "completed": False, "priority": 3})
    response = client.patch("/tasks/20/complete")
    assert response.status_code == 200
    assert response.json()["completed"] == True
