from collection import _filter, filter_for_indices

def is_even(number):
    return number % 2 == 0

def test_filter():
    assert _filter(is_even, [1, 2, 3, 4, 5]) == [2, 4]

def test_filter_for_indices():
    assert filter_for_indices(is_even, [100, 12, 33, 97]) == [0, 1]


# NOTE: UNNECESSARY BUT INTERESTING INFORMATION AHEAD!
# The following test is just to show that the core library version of `filter` is very similar
# to what we designed here. The extra "list" call is needed simply because filter returns 
# an iterator rather than an actual array. While I'm not an expert on the why behind this, it basically
# means that the data needs to be traversed in order to make it "real" - until then it's more of a system
# that can *create* an array. 

# One reason for this type of construction is lazy evaluation - an array with a billion items might overload 
# memory, but an Iterator could have infinite items without issue as long as a program only asks for ten of them.
def test_core_library_filter():
    assert list(filter(is_even, [1, 2, 3, 4, 5])) == [2, 4]
