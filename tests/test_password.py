import pytest
from lib.password_checker import *

def test_password_length():
    my_password = PasswordChecker()
    with pytest.raises(Exception) as e:
        my_password.check("diasy")
    error_mess = str(e.value)
    assert error_mess == "Invalid password, must be 8+ characters."


def test_password_correct_length():
    my_password = PasswordChecker()
    result = my_password.check("Judge Judy")
    assert result == True
