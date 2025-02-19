def test_square_area_8():
    answer = square_area(8)
    assert answer == 64

def test_square_area_6():
    answer = square_area(6)
    assert answer == 36

def test_square_area_4():
    answer = square_area(4)
    assert answer == 16

def test_square_area_negative():
    answer = square_area(-1)
    assert answer == None

def square_area(side):
    answer = None
    if side >= 0:
        answer = side * side 
    return answer