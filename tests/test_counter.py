from lib.counter import *

def test_how_much_was_counted():
    current_count = Counter()
    current_count.add(3)
    result = current_count.report()
    assert result == "Counted to 3 so far."