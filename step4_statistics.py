__author__ = 'nikita_kartashov'

from repeat import query_position_begin, query_position_end
from step1_reading_writing_file import get_clean_data, dump_repeat_sequences
from step2_sorting_aggregating import filter_fully_matching, \
    group_by_repeat_family, group_by_matching_repeat

from fasta_sequence import read_naive_fasta

CHEETAH_DATA_FILE = '/Users/nikita_kartashov/Downloads/cheetah_scaffolds.fa.out'
TARGET_REPEAT_CLASS = 'LINE/L1'
GENOME_FILE_PATH = '/Users/nikita_kartashov/Downloads/cheetahScaffoldsRmTrf.fa'
REPEATS_TO_ALIGN = 'repeats_to_align.txt'


def get_samples(data, number):
    if len(data) < number:
        return data
    if number <= 0:
        return []
    return data[:number]


def conservativeness(data, fasta_sequence):
    pass


if __name__ == '__main__':
    fully_matched = filter_fully_matching(get_clean_data(CHEETAH_DATA_FILE))
    grouped_by_repeat_family = group_by_repeat_family(fully_matched)
    target_block = grouped_by_repeat_family[TARGET_REPEAT_CLASS]
    grouped_by_matching_repeat = group_by_matching_repeat(target_block)
    sequence = read_naive_fasta(GENOME_FILE_PATH)
    dump_repeat_sequences(target_block, sequence, REPEATS_TO_ALIGN)