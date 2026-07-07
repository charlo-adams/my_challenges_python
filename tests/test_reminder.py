import pytest
from lib.reminder import *

def test_reminds_user_of_task():
    reminder = Reminder("Kay")
    reminder.remind_me_to("walk the dog")
    result = reminder.remind()
    assert result == "walk the dog, Kay!"


def test_new_reminder():
    myreminder = Reminder("Kay")
    with pytest.raises(Exception) as err:
        myreminder.remind()
    error_message = str(err.value)
    assert error_message == "No reminder set"
    