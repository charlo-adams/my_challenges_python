import pytest
from lib.diary import * 

def test_format():
    my_entry = DiaryEntry('what happended', 'Today i saw a balloon')
    assert my_entry.format() == "what happended: Today i saw a balloon"


def test_format():
    new_entry = DiaryEntry('hello', )
    with pytest.raises(Exception) as err:
        new_entry.format()
    error_message = str(err.value)
    assert error_message == "nothing entered"


def test_format_again():
    diary = DiaryEntry('Monday the 17th of october', 'I caught a Gengar')
    assert diary.format() == "Monday the 17th of october: I caught a Gengar"

def test_count_words():
    diary = DiaryEntry('what happended', 'Today i saw a balloon')
    assert diary.count_words() == 7

def test_count_again():
    my_diary = DiaryEntry('Monday the 17th of october', 'I caught a Gengar')
    assert my_diary.count_words() == 9

def test_reading_time():
    diary = DiaryEntry('what happended', 'Today i saw a balloon and it floated away as i ran to it but it was gone so i cried alot')
    assert diary.reading_time(2) == 11

def test_uneven_reading_time():
    diary = DiaryEntry('In March', 'The sky was glowing and a meteor was approaching')
    assert diary.reading_time(4) == 2

def test_time_again():
    diary = DiaryEntry('in May', 'there was a dinosaur')
    assert diary.reading_time(3) == 1  

def test_reading_chunk():
    diary = DiaryEntry('what happended', 'Today i saw a balloon and it floated away as i ran to it but it was gone so i cried alot')
    result = diary.reading_chunk(2, 1)
    assert result == "Today i"

def test_chunk():
    diary = DiaryEntry('what happended', 'Today i saw a balloon and it floated away as i ran to it but it was gone so i cried alot')
    result = diary.reading_chunk(3, 3)
    assert result == "Today i saw a balloon and it floated away"


