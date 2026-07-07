import pytest
from lib.present import *

def test_my_presents():
   my_present = Present()
   my_present.wrap("a bicycle shaped box")
   assert my_present.unwrap() == "a bicycle shaped box"


def test_no_present():
    present = Present()
    with pytest.raises(Exception) as err:
        present.unwrap()
    error_message = str(err.value)
    assert error_message == "No contents have been wrapped."

def test_present_again():
    new_present = Present()
    new_present.wrap("box")
    with pytest.raises(Exception) as err:
        new_present.wrap("pillow")
    error_mess = str(err.value)
    assert error_mess == "A contents has already been wrapped."

def test_already_wrapped_present():
    present = Present()
    present.wrap(44)
    with pytest.raises(Exception) as e:
        present.wrap(67)
    assert present.unwrap() == 44