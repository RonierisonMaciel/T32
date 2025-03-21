from fastapi import FastAPI, HTTPException, Query
from app.models import Task
from app.database import tasks
from app.services import get_task, add_task, update_task, delete_task, filter_tasks_by_priority

app = FastAPI()

@app.get("/tasks")
def list_tasks(priority: int = Query(None)):
    if priority:
        return filter_tasks_by_priority(priority)
    return tasks.copy()

@app.post("/tasks")
def create_task(task: Task):
    if any(t.id == task.id for t in tasks):
        raise HTTPException(status_code=400, detail="Task ID já existe")
    if task.priority < 1 or task.priority > 6:
        raise HTTPException(status_code=422, detail="Prioridade deve estar entre 1 e 5")
    return add_task(task)

@app.get("/tasks/{task_id}")
def read_task(task_id: int):
    task = get_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task não encontrada")
    return task

@app.put("/tasks/{task_id}")
def update_existing_task(task_id: int, task: Task):
    if task_id != task.id:
        raise HTTPException(status_code=400, detail="ID da task no corpo e na URL são diferentes")
    existing = get_task(task_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Task não encontrada")
    return update_task(task_id, task)

@app.delete("/tasks/{task_id}")
def remove_task(task_id: int):
    task = get_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task não encontrada")
    return delete_task(task_id)

@app.patch("/tasks/{task_id}/complete")
def mark_task_complete(task_id: int):
    task = get_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task não encontrada")
    task.completed = True
    return task
