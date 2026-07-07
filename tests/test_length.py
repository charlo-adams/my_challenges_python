from lib.report_length import report_length

def test_length_of_string():
    result = report_length("charlotte")
    assert result == "This string was 9 characters long"


def test_length_of_other_string():
    result = report_length("beer")
    assert result == "This string was 4 characters long"


