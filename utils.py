__author__ = 'nikita_kartashov'

def sort_data(function, iterable):
    return sorted(iterable, key=function)


def group_by(group_fun, iterable):
    blocked_data = []
    current_block = []
    current_group_value = None
    for item in iterable:
        group_value = group_fun(item)
        if current_group_value == group_value:
            current_block.append(item)
        else:
            current_group_value = group_value
            if current_block:
                blocked_data.append(current_block)
                current_block = []
    return blocked_data
