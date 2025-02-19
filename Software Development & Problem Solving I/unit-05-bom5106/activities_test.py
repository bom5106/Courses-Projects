from activities import *

def text_exponent():
    #set up
    base = 5
    power = 3
    expected = 5 ** 3
    #invoke
    actual = exponent(base, power)
    #analyze
    assert expected == actual

def test_exponent_negative():
    #setup
    base = 5
    power = -3
    #invoke
    try:
        exponent(base, power)
        assert(False)
    except ValueError:
        assert True