def _filter(filter_fn, items):
    returned_items = []

    for item in items:
        if filter_fn(item):
            returned_items.append(item)

    return returned_items


def filter_for_indices(filter_fn, items):
    returned_items = []

    for index, item in enumerate(items):
        if filter_fn(item):
            returned_items.append(index)

    return returned_items
