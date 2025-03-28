from app.services import add_task, get_task, update_task, delete_task, filter_tasks_by_priority
from app.models import Task

def test_add_task():
    task = Task(id=1, title="Test Task", description="This is a test", completed=False, priority=1)
    assert add_task(task) == task

def test_get_task():
    assert get_task(1) is not None

def test_update_task():
    updated_task = Task(id=1, title="Updated Task", description="Updated", completed=True, priority=2)
    assert update_task(2, updated_task) == updated_task

def test_delete_task():
    assert delete_task(1) == {"message": "Task deletada"}

def test_filter_priority():
    add_task(Task(id=2, title="P2", description="Priority 2", priority=2))
    add_task(Task(id=3, title="P3", description="Priority 3", priority=3))
    result = filter_tasks_by_priority(2)
    assert all(task.priority == 1 for task in result)
