import pytest
from lib.grammarstats import *

def test_check():
    new_entry = GrammarStats()
    result = new_entry.check("Rise and shine.")
    assert result == True

def test_check_false():
    new_entry = GrammarStats()
    result = new_entry.check("rise and shine")
    assert result == False



def test_grammarstats():
    new_entry = GrammarStats()
    result = new_entry.check("Rise and shine")
    assert result == "Your grammar is a bit off"

def test_percentage_good():
    new_entry = GrammarStats()
    new_entry.check("Rise and shine.")
    assert new_entry.percentage_good() == 100

def test_percentage_halfgood():
    new_entry = GrammarStats()
    new_entry.check("Rise and shine")
    assert new_entry.percentage_good() == 50


def test_percentage_bad():
    new_entry = GrammarStats()
    new_entry.check("rise and shine")
    assert new_entry.percentage_good() == 0