from lib.todo_list import *
from lib.todo import *

def test_add_todo():
    job_1 = ToDo('Go shopping')
    todo_list = ToDoList()
    todo_list.add_todo(job_1)
    assert todo_list.todos == [job_1]