__author__ = 'nikita_kartashov'

from repeat import sw_score, repeat_class_family, matching_repeat, make_file_repr,\
    split_repeat_line, query_position_begin, query_position_end


def output_to_file(filename, data, repr_func=make_file_repr):
    """
    Outputs all tuples to file using *repr_func*
    :param filename: file to dump the data to
    :param data: iterable of data tuples
    :param repr_func: function returning the string representation of the tuple
    :return: None
    """
    with open(filename, 'w') as outfile:
        outfile.writelines(map(repr_func, data))


def get_all_data(filename, open_mode='r'):
    """
    Naively reads all data from *filename* to memory
    :param filename: file with data
    :param open_mode: mode of opening the file
    :return: all lines from file
    """
    with open(filename, open_mode) as input_file:
        return input_file.readlines()


def skip_annotations(lines):
    """
    Returns clean data from a file for processing
    :param lines: lines of the input file
    :return: lines but the first 3 as they are annotations
    """
    return lines[3:]


def get_clean_data(filename):
    """
    Gets all data from
    :param filename file with data
    :return: list of data tuples
    """
    return map(split_repeat_line, skip_annotations(get_all_data(filename)))


def get_repeat_sequences(data, sequence):
    """
    NOT YET WORKING
    :param data:
    :param sequence:
    :return:
    """
    return [sequence.slice(query_position_begin(item), query_position_end(item)) for item in data]


def get_repeat_sequences_naive(data, sequence):
    """
    Gets repeats from genome using data tuples provided
    :param data: provided data tuples
    :param sequence: genome
    :return: requested repeats
    """
    return [sequence[query_position_begin(item): query_position_end(item)] for item in data]


def dump_repeat_sequences_fasta_format(data_tuples, sequence, filename, tuple_getter=get_repeat_sequences_naive):
    """
    Dumps the repeats from genome using tuples in *data_tuples*
    :param data_tuples: repeat data tuples
    :param sequence: genome
    :param filename: output file
    :param tuple_getter: function extracting repeats from genome
    :return: None
    """
    data = tuple_getter(data_tuples, sequence)
    with open(filename, 'a') as output_file:
        for index, line in enumerate(data):
            output_file.write('>sequence{0}\n'.format(index))
            output_file.write('{0}\n'.format(line))