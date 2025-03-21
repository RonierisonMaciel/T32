from app.database import tasks
from app.models import Task

# Function to get all tasks
def get_tasks(task_id: int):
    return next((task for task in tasks if task.id == task_id), None)

# Function to add a task
def add_task(task: Task):
    tasks.append(task)
    return task

# Function to update a task
def update_task(task_id: int, update_task: Task):
    for i, task in enumerate(tasks):
        if task.id == task_id:
            tasks[i] = update_task
            return update_task
    return None

# Function to delete a task
def delete_task(task_id: int):
    global tasks
    tasks = [task for task in tasks if task.id != task_id]
    return {"message": "Task removida com sucesso!"}
