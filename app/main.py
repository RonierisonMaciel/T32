from fastapi import FastAPI, HTTPException
from app.models import Task
from app.database import tasks
from app.services import get_tasks, add_task, update_task, delete_task

app = FastAPI()

# Function to root
@app.get("/")
async def root():
    return {"message": "Bem vindo a API de tarefas!"}

# Function to get all tasks
@app.get("/tasks")
async def list_tasks():
    return tasks

# Function to create a task
@app.post("/tasks")
async def create_task(task: Task):
    return add_task(task)

# Function to get a task
@app.get("/tasks/{task_id}")
async def read_task(task_id: int):
    task = get_tasks(task_id)
    if not task:
        return HTTPException(status_code=404, detail="Task not encontrada")
    return task

# Function to update a task
@app.put("/tasks/{task_id}")
async def update_task(task_id: int):
    return update_task(task_id)

# Function to delete a task
@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    return delete_task(task_id)
