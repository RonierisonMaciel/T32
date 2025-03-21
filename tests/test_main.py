from app.services import get_tasks, add_task, update_task, delete_task
from app.models import Task

def test_add_task():
    task = Task(id=1, title="Title Task", description="Task Description", status=False)
    assert add_task(task) == task

def test_get_task():
    assert get_tasks(1)

def test_update_task():
    task_to_update = Task(id=1, title="Title Task", description="Task Description", status=True)
    updated_task = update_task(1, task_to_update)
    assert updated_task == task_to_update

def test_delete_task():
    assert delete_task(1) == {"message": "Task removida com sucesso!"}