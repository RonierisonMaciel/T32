from pydantic import BaseModel

# Class Task is a model for the task object
class Task(BaseModel):
    id: int
    title: str
    description: str
    status: bool = False