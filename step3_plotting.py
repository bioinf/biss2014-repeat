__author__ = 'nikita_kartashov'

import matplotlib.pyplot as plt

from step1_reading_writing_file import get_clean_data
from step2_sorting_aggregating import filter_fully_matching, \
    group_by_repeat_family, cluster_by_divergence, items_in_clusters


CHEETAH_DATA_FILE = '/Users/nikita_kartashov/Downloads/cheetah_scaffolds.fa.out'
TARGET_REPEAT_CLASS = 'LINE/L2'

if __name__ == '__main__':
    fully_matched = filter_fully_matching(get_clean_data(CHEETAH_DATA_FILE))
    grouped_by_repeat_family = group_by_repeat_family(fully_matched)
    target_block = grouped_by_repeat_family[TARGET_REPEAT_CLASS]
    min_divergence = 0
    max_divergence = 50
    number_of_clusters = 1000
    clustered_by_divergence = cluster_by_divergence(target_block,
                                                    min_divergence,
                                                    max_divergence,
                                                    number_of_clusters)
    cluster_sizes = items_in_clusters(clustered_by_divergence)
    plt.plot(range(number_of_clusters), cluster_sizes, 'ro')
    plt.axis([0, number_of_clusters, 0, max(cluster_sizes)])
    plt.show()
