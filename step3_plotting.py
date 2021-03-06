__author__ = 'nikita_kartashov'

import matplotlib.pyplot as plt

from step1_reading_writing_file import get_clean_data
from step2_sorting_aggregating import filter_fully_matching, \
    group_by_repeat_family, cluster_by_divergence, items_in_clusters, group_by_matching_repeat, items_in_values

from repeat import repeat_length


CHEETAH_DATA_FILE = '/Users/nikita_kartashov/Downloads/cheetah_scaffolds.fa.out'
TARGET_REPEAT_CLASS = 'SINE/tRNA'


if __name__ == '__main__':
    fully_matched = filter_fully_matching(get_clean_data(CHEETAH_DATA_FILE))
    grouped_by_repeat_family = group_by_repeat_family(fully_matched)
    target_block = grouped_by_repeat_family[TARGET_REPEAT_CLASS]
    grouped_by_matching_repeat = group_by_matching_repeat(target_block)
    target_matching_repeats = ['SINEC_Fc3', 'SINEC_Fc2', 'SINEC_Fc']
    t = [grouped_by_matching_repeat[target_repeat] for target_repeat in target_matching_repeats]
    min_divergence = 0
    max_divergence = 50
    number_of_clusters = 10000
    c = [cluster_by_divergence(data, min_divergence, max_divergence, number_of_clusters) for data in t]
    print(repeat_length(grouped_by_matching_repeat[target_matching_repeats[0]][0]))
    c = map(items_in_clusters, c)
    plt.plot(range(number_of_clusters), c[0], 'ro', c[1], 'bo', c[2], 'go')
    plt.axis([0, number_of_clusters, 0, max(max(c))])
    plt.show()
