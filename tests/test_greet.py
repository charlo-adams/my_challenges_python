from lib.greet import greet

def test_greet_angela():
    result = greet("angela")
    assert result == "Hello, angela!"