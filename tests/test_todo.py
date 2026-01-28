from lib.todo import *

def test_sets_todo_on_initialisation():
    job_1 = ToDo('Go shopping')
    assert job_1.todo == 'Go shopping'