import pytest
from lib.todo_list import *

def test_add():
    my_to_do = ToDo_list()
    result = my_to_do.add("Walk the dog")
    assert result == ["Walk the dog"]


def test_add_two_tasks_1():
    my_to_do = ToDo_list()
    result = my_to_do.add("water the plants")
    assert result == ["water the plants"]

def test_add_two_tasks():
    my_to_do = ToDo_list()
    result = my_to_do.add("water the plants") and my_to_do.add("Walk the dog")
    assert result == ["water the plants", "Walk the dog"]

def test_mark_complete():
    my_to_do = ToDo_list()
    my_to_do.add("water the plants") and my_to_do.add("Walk the dog") and my_to_do.add("go shopping")
    result = my_to_do.mark_complete("water the plants")
    assert result == ["Walk the dog", "go shopping"]
    
def test_mark_complete_2():
    my_to_do = ToDo_list()
    my_to_do.add("water the plants") and my_to_do.add("Walk the dog") and my_to_do.add("go shopping")
    result = my_to_do.mark_complete("Walk the dog")
    assert result == ["water the plants", "go shopping"]

def test_mark_complete_3():
    my_to_do = ToDo_list()
    my_to_do.add("Walk the dog") 
    result = my_to_do.mark_complete("Walk the dog")
    assert result == []