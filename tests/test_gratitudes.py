from lib.gratitudes import *

def test_if_gratitude_working():
    my_gratitude = Gratitudes()
    my_gratitude.add("the clean air that we breath")
    assert my_gratitude.format() == "Be grateful for: the clean air that we breath"


def test_2_for_gratidue():
    new_gratitude = Gratitudes()
    new_gratitude.add("the fact that an asteroid hasn't taken us all out yet")
    assert new_gratitude.format() == "Be grateful for: the fact that an asteroid hasn't taken us all out yet"