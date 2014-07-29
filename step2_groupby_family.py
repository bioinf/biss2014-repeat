__author__ = 'nikita_kartashov'

from os import path

from step1_read_data_from_file import perform_sorting_by_family
from repeat import repeat_class_family, pers_div, split_repeat_line

CHEETAH_SORTED_DATA_FILE = '/Users/nikita_kartashov/Downloads/cheetah_scaffolds.fa.out_repeat_class'


def read_data(filename):
    if path.exists(filename):
        with open(CHEETAH_SORTED_DATA_FILE, 'r') as data_file:
            input_data = data_file.readlines()
        return map(split_repeat_line, input_data)
    else:
        return perform_sorting_by_family()


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

def divergence_sort(block):
    return sorted(block, key=pers_div)


def perform_grouping():
    input_data = read_data(CHEETAH_SORTED_DATA_FILE)
    grouped_data = group_by(repeat_class_family, input_data)
    grouped_data_sorted_by_less_divergence = map(divergence_sort, grouped_data)
    return grouped_data_sorted_by_less_divergence

if __name__ == '__main__':
    perform_grouping()