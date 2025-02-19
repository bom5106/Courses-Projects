from array import array
import array_utils
import merge_sort

def test_merge_sort():
    # setup
    an_array = array_utils.range_array(10, -1, -1)
    #invoke
    result = merge_sort.merge_sort(an_array)
    #analyze
    for i in range(len(result)):
        assert result[i] == i

def test_split_even():
    #setup
    an_array = array_utils.range_array(0,6)
    #invoke
    h1, h2 = merge_sort.split(an_array)
    #analyze
    assert len(h1) == 3
    assert h1[0] == 0
    assert h1[1] == 2
    assert h1[2] == 4
    assert len(h2) == 3
    assert h2[0] == 1
    assert h2[1] == 3
    assert h2[2] == 5

def test_split_odd():
    #setup
    an_array = array_utils.range_array(0,7)
    #invoke
    h1, h2 = merge_sort.split(an_array)
    #analyze
    assert len(h1) == 4
    assert h1[0] == 0
    assert h1[1] == 2
    assert h1[2] == 4
    assert h1[3] == 6
    assert len(h2) == 3
    assert h2[0] == 1
    assert h2[1] == 3
    assert h2[2] == 5

def test_merge():
    #setup
    a1 = array_utils.range_array(0,11,2)
    a2 = array_utils.range_array(1,11,2)
    #invoke
    result = merge_sort.merge(a1,a2)
    #analyze
    for i in range(len(result)):
        assert result[i] == i