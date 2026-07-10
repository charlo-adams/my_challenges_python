import pytest
from lib.toy_store import *

def test_toy_store_creates_empty_list():
    toy_store = ToyStore()
    assert toy_store.toy_list == [] 

def test_add_a_toy_and_store_in_list():
    toy_store = ToyStore()
    toy_store.add("Dubai chocolate labubu") 
    assert toy_store.toy_list == ["Dubai chocolate labubu"]

def test_two_toys_are_added_to_list():
    toy_store = ToyStore()
    toy_store.add("Dubai chocolate labubu")
    toy_store.add("Millennium Falcon") 
    assert toy_store.toy_list == ["Dubai chocolate labubu", "Millennium Falcon"]

def test_see_list_of_toys():
    toy_store = ToyStore()
    toy_store.add("Dubai chocolate labubu")
    toy_store.add("Millennium Falcon")
    toy_store.add("Smiski")
    assert toy_store.see_toys() == ["Dubai chocolate labubu", "Millennium Falcon", "Smiski"]

def test_toy_that_is_a_number():
    toy_store = ToyStore()
    with pytest.raises(Exception) as err:
        toy_store.add(9)
    error_message = str(err.value)
    assert error_message == "toy must be a string"

