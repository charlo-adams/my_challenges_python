from lib.check_codeword import check_codeword

def test_codeword_is_correct():
    result = check_codeword("horse")
    assert result == "Correct! Come in."


def test_codeword_is_wrong():
    result = check_codeword("griffin")
    assert result == "WRONG!"

def test_codeword_is_close():
    result = check_codeword("homoie")
    assert result == "Close, but nope."