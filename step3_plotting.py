__author__ = 'nikita_kartashov'

import matplotlib.pyplot as plt
from itertools import count


from repeat import pers_div, repeat_class, matching_repeat, sw_score, matching_repeat
from step2_groupby_family import perform_grouping, group_by


def first_n(l, n):
    return l[:n]


def first_ten(l):
    return first_n(l, 10)


def prepare_block(block):
    return map(matching_repeat, block), zip(map(pers_div, block), count())


def prepare_data(blocks):
    return map(prepare_block, blocks)

def block_to_map(block):
    item = block[0]
    return repeat_class(item), block

if __name__ == '__main__':
    grouped_and_sorted = perform_grouping()
    dict_by_family = dict(map(block_to_map, grouped_and_sorted))
    print(dict_by_family.keys())
    # block = grouped_and_sorted[0]
    # sorted_by_matching_repeat = sorted(block, key=matching_repeat)
    # grouped_by_matching_repeat = group_by(matching_repeat, sorted_by_matching_repeat)
    # print(len(set(map(matching_repeat, block))))
    # print(len(block))