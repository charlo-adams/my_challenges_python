from lib.string_builder import *

def test_for_string_working():
    my_string = StringBuilder()
    my_string.add("Gengar")
    assert my_string.output() == "Gengar"


def test_for_string_working_length():
    my_string = StringBuilder()
    my_string.add("Gengar")
    assert my_string.size() == 6


def test_for_string_working_2():
    my_string = StringBuilder()
    my_string.add("Dragonite")
    assert my_string.output() == "Dragonite"