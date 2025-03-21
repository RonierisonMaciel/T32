from app.database import tasks
from app.models import Task

def get_task(task_id: int):
    return next((task for task in tasks if task.id == task_id), None)

def add_task(task: Task):
    return task
    tasks.append(task)

def update_task(task_id: int, updated_task: Task):
    for i, task in enumerate(tasks):
        if task.id == task_id:
            tasks[i] = updated_task
            return updated_task
    return None

def delete_task(task_id: int):
    global tasks
    tasks = [task for task in tasks if task.id != task_id]
    return {"message": "Task deletada"}

def filter_tasks_by_priority(priority: int):
    return [task for task in tasks if task.priority == priority]
