__author__ = 'nikita_kartashov'

import matplotlib.pyplot as plt
from itertools import count, repeat


from repeat import pers_div, repeat_class_family, matching_repeat, sw_score, left_in_repeat_consensus, pers_div
from step1_read_data_from_file import get_clean_data, filterer_by, output_to_file, CHEETAH_DATA_FILE
from step2_groupby_family import perform_grouping, group_by


TARGET_CLASS_FAMILY = 'LINE/L2'


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
    return repeat_class_family(item), block


def get_target_block():
    return grouped_dict()[TARGET_CLASS_FAMILY]


def grouped_dict():
    return dict(map(block_to_map, perform_grouping()))


def sort_by_repeat_family(data):
    return sorted(data, key=repeat_class_family)


def group_to_dict_by_repeat_family(data):
    return dict(map(block_to_map, group_by(repeat_class_family, sort_by_repeat_family(data))))


def cluster_by_divergence(data, number_of_clusters):
    result = [0 for i in range(number_of_clusters)]
    for item in data:
        index = int(pers_div(item) // number_of_clusters)
        result[index] += 1
    return result

TARGET_REPEAT_CLASS = 'LINE/L2'

if __name__ == '__main__':
    # value = 'DNA/TcMar-Tc2'
    # i = 0
    # for item in filter(filterer_by(repeat_class_family, value), get_clean_data()):
    #     if i == 10:
    #         break
    #     print(item)
    #     i += 1
    # all_matched = filter(filterer_by(left_in_repeat_consensus, 0), get_clean_data())
    # # output_to_file(CHEETAH_DATA_FILE + '_' + 'fully_matched', all_matched)
    # grouped = group_to_dict_by_repeat_family(all_matched)
    # # print(zip(grouped.keys(), map(len, grouped.values())))
    # target_block = grouped[TARGET_REPEAT_CLASS]
    # sorted_by_divergence = sorted(target_block, key=pers_div)
    # number_of_clusters = 20
    # clustered_data = cluster_by_divergence(sorted_by_divergence, number_of_clusters)
    # print(clustered_data)
    # plt.plot(range(len(clustered_data)), clustered_data, 'ro')
    # plt.axis([0, len(clustered_data), 0, len(sorted_by_divergence)])
    # plt.show()

    filtered = filter(filterer_by(repeat_class_family, 'DNA?'), get_clean_data())
    output_to_file(CHEETAH_DATA_FILE + '_DNA_UNIDENTIFIED', filtered)