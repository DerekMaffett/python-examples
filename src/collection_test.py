from collection import _filter, filter_for_indices

def is_even(number):
    return number % 2 == 0

def test_filter():
    assert _filter(is_even, [1, 2, 3, 4, 5]) == [2, 4]

def test_filter_for_indices():
    assert filter_for_indices(is_even, [100, 12, 33, 97]) == [0, 1]
