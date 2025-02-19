from quick_sort import *
import random
import array_utils

def test_partition():
    # setup
    an_array = array_utils.range_array(0,11)
    an_array[0] = 5
    # invoke
    less, same, more = partition(5, an_array)
    # analyze
    assert len(less) == 4
    assert less[0] == 1
    assert less[1] == 2
    assert less[2] == 3
    assert less[3] == 4
    assert len(same) == 2
    assert same[0] == 5
    assert same[1] == 5
    assert len(more) == 5
    assert more[0] == 6
    assert more[1] == 7
    assert more[2] == 8
    assert more[3] == 9
    assert more[4] == 10

def test_quick_sort():
    #  setup
    random.seed(1)
    an_array = array_utils.random_array(10)
    # invoke
    sorted = quick_sort_random(an_array)
    # analyze
    for i in range(1, len(sorted)):
        assert sorted[i] >= sorted[i-1]