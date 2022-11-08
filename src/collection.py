# NOTE: filter is an actual function in the core library so we name this _filter to differentiate it. It 
# does basically the same thing.

# This takes a list of items and a function f(x) returning a boolean, and returns the items that satistfy the function
def _filter(filter_fn, items):
    returned_items = []

    for item in items:
        if filter_fn(item):
            returned_items.append(item)

    return returned_items


# This is almost the same as filter, but returns the index of the items instead. The implementation is
# very similar overall, and now we can ignore the list-manipulation logic for the rest of our problems. 
def filter_for_indices(filter_fn, items):
    returned_items = []

    for index, item in enumerate(items):
        if filter_fn(item):
            returned_items.append(index)

    return returned_items

# While the above particular function is weird, most common operations on lists are covered in the core library or
# other common utility libraries.

# Examples:
#     - map - apply a transformation to each item in a list
#     - filter - create a new list of items matching a criteria
#     - reduce - iterate through a list to crunch them down to a single value or otherwise smaller data point
#     - find - return the first item in a list that matches a criteria, if any match
#     - any - do any items in this list fit a criteria?
#     - all - do ALL of the items in this list fit a criteria?
#     - zip - combine pairwise the items in two lists (like a zipper)

# These can all be done with for-loops and Python does appear to make greater use of them than many other languages, 
# but understanding especially the first four example operations (map/filter/reduce/find) can make it MUCH easier 
# to focus on the actual logic of the unique problem you're approaching. 
